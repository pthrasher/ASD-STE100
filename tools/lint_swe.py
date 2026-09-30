#!/usr/bin/env python3
"""Check the structure of the software profile (issue-9-swe/).

This checks structure only: front matter, links, rule statements against
Issue 9, and dictionary fields. It does not check if the text is STE.
Only a review can do that (issue-9-swe/review/).

Usage: tools/lint_swe.py [profile-dir] [base-issue-dir]   (default: issue-9-swe issue-9)
Exit status 1 if there are errors.
"""

import os
import re
import sys

from mdlib import (front_matter_field, link_errors, md_files, read, rule_statement,
                   split_front_matter)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, sys.argv[1] if len(sys.argv) > 1 else "issue-9-swe")
BASE = os.path.join(REPO, sys.argv[2] if len(sys.argv) > 2 else "issue-9")
RULE_FILE = re.compile(r"(rule-\d+-\d\d|gr-\d+)\.md$")
STATUS = {"unchanged", "adapted", "new"}
CHECK = {"detects", "suggests", "none"}
DECISION = {"standard", "proposed", "accepted"}
PROFILE_STATUS = {"approved", "technical verb", "technical noun", "not approved"}
TAGS = {"STE", "Non-STE", "Neutral"}

errors, warnings = [], []
err, warn = errors.append, warnings.append
relp = lambda p: os.path.relpath(p, PROFILE)
files = list(md_files(PROFILE))

# ---- front matter and example tags
for p in files:
    fm, body = split_front_matter(read(p))
    if fm is None:
        err(f"{relp(p)}: no front matter")
    fence = False
    for n, line in enumerate(body.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"\s*- \[([^\]]+)\](?!\()", line)
        if m and m.group(1) not in TAGS:
            err(f"{relp(p)}: unknown example tag [{m.group(1)}]")

# ---- rule pages
base_rules = {os.path.relpath(p, os.path.join(BASE, "part-1-writing-rules"))
              for p in md_files(os.path.join(BASE, "part-1-writing-rules")) if RULE_FILE.search(p)}
seen = set()
for p in files:
    if not RULE_FILE.search(p):
        continue
    fm, body = split_front_matter(read(p))
    rid, gr = front_matter_field(fm, "rule"), front_matter_field(fm, "gr")
    label = f"Rule {rid}" if rid else gr
    for key in ("title", "section", "topic", "inherits", "status", "mechanical-check"):
        if not front_matter_field(fm, key):
            err(f"{relp(p)}: front matter has no {key}")
    status = front_matter_field(fm, "status")
    check = front_matter_field(fm, "mechanical-check")
    if status not in STATUS:
        err(f"{relp(p)}: status '{status}' is not one of {sorted(STATUS)}")
    if check not in CHECK:
        err(f"{relp(p)}: mechanical-check '{check}' is not one of {sorted(CHECK)}")
    for part in ("## In software text", "## Examples", "## Review notes"):
        if not re.search(rf"^{re.escape(part)}\s*$", body, re.M):
            err(f"{relp(p)}: no '{part}' part")
    inherits = front_matter_field(fm, "inherits") or ""
    if inherits == "none":
        if status != "new":
            err(f"{relp(p)}: inherits none, but status is not 'new'")
        continue
    src = os.path.normpath(os.path.join(os.path.dirname(p), inherits))
    if not os.path.isfile(src):
        err(f"{relp(p)}: inherits path does not exist: {inherits}")
        continue
    seen.add(os.path.relpath(src, os.path.join(BASE, "part-1-writing-rules")))
    if inherits not in body:
        err(f"{relp(p)}: no Source link to {inherits}")
    if rid:
        mine = rule_statement(body, label)
        _, src_body = split_front_matter(read(src))
        theirs = rule_statement(src_body, label)
        if mine != theirs:
            err(f"{relp(p)}: rule statement differs from Issue 9\n    profile: {mine}\n    issue 9: {theirs}")
for missing in sorted(base_rules - seen):
    err(f"no profile page for Issue 9 {missing}")

# ---- dictionary entries
for fname in ("verbs.md", "nouns.md"):
    p = os.path.join(PROFILE, "dictionary", fname)
    if not os.path.exists(p):
        err(f"dictionary/{fname}: missing")
        continue
    heads = set()
    for block in re.split(r"^## ", read(p), flags=re.M)[1:]:
        head, _, rest = block.partition("\n")
        if head in heads:
            err(f"dictionary/{fname}: duplicate entry '{head}'")
        heads.add(head)
        if not re.match(r".+ \((v|TN|n|adj|adv)\)$", head):
            err(f"dictionary/{fname}: '{head}' has no part of speech")
        fields = dict(re.findall(r"^- ([A-Za-z0-9 ]+): (.*)$", rest, re.M))
        if fields.get("Profile status") not in PROFILE_STATUS:
            err(f"dictionary/{fname}: '{head}' has Profile status '{fields.get('Profile status')}'")
        if fields.get("Decision") not in DECISION:
            err(f"dictionary/{fname}: '{head}' has Decision '{fields.get('Decision')}'")
        if fields.get("Profile status") == "not approved" and "- Alternative:" not in rest:
            err(f"dictionary/{fname}: '{head}' is not approved but gives no Alternative")
        if fields.get("Profile status") in ("technical verb", "technical noun") and "- Meaning:" not in rest:
            err(f"dictionary/{fname}: '{head}' gives no Meaning")

# ---- links
for m in link_errors(files, relp):
    err(m)

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"{len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
