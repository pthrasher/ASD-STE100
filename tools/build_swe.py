#!/usr/bin/env python3
"""Build the generated parts of the software profile (issue-9-swe/).

This reads only markdown: the profile pages and the Issue 9 transcription.
It fills the <!-- index:start -->…<!-- index:end --> blocks and writes
dictionary/index.md. Run it after a change to a rule page or a dictionary entry.

Usage: tools/build_swe.py [profile-dir] [base-issue-dir]   (default: issue-9-swe issue-9)
"""

import os
import re
import sys

from mdlib import (Slugger, front_matter_field, md_files, read, rule_statement,
                   split_front_matter, strip_inline_md, write)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, sys.argv[1] if len(sys.argv) > 1 else "issue-9-swe")
BASE = os.path.join(REPO, sys.argv[2] if len(sys.argv) > 2 else "issue-9")
RULES = os.path.join(PROFILE, "rules")
DICT = os.path.join(PROFILE, "dictionary")
RULE_FILE = re.compile(r"(rule-\d+-\d\d|gr-\d+)\.md$")


def rel(frm_file, to_path):
    return os.path.relpath(to_path, os.path.dirname(frm_file))


def replace_block(text, name, content):
    block = f"<!-- {name}:start -->\n{content.strip()}\n<!-- {name}:end -->"
    pat = re.compile(rf"<!-- {name}:start -->.*?<!-- {name}:end -->", re.S)
    if not pat.search(text):
        raise SystemExit(f"no <!-- {name}:start --> block")
    return pat.sub(lambda _: block, text, count=1)


def fill(path, content, name="index"):
    if not os.path.exists(path):
        print(f"WARNING: missing {os.path.relpath(path, REPO)}")
        return
    text = read(path)
    new = replace_block(text, name, content)
    if new != text:
        write(path, new)


def cell(s):
    return s.replace("|", "\\|")


# ---------------------------------------------------------------- rules
def load_rules():
    rules = []
    for path in md_files(RULES):
        if not RULE_FILE.search(path):
            continue
        fm, body = split_front_matter(read(path))
        rid, gr = front_matter_field(fm, "rule"), front_matter_field(fm, "gr")
        label = f"Rule {rid}" if rid else gr
        if rid:
            key = tuple(int(x) for x in rid.split("."))
        else:
            key = (9, 100 + int(re.findall(r"\d+", gr)[0]))
        if rid:
            statement = rule_statement(body, label)
        else:
            statement = strip_inline_md(front_matter_field(fm, "title") or gr)
            statement = re.sub(rf"^{re.escape(gr)}\s*", "", statement)
        inherits = front_matter_field(fm, "inherits") or "none"
        rules.append(dict(
            path=path, label=label, key=key, statement=statement,
            topic=front_matter_field(fm, "topic") or "",
            status=front_matter_field(fm, "status") or "?",
            check=front_matter_field(fm, "mechanical-check") or "?",
            source=None if inherits == "none" else os.path.normpath(os.path.join(os.path.dirname(path), inherits)),
        ))
    return sorted(rules, key=lambda r: r["key"])


def title_of(readme):
    return next((strip_inline_md(l[2:]) for l in read(readme).splitlines() if l.startswith("# ")),
                os.path.basename(os.path.dirname(readme)))


def section_dirs():
    dirs = [d for d in os.listdir(RULES) if d.startswith("section-")]
    return sorted(dirs, key=lambda d: int(re.search(r"\d+", d).group()))


def fill_section_readmes(rules):
    for d, _, files in os.walk(RULES):
        if d == RULES or "README.md" not in files:
            continue
        readme = os.path.join(d, "README.md")
        here = [r for r in rules if os.path.dirname(r["path"]) == d]
        lines = ["## Rules", "", "| Rule | Statement | Status | Mechanical check |", "|---|---|---|---|"]
        lines += [f"| [{r['label']}]({rel(readme, r['path'])}) | {cell(r['statement'])} | {r['status']} | {r['check']} |"
                  for r in here]
        subs = sorted(x for x in os.listdir(d) if os.path.isfile(os.path.join(d, x, "README.md")))
        for s in subs:
            lines += ["", f"Also in this section: [{title_of(os.path.join(d, s, 'README.md'))}]({s}/README.md)"]
        fill(readme, "\n".join(lines))


def rules_index(rules):
    readme = os.path.join(RULES, "README.md")
    out = []
    for d in section_dirs():
        sreadme = os.path.join(RULES, d, "README.md")
        title = title_of(sreadme) if os.path.exists(sreadme) else d
        out += [f"### [{title}]({d}/README.md)", "",
                "| Rule | Statement | Status | Mechanical check | Issue 9 |", "|---|---|---|---|---|"]
        for r in rules:
            if r["path"].startswith(os.path.join(RULES, d) + os.sep):
                src = f"[source]({rel(readme, r['source'])})" if r["source"] else "new"
                out.append(f"| [{r['label']}]({rel(readme, r['path'])}) | {cell(r['statement'])} | "
                           f"{r['status']} | {r['check']} | {src} |")
        out.append("")
    fill(readme, "\n".join(out))


