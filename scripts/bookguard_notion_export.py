#!/usr/bin/env python3
"""Export configured Notion page trees to a local directory. No credentials in files."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import urllib.parse
import urllib.request

API = "https://api.notion.com/v1/"

def request(path, token):
    req = urllib.request.Request(API + path, headers={
        "Authorization": "Bearer " + token, "Notion-Version": "2022-06-28"})
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)

def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dest", type=Path, required=True)
    parser.add_argument("--pages", required=True, help="Comma-separated Notion page UUIDs")
    args = parser.parse_args()
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        raise ValueError("NOTION_TOKEN environment variable required")
    roots = [x.strip().replace("-", "") for x in args.pages.split(",") if x.strip()]
    if not roots or any(len(x) != 32 or not all(c in "0123456789abcdefABCDEF" for c in x) for x in roots):
        raise ValueError("Supply valid Notion page UUIDs")
    dest = args.dest.resolve()
    if dest.exists() and any(dest.iterdir()):
        raise ValueError("Destination must be empty")
    dest.mkdir(parents=True, exist_ok=True)
    pending, visited = list(roots), set()
    while pending:
        page_id = pending.pop()
        if page_id in visited:
            continue
        visited.add(page_id)
        page = request("pages/" + page_id, token)
        write_json(dest / (page_id + ".page.json"), page)
        blocks, cursor = [], None
        while True:
            path = "blocks/" + page_id + "/children?page_size=100"
            if cursor:
                path += "&start_cursor=" + urllib.parse.quote(cursor)
            result = request(path, token)
            blocks.extend(result["results"])
            for block in result["results"]:
                if block.get("has_children"):
                    pending.append(block["id"].replace("-", ""))
            if not result.get("has_more"):
                break
            cursor = result.get("next_cursor")
            if not cursor:
                raise ValueError("Pagination cursor missing")
        write_json(dest / (page_id + ".blocks.json"), blocks)
    checksums = {}
    for path in sorted(dest.glob("*.json")):
        checksums[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    write_json(dest / "manifest.json", {"schema": 1, "roots": roots, "items": len(visited),
                                      "sha256": checksums, "limitations": [
                                      "Notion file attachments are references only, not downloaded",
                                      "Database rows are not exported unless present as traversable child pages",
                                      "Notion comments, history, permissions and external linked data not included"]})
    for name, expected in checksums.items():
        actual = hashlib.sha256((dest / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError("Checksum mismatch: " + name)
    print(json.dumps({"status": "EXPORT_VERIFIED", "pages_and_blocks": len(visited), "files": len(checksums)}))

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("NOTION_BACKUP_BLOCKED:", error, file=sys.stderr)
        sys.exit(1)
