#!/usr/bin/env python3
"""Reproducible one-file Word backup for Story X. Preserves every Markdown source."""
from __future__ import annotations
import hashlib, json, re, subprocess
from datetime import datetime, timezone
from pathlib import Path
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parent.parent
OUTDIR = ROOT / 'exports'
OUTDIR.mkdir(exist_ok=True)
OUTPUT = OUTDIR / 'SYUZHET_IKS_POLNOE_RABOCHEE_SOBRANIE_2026_11_03.docx'
MANIFEST = OUTDIR / 'SYUZHET_IKS_SOSTAV_SBORKI_2026_11_03.json'
IGNORE_DIRS = {'.git', '.github', 'exports', '__pycache__', '.venv'}
files = [p for p in ROOT.rglob('*.md') if not (set(p.relative_to(ROOT).parts) & IGNORE_DIRS)]
files.sort(key=lambda p: p.relative_to(ROOT).as_posix().lower())

PRIORITY = '00_CANONICAL_PROLOGUE_YUDZHIN.md'
def grouping(p):
    r=p.relative_to(ROOT).as_posix()
    b=p.name
    if r == PRIORITY or re.match(r'^\d+_CHAPTER_(?!MAP)', b): return 'narrative'
    if r.startswith('NOTION_WORKING/'): return 'notion'
    if (re.match(r'^\d+_', b) or b.startswith(('CHAPTER_', 'EPISODE_', 'BROTSKY_', 'BARDO_', 'CITY_X_', 'THE_'))):
        return 'supplement'
    return 'documents'

groups = {'narrative':[], 'supplement':[], 'notion':[], 'documents':[]}
for p in files: groups[grouping(p)].append(p)
def file_order(p):
    m=re.match(r'^(\d+)_',p.name)
    if p.name==PRIORITY: return (-1,p.name)
    return (int(m.group(1)) if m else 9999,p.name)
for group in ['narrative','supplement']:
    groups[group].sort(key=file_order)
try:
    commit=subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip()
except Exception:
    commit='commit not available'

DOC=Document()
sec=DOC.sections[0]
sec.page_height=Cm(29.7); sec.page_width=Cm(21)
sec.top_margin=Cm(1.8); sec.bottom_margin=Cm(1.8)
sec.left_margin=Cm(2.25); sec.right_margin=Cm(1.8)
sec.header_distance=Cm(0.8); sec.footer_distance=Cm(0.8)
normal=DOC.styles['Normal']; normal.font.name='Times New Roman'; normal.font.size=Pt(10.5)
normal.paragraph_format.space_after=Pt(5);normal.paragraph_format.line_spacing=1.08
for sname,pts,bold in [('Title',26,True),('Heading 1',17,True),('Heading 2',13,True),('Heading 3',11,True)]:
    style=DOC.styles[sname]; style.font.name='Times New Roman'; style.font.size=Pt(pts);style.font.bold=bold
    style.font.color.rgb=RGBColor(25,36,49)
    style.paragraph_format.space_before=Pt(15 if sname!='Heading 3' else 9)
    style.paragraph_format.space_after=Pt(9 if sname!='Heading 3' else 5)
    style.paragraph_format.keep_with_next=True
header=sec.header.paragraphs[0]; header.text='СЮЖЕТ ИКС   ·   ПОЛНОЕ РАБОЧЕЕ СОБРАНИЕ   ·   РЕЗЕРВНАЯ КОПИЯ';header.style='Caption'
footer=sec.footer.paragraphs[0]; footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
footer.add_run('Югатн  ·  ')
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)

def add_title(s,style):
    p=DOC.add_paragraph(style=style);p.add_run(s);return p

p=DOC.add_paragraph(style='Title');p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.add_run('СЮЖЕТ ИКС')
p=DOC.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER
p.add_run('Полное рабочее собрание и текстовый архив\n').bold=True
p.add_run('Югатн\n\nРезервная редакция • 3 ноября 2026 года')
DOC.add_paragraph('Составлено из GitHub-репозитория Yugatn/story-x и отдельно перенесённых рабочих материалов Notion. Включает все Markdown-исходники указанного снимка, в том числе альтернативы, черновики, документацию и исследования, разделённые по разделам. Это не окончательная последовательность романа и не утверждённый автором текст для печати.')
DOC.add_paragraph('Исключены только не-Markdown активы (например, изображения и технические файлы), которые нельзя корректно превратить в текст Word. Оригиналы, текущие имена и перечень всех вошедших исходников доступны в репозитории и приложенном JSON-реестре.')
DOC.add_paragraph('Git commit сборки: '+commit)
DOC.add_paragraph('Всего Markdown-источников: '+str(len(files))+'. Включая главы: '+str(len(groups['narrative']))+', дополнительные сюжетные материалы: '+str(len(groups['supplement']))+', импорт Notion: '+str(len(groups['notion']))+', служебные материалы: '+str(len(groups['documents']))+'.')
add_title('Оглавление', 'Heading 1')
DOC.add_paragraph('В Microsoft Word щёлкните по полю оглавления правой кнопкой мыши и выберите «Обновить поле» → «Обновить целиком». Для навигации используйте панель заголовков.')
toc_p=DOC.add_paragraph();toc_field=OxmlElement('w:fldSimple');toc_field.set(qn('w:instr'), 'TOC \\o "1-2" \\h \\z \\u');toc_p._p.append(toc_field)
DOC.add_page_break()