def limits_table(rules):
    path = os.path.join(PROFILE, "review", "LIMITS.md")
    out = []
    for value, meaning in (("detects", "A check can find all text with the pattern. A person finds if each result is an error."),
                           ("suggests", "A check can show possible problems. It misses some, and it shows some correct text."),
                           ("none", "Only a person or an agent who reads the text can use the rule.")):
        here = [r for r in rules if r["check"] == value]
        out += [f"### `{value}` ({len(here)})", "", meaning, ""]
        out += [", ".join(f"[{r['label'].replace('Rule ', '')}]({rel(path, r['path'])})" for r in here) or "None.", ""]
    fill(path, "\n".join(out))


def quick_reference(rules):
    path = os.path.join(PROFILE, "QUICK-REFERENCE.md")
    out, current = [], None
    for r in rules:
        d = os.path.relpath(r["path"], RULES).split(os.sep)[0]
        if d != current:
            current = d
            out += ["", f"**{title_of(os.path.join(RULES, d, 'README.md'))}**", ""]
        out.append(f"- [{r['label'].replace('Rule ', '')}]({rel(path, r['path'])}) {r['statement']}")
    fill(path, "\n".join(out).strip())


# ---------------------------------------------------------------- dictionary
def parse_entries(path, fields):
    """Entries under '## head' headings, with the '- Field: value' lines named in fields."""
    entries, cur, slugger = [], None, Slugger()
    for line in read(path).splitlines():
        if line.startswith("# "):
            slugger.slug(strip_inline_md(line[2:]))
        elif line.startswith("## "):
            head = line[3:].strip()
            cur = dict(head=head, anchor=slugger.slug(strip_inline_md(head)), alts=[])
            entries.append(cur)
        elif cur:
            m = re.match(r"- ([A-Za-z0-9 ]+): (.*)", line)
            if m and m.group(1) in fields:
                if m.group(1) == "Alternative":
                    cur["alts"].append(m.group(2).strip())
                else:
                    cur.setdefault(m.group(1), m.group(2).strip())
    return entries


def key_of(head):
    head = re.sub(r"<!--.*?-->", "", head)
    m = re.match(r"(.+?) \(([^)]*)\)", strip_inline_md(head))
    word, pos = (m.group(1), m.group(2)) if m else (strip_inline_md(head), "")
    return word.strip().casefold(), pos.strip().casefold()


def dictionary_index():
    words_dir = os.path.join(BASE, "part-2-dictionary", "words")
    rows = {}
    for fname in sorted(os.listdir(words_dir)):
        path = os.path.join(words_dir, fname)
        for e in parse_entries(path, ("Status", "Alternative")):
            rows.setdefault(key_of(e["head"]), {})["base"] = (e, path)
    counts = {}
    for fname in ("verbs.md", "nouns.md"):
        path = os.path.join(DICT, fname)
        if not os.path.exists(path):
            continue
        for e in parse_entries(path, ("Profile status", "Decision", "Limit")):
            rows.setdefault(key_of(e["head"]), {})["profile"] = (e, path)
            counts[e.get("Decision", "?")] = counts.get(e.get("Decision", "?"), 0) + 1
    out_path = os.path.join(DICT, "index.md")
    n_profile = sum(counts.values())
    lines = [
        "---", 'title: "Dictionary index"', "generated: true", "---", "",
        "# Dictionary index", "",
        "All headwords of the Issue 9 dictionary and of this profile, in one table. "
        "`tools/build_swe.py` makes this file. Do not change it.", "",
        "- If the Profile column has a value, use the profile entry, not the Issue 9 entry.",
        "- If the Profile column is empty, the Issue 9 entry is applicable without a change.",
        "- In the Issue 9 columns, UPPERCASE is approved and lowercase is not approved.", "",
        f"Profile entries: {n_profile} ("
        + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())) + ").", "",
        "| Word | Issue 9 status | Issue 9 alternatives | Profile |",
        "|---|---|---|---|",
    ]
    for key in sorted(rows, key=lambda k: (k[0].lstrip("-"), k[1])):
        r = rows[key]
        if "base" in r:
            e, path = r["base"]
            word = f"[{cell(strip_inline_md(e['head']))}]({rel(out_path, path)}#{e['anchor']})"
            status, alts = e.get("Status", ""), cell("; ".join(e["alts"]))
        else:
            e, path = r["profile"]
            word, status, alts = cell(e["head"]), "not in Issue 9", ""
        prof = ""
        if "profile" in r:
            pe, ppath = r["profile"]
            text = pe.get("Profile status", "?")
            if pe.get("Limit"):
                text += f" ({pe['Limit']})"
            prof = f"[{cell(text)}, {pe.get('Decision', '?')}]({rel(out_path, ppath)}#{pe['anchor']})"
        lines.append(f"| {word} | {status} | {alts} | {prof} |")
    write(out_path, "\n".join(lines) + "\n")
    return n_profile


if __name__ == "__main__":
    rules = load_rules()
    print(f"rule pages: {len(rules)}")
    fill_section_readmes(rules)
    rules_index(rules)
    limits_table(rules)
    quick_reference(rules)
    print(f"profile dictionary entries: {dictionary_index()}")
