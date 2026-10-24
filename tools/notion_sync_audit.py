#!/usr/bin/env python3
"""Read-only source-path/content audit of Yugatn/story-x against Notion."""
import csv, html, json, os, re, subprocess, sys, time
from collections import defaultdict
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API="https://api.notion.com/v1"
ROOT=os.environ.get("NOTION_PARENT_PAGE_ID","403d1323-8599-817f-855b-e71fde012476")
TOKEN=os.environ.get("NOTION_TOKEN")
SRC=re.compile(r"github\.com/Yugatn/story-x/blob/(?:main|master)/([^\s)\]>\"']+)",re.I)
FILE=re.compile(r"(?:Исходный файл|Источник файла):\s*`?([\w./ -]+\.(?:md|html))",re.I)

def request(path):
    for attempt in range(7):
        try:
            with urlopen(Request(API+path,headers={"Authorization":"Bearer "+TOKEN,"Notion-Version":"2022-06-28"}),timeout=60) as r:
                return json.load(r)
        except HTTPError as e:
            if e.code==429 and attempt<6:
                time.sleep(float(e.headers.get("Retry-After","2"))+.5); continue
            raise

def children(block):
    cursor=None
    while True:
        url="/blocks/"+block+"/children?page_size=100"+("&start_cursor="+cursor if cursor else "")
        page=request(url)
        yield from page["results"]
        if not page.get("has_more"): break
        cursor=page["next_cursor"]
        time.sleep(.36)

def text_blocks(page):
    parts=[]
    def scan(block,depth):
        for b in children(block):
            obj=b.get(b.get("type",""),{})
            if "rich_text" in obj:
                for rich in obj["rich_text"]:
                    parts.append(rich.get("plain_text",""))
                    if rich.get("href"): parts.append(rich["href"])
            elif b.get("type")=="bookmark": parts.append(obj.get("url",""))
            if b.get("has_children") and b.get("type")!="child_page" and depth<8:
                scan(b["id"],depth+1)
    scan(page,0)
    return "\n\n".join(parts)

def norm(s):
    s=html.unescape(s)
    s=re.sub(r"!?\[([^\]]+)\]\([^)]*\)",r"\1",s)
    s=re.sub(r"<[^>]+>","",s)
    s=re.sub(r"\\([_*\[\]])",r"\1",s)
    return " ".join(re.sub(r"[*_`]","",s).split())

def main():
    if not TOKEN: sys.exit("Missing NOTION_TOKEN repository secret.")
    repo=Path(".")
    tracked=[p.decode() for p in subprocess.check_output(["git","ls-files","-z"]).split(b"\0") if p]
    tracked=sorted(p for p in tracked if not p.startswith(".github/workflows/notion-sync-audit") and p!="tools/notion_sync_audit.py")
    known=set(tracked)
    pages=[(b["id"],b["child_page"].get("title","")) for b in children(ROOT)
           if b.get("type")=="child_page" and (b["child_page"].get("title","").startswith("Архив оригинала") or b["child_page"].get("title","").startswith("Сюжет Икс — источник"))]
    mapped=defaultdict(list); ambiguous=[]
    for index,(pid,title) in enumerate(pages,1):
        try:
            text=text_blocks(pid)
            paths={p for p in SRC.findall(text) if p in known}
            paths.update(p.strip() for p in FILE.findall(text) if p.strip() in known)
            if len(paths)==1:
                mapped[next(iter(paths))].append((pid,text))
            else: ambiguous.append({"notion_id":pid,"title":title,"source_paths":sorted(paths)})
        except Exception as e: ambiguous.append({"notion_id":pid,"title":title,"error":str(e)})
        if index%50==0: print("Pages checked:",index,"/",len(pages),flush=True)
        time.sleep(.36)
    rows=[]
    for path in tracked:
        copies=mapped.get(path,[])
        matched=total=0
        if not copies: status="missing_or_unmapped"
        elif len(copies)>1: status="duplicate_review"
        elif not path.endswith(".md"): status="format_review"
        else: status="present"
        if copies and path.endswith(".md"):
            raw=(repo/path).read_text(encoding="utf-8",errors="replace")
            pars=[p.strip() for p in re.split(r"\n\s*\n",raw) if len(p.strip())>=100 and not p.lstrip().startswith(("#","- ","* ",">"))]
            total=len(pars)
            matched=max(sum(norm(p) in norm(body) for p in pars) for _,body in copies)
            if matched<total: status="content_review" if len(copies)==1 else "duplicate_review"
        sha=subprocess.check_output(["git","hash-object","--",path],text=True).strip()
        rows.append({"path":path,"git_blob_sha":sha,"status":status,"pages":len(copies),
                     "matched_paragraphs":matched,"checked_paragraphs":total,
                     "notion_urls":" | ".join("https://www.notion.so/"+pid.replace("-","") for pid,_ in copies)})
    out=Path("notion-audit-output");out.mkdir(exist_ok=True)
    with (out/"report.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    counts={s:sum(r["status"]==s for r in rows) for s in sorted(set(r["status"] for r in rows))}
    (out/"report.json").write_text(json.dumps({"counts":counts,"ambiguous":ambiguous,"rows":rows},ensure_ascii=False,indent=2),encoding="utf-8")
    lines=["# Story-X / Notion archive audit","",f"Git files: {len(tracked)}",f"Notion archive candidates: {len(pages)}",""]
    lines += [f"- {k}: {v}" for k,v in counts.items()]
    lines += ["",f"Unmapped or ambiguous pages: {len(ambiguous)}","",
              "This is a read-only audit. Apparent missing files require manual review. No byte-identical claim."]
    (out/"summary.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as f:f.write("\n".join(lines)+"\n")
    print("\n".join(lines))
if __name__=="__main__":main()