labels=[('narrative','Часть I. Основные пронумерованные главы и канонический пролог',
         'Порядок по порядковому номеру исходного файла GitHub; совпадения номеров и параллельные версии не удалены.'),
        ('supplement','Часть II. Дополнительные сцены, альтернативы и ненумерованные арки',
         'Потенциально перекрывающиеся сцены сохранены отдельно; их место в хронологии не утверждено.'),
        ('notion','Часть III. Новые рабочие материалы из Notion',
         'Импортированные страницы сохранены как самостоятельные материалы резервной ветки, не сливаются с уже утверждёнными главами.'),
        ('documents','Часть IV. Исследования, канон, редакционные документы и прочий архив',
         'Материалы включены для сохранности; они не являются частью художественного повествования без отдельного авторского решения.')]
manifest=[]
all_text_chars=0
def sanitise(s):
    return ''.join(c for c in s if c in '\t\n\r' or ord(c)>=32)
def add_source(p,idx):
    global all_text_chars
    rel=p.relative_to(ROOT).as_posix()
    raw=p.read_text(encoding='utf-8-sig',errors='replace')
    all_text_chars += len(raw)
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    first_head=next((re.sub(r'^#+\s*','',x).strip() for x in raw.splitlines() if re.match(r'^#{1,2}\s+',x)), None)
    title=first_head or p.stem.replace('_',' ')
    if len(title)>145: title=title[:142]+'…'
    h=add_title(title, 'Heading 2')
    if idx>1 and grouping(p)=='narrative':h.paragraph_format.page_break_before=True
    cap=DOC.add_paragraph(style='Caption');cap.add_run(rel).italic=True
    lines=raw.splitlines()
    for line in lines:
        line=sanitise(line.rstrip('\r'))
        if not line.strip(): continue
        m=re.match(r'^(#{1,6})\s+(.+)$',line)
        if m:
            par=DOC.add_paragraph(style='Heading 3');par.add_run(m.group(2));continue
        if line.strip() in ('---','***','___'):
            par=DOC.add_paragraph('•  •  •');par.alignment=WD_ALIGN_PARAGRAPH.CENTER;continue
        if line.startswith('> '):
            par=DOC.add_paragraph(style='Quote');par.add_run(line[2:]);continue
        par=DOC.add_paragraph()
        if line.startswith(('- ','* ','+ ')):
            par.paragraph_format.left_indent=Cm(0.5)
        par.add_run(line)
    manifest.append({'path':rel,'group':grouping(p),'size_bytes':p.stat().st_size,'sha256':digest,'title':title,'characters':len(raw),'lines':len(lines)})

idx=0
for key, title,subtitle in labels:
    DOC.add_page_break()
    add_title(title,'Heading 1')
    DOC.add_paragraph(subtitle)
    for p in groups[key]:
        idx+=1
        add_source(p,idx)
        if idx % 30==0: print(f'Processed {idx}/{len(files)}: {p.name}',flush=True)

DOC.core_properties.title='Сюжет Икс — полное рабочее собрание и архив'
DOC.core_properties.author='Югатн'
DOC.core_properties.subject='Резервная сборка полного текстового корпуса GitHub и рабочих материалов Notion'
DOC.save(OUTPUT)
verify=Document(OUTPUT)
bodycount=sum(len(p.text) for p in verify.paragraphs)
if len(manifest)!=len(files) or bodycount<all_text_chars*.62:
    raise RuntimeError(f'Integrity failure: files={len(manifest)}/{len(files)} body={bodycount} raw={all_text_chars}')
summary={'title':DOC.core_properties.title,'github_commit':commit,'generated_utc':datetime.now(timezone.utc).isoformat(),
 'docx_file':str(OUTPUT.name),'sources_total':len(files),'sources_by_group':{k:len(v) for k,v in groups.items()},
 'original_text_characters':all_text_chars,'docx_body_characters':bodycount,'documents':manifest}
MANIFEST.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'file':str(OUTPUT),'size_bytes':OUTPUT.stat().st_size,'sources':len(files),'original_characters':all_text_chars,'paragraphs':len(verify.paragraphs),'word_characters':bodycount},ensure_ascii=False),flush=True)
