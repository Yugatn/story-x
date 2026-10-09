#!/usr/bin/env python3
"""Scan Story X text files for common accidental assistant/tool artifacts.

Run from repository root:
    python3 scripts/audit_text_artifacts.py
This script reports matches with file, line number and category. It does not
modify files; review each match before deciding whether it is a real artifact.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".txt", ".html", ".htm", ".json", ".yaml", ".yml"}

PATTERNS = {
    "ChatGPT citation marker": re.compile(r"cite[^]*|\bturn\d+(?:search|news|image|fetch|view)\d+\b"),
    "Sandbox path": re.compile(r"sandbox:/mnt/data/\S+"),
    "Template placeholder": re.compile(r"\b(?:TODO|FIXME|PLACEHOLDER|INSERT HERE|Lorem ipsum)\b", re.I),
    "Assistant boilerplate": re.compile(r"\b(?:As an AI language model|Here is the revised version|Certainly!|Sure, here(?:'s| is))\b", re.I),
    "Unrendered HTML": re.compile(r"</?(?:div|span|br|p|strong|em)\b[^>]*>", re.I),
    "Replacement character": re.compile("�"),
}

def main() -> int:
    findings = 0
    files = sorted(p for p in ROOT.rglob("*")
                   if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES
                   and ".git" not in p.parts)
    for path in files:
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for line_number, line in enumerate(lines, 1):
            for category, pattern in PATTERNS.items():
                for match in pattern.finditer(line):
                    print(f"{path.relative_to(ROOT)}:{line_number}: [{category}] {match.group(0)}")
                    findings += 1
    print(f"\nScanned {len(files)} text files; found {findings} candidate artifact(s).")
    print("Matches are candidates for manual review, not automatic proof of an error.")
    return 1 if findings else 0

if __name__ == "__main__":
    sys.exit(main())
