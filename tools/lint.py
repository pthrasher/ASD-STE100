#!/usr/bin/env python3
"""Check the structure and coverage of a transcribed issue.

This reads only the transcribed markdown. It never reads the PDF.

Usage: tools/lint.py [issue-dir] [--blank 30,44,...]
Exit status 1 if there are errors. Warnings are printed but do not fail.
"""

import os
import re
import sys
from collections import Counter

from mdlib import (link_errors, md_files, page_markers, read, split_front_matter,
                   strip_inline_md)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
ISSUE = args[0] if args else "issue-9"
ROOT = os.path.join(REPO, ISSUE)
TOTAL_PAGES = 434
# Pages that print only "Blank Page" (confirmed from the page images).
BLANK = {30, 44, 62, 76, 86, 94, 102, 128, 130, 148, 226, 274, 292, 294, 328, 348, 366, 412, 432, 434}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


files = [p for p in md_files(ROOT) if os.path.basename(p) != "CONVENTIONS.md"]
relp = lambda p: os.path.relpath(p, ROOT)

# ---- front matter and leftovers
for p in files:
    text = read(p)
    fm, body = split_front_matter(text)
    if fm is None and os.path.basename(p) != "CONVENTIONS.md":
        err(f"{relp(p)}: no front matter")
    if "<!-- rules -->" in body:
        err(f"{relp(p)}: unfilled <!-- rules --> placeholder")
    for m in re.finditer(r"<!-- unclear:(.*?)-->", body):
        warn(f"{relp(p)}: unclear:{m.group(1)}")
    if os.path.basename(p) != "CONVENTIONS.md":
        for m in re.finditer(r"^\s*- \[([^\]]+)\](?!\()", body, re.M):
            if m.group(1) not in ("STE", "Non-STE", "Neutral"):
                err(f"{relp(p)}: unknown band tag [{m.group(1)}]")

# ---- page coverage
where = {}
for p in files:
    if os.path.basename(p) in ("page-map.md", "CONVENTIONS.md"):
        continue
    for page, label in page_markers(read(p)):
        where.setdefault(page, set()).add(relp(p))
        if not 1 <= page <= TOTAL_PAGES:
            err(f"{relp(p)}: page marker out of range: {page}")
missing = [n for n in range(1, TOTAL_PAGES + 1) if n not in where and n not in BLANK]
if missing:
    err(f"pages with content but no page marker: {missing}")
blank_marked = sorted(n for n in BLANK if n in where)
if blank_marked:
    warn(f"pages listed as blank but marked in files: {blank_marked}")

# ---- rules
rule_files = [p for p in files if re.search(r"/rule-\d-\d\d\.md$", p)]
gr_files = [p for p in files if re.search(r"/gr-\d\.md$", p)]
if len(rule_files) != 53:
    err(f"expected 53 rule files, found {len(rule_files)}")
if len(gr_files) != 8:
    err(f"expected 8 GR files, found {len(gr_files)}")
for p in rule_files:
    fm, body = split_front_matter(read(p))
    num = re.search(r"rule-(\d)-(\d\d)", p)
    rid = f"{num.group(1)}.{int(num.group(2))}"
    if f'rule: "{rid}"' not in (fm or ""):
        err(f"{relp(p)}: front matter rule is not \"{rid}\"")
    if not re.search(rf"^# Rule {re.escape(rid)}\s*$", body, re.M):
        err(f"{relp(p)}: missing '# Rule {rid}' heading")
    if not re.search(rf"^> \*\*Rule {re.escape(rid)}\*\*", body, re.M):
        err(f"{relp(p)}: missing rule box '> **Rule {rid}**'")

# ---- dictionary
words = os.path.join(ROOT, "part-2-dictionary", "words")
status_count = Counter()
if os.path.isdir(words):
    for fname in sorted(os.listdir(words)):
        p = os.path.join(words, fname)
        lines = read(p).splitlines()
        heads = Counter()
        for i, line in enumerate(lines):
            if not line.startswith("## "):
                continue
            head = line[3:].strip()
            heads[head] += 1
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            m = re.match(r"- Status: (approved|not approved)$", nxt)
            if not m:
                err(f"words/{fname}: '{head}' is not followed by a valid '- Status:' line")
                continue
            status_count[m.group(1)] += 1
            word = re.sub(r"\([^)]*\)", "", strip_inline_md(head))
            letters = [c for c in word if c.isalpha()]
            upper = letters and all(c.isupper() for c in letters)
            lower = letters and any(c.islower() for c in letters)
            if (m.group(1) == "approved") != bool(upper) or (m.group(1) == "not approved") != bool(lower):
                warn(f"words/{fname}: status '{m.group(1)}' disagrees with the case of '{head}'")
        for h, n in heads.items():
            if n > 1:
                warn(f"words/{fname}: duplicate heading '{h}' ×{n}")
    print(f"dictionary: {sum(status_count.values())} headwords "
          f"({status_count['approved']} approved, {status_count['not approved']} not approved); "
          f"the book states 875 approved / 1274 not approved words")

# ---- links
for m in link_errors(files, relp):
    err(m)

latest = os.path.join(REPO, "latest")
if not (os.path.islink(latest) and os.path.isfile(os.path.join(latest, "README.md"))):
    err("latest is not a symlink to a folder with a README.md")

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"{len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
