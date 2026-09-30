#!/usr/bin/env python3
"""Build navigation, indexes and cross-reference links from the transcribed markdown.

The input is only the markdown under issue-N/, never the PDF. The script is
idempotent: generated blocks are delimited by HTML comments and are replaced
on each run.

It does four things:
  - fills the rule-link blocks in the section READMEs and the index blocks in
    the part READMEs
  - generates part-2-dictionary/index.md and page-map.md
  - turns references such as "rule 1.5", "GR-3" and "section 9" into relative
    links, and links the rule column of the Subject-to-rule index

Usage: tools/build_indexes.py [issue-dir]   (default: issue-9)
"""

import os
import re
import sys

from mdlib import (Slugger, front_matter_field, md_files, page_markers, read, rule_statement,
                   split_front_matter, strip_inline_md, write)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISSUE = sys.argv[1] if len(sys.argv) > 1 else "issue-9"
ROOT = os.path.join(REPO, ISSUE)
P1 = os.path.join(ROOT, "part-1-writing-rules")
P2 = os.path.join(ROOT, "part-2-dictionary")
TOTAL_PAGES = 434


def rel(frm_file, to_path):
    return os.path.relpath(to_path, os.path.dirname(frm_file))


def norm(s):
    return re.sub(r"\s+", " ", strip_inline_md(s)).strip().casefold()


def replace_block(text, name, content):
    """Replace <!-- name:start -->…<!-- name:end -->, or insert it at a <!-- name --> placeholder."""
    block = f"<!-- {name}:start -->\n{content.strip()}\n<!-- {name}:end -->"
    pat = re.compile(rf"<!-- {name}:start -->.*?<!-- {name}:end -->", re.S)
    if pat.search(text):
        return pat.sub(lambda _: block, text, count=1)
    return text.replace(f"<!-- {name} -->", block, 1)


# ---------------------------------------------------------------- rules
def load_rules():
    rules = []
    for path in md_files(P1):
        name = os.path.basename(path)
        if not re.match(r"(rule-\d-\d\d|gr-\d)\.md$", name):
            continue
        fm, body = split_front_matter(read(path))
        rid = front_matter_field(fm, "rule")
        gr = front_matter_field(fm, "gr")
        label = f"Rule {rid}" if rid else gr
        key = tuple(int(x) for x in re.findall(r"\d+", rid)) if rid else (9, 100 + int(re.findall(r"\d+", gr)[0]))
        statement = rule_statement(body, label)
        rules.append(dict(path=path, id=rid or gr, label=label, key=key, statement=statement,
                          topic=front_matter_field(fm, "topic") or ""))
    return sorted(rules, key=lambda r: r["key"])


def fill_section_readmes(rules):
    unassigned = {r["path"] for r in rules}
    for readme in md_files(P1):
        if os.path.basename(readme) != "README.md" or readme == os.path.join(P1, "README.md"):
            continue
        text = read(readme)
        here = [r for r in rules if os.path.dirname(r["path"]) == os.path.dirname(readme)]
        out, heading = [], None
        lines = text.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i]
            m = re.match(r"#{1,6} (.*)", line)
            if m:
                heading = norm(m.group(1))
            if line.strip() in ("<!-- rules -->", "<!-- rules:start -->"):
                if line.strip() == "<!-- rules:start -->":
                    while i < len(lines) and lines[i].strip() != "<!-- rules:end -->":
                        i += 1
                matched = [r for r in here if norm(r["topic"]) == heading]
                links = "\n".join(f"- [{r['label']}]({rel(readme, r['path'])})" for r in matched)
                out.append("<!-- rules:start -->\n" + (links or "<!-- no rules matched this topic -->") + "\n<!-- rules:end -->")
                unassigned -= {r["path"] for r in matched}
            else:
                out.append(line)
            i += 1
        write(readme, "\n".join(out))
    for p in sorted(unassigned):
        print(f"WARNING: rule not linked from any topic heading: {os.path.relpath(p, REPO)}")


def section_dirs():
    return sorted(d for d in os.listdir(P1) if d.startswith("section-"))


def part1_index(rules):
    readme = os.path.join(P1, "README.md")
    out = ["## Sections and rules", ""]
    for d in section_dirs():
        sreadme = os.path.join(P1, d, "README.md")
        title = next((strip_inline_md(l[2:]) for l in read(sreadme).splitlines() if l.startswith("# ")), d)
        out.append(f"### [{title}]({d}/README.md)")
        out.append("")
        for r in rules:
            if r["path"].startswith(os.path.join(P1, d) + os.sep):
                out.append(f"- [{r['label']}]({rel(readme, r['path'])}) — {r['statement']}")
        out.append("")
    write(readme, replace_block(read(readme), "index", "\n".join(out)))


# ---------------------------------------------------------------- dictionary
def load_dictionary():
    entries = []
    words = os.path.join(P2, "words")
    for fname in sorted(os.listdir(words)):
        path = os.path.join(words, fname)
        slugger = Slugger()
        cur = None
        for line in read(path).splitlines():
            if line.startswith("# "):
                slugger.slug(line[2:])
            elif line.startswith("## "):
                head = line[3:].strip()
                cur = dict(file=fname, head=head, anchor=slugger.slug(strip_inline_md(head)), status="", alts=[])
                entries.append(cur)
            elif cur and line.startswith("- Status:"):
                cur["status"] = line.split(":", 1)[1].strip()
            elif cur and line.startswith("- Alternative:"):
                cur["alts"].append(line.split(":", 1)[1].strip())
    return entries


def dictionary_index(entries):
    approved = sum(e["status"] == "approved" for e in entries)
    lines = [
        "---", 'title: "Dictionary index"', "generated: true", "---", "",
        "# Dictionary index", "",
        "Every dictionary headword, with its status and its approved alternatives. "
        "The Word column links to the full entry. The markdown entries were transcribed from the page images; this index was generated from those entries.", "",
        f"- Headwords: {len(entries)}",
        f"- Approved (UPPERCASE): {approved}",
        f"- Not approved (lowercase): {len(entries) - approved}", "",
        "| Word | Status | Approved alternatives |",
        "|---|---|---|",
    ]
    for e in entries:
        word = e["head"].replace("|", "\\|")
        alts = "; ".join(a.replace("|", "\\|") for a in e["alts"])
        lines.append(f"| [{word}](words/{e['file']}#{e['anchor']}) | {e['status']} | {alts} |")
    write(os.path.join(P2, "index.md"), "\n".join(lines) + "\n")


def part2_index():
    readme = os.path.join(P2, "README.md")
    words = sorted(os.listdir(os.path.join(P2, "words")))
    intro = [("general.md", "General"), ("guide-to-the-dictionary.md", "Guide to the dictionary"),
             ("how-to-select-words.md", "How to select words correctly"),
             ("recurring-errors.md", "List of recurring errors"), ("approved-verbs.md", "List of approved verbs")]
    out = ["## How to look up a word", "",
           "- Quick lookup: [index.md](index.md) lists every headword with its status and alternatives. It is one file, so you can search all of it at once.",
           "- Full entries: `words/<letter>.md`. Each headword is a `## WORD (pos)` heading. UPPERCASE means approved; lowercase means not approved.",
           "", "## Introduction", ""]
    out += [f"- [{t}](introduction/{f})" for f, t in intro]
    out += ["", "## Words", "", " · ".join(f"[{w[:-3].upper()}](words/{w})" for w in words)]
    write(readme, replace_block(read(readme), "index", "\n".join(out)))


# ---------------------------------------------------------------- page map
def page_map():
    pages = {}
    for path in md_files(ROOT):
        if os.path.basename(path) in ("CONVENTIONS.md", "page-map.md"):
            continue
        for p, label in page_markers(read(path)):
            entry = pages.setdefault(p, [label, []])
            r = os.path.relpath(path, ROOT)
            if r not in entry[1]:
                entry[1].append(r)
    lines = ["---", 'title: "Page map"', "generated: true", "---", "", "# Page map", "",
             "Each PDF page with its printed page label and the markdown file(s) that hold its content. "
             "Pages not listed hold only \"Blank Page\".", "",
             "| PDF page | Printed label | File(s) |", "|---|---|---|"]
    for p in sorted(pages):
        label, files = pages[p]
        lines.append(f"| {p} | {label} | " + "<br>".join(f"[{f}]({f})" for f in files) + " |")
    blank = [p for p in range(1, TOTAL_PAGES + 1) if p not in pages]
    lines += ["", f"Pages with no content: {', '.join(map(str, blank))}"]
    write(os.path.join(ROOT, "page-map.md"), "\n".join(lines) + "\n")


# ---------------------------------------------------------------- cross-references
def link_targets(rules):
    t = {}
    for r in rules:
        t[r["id"]] = r["path"]
    for d in section_dirs():
        n = re.match(r"section-(\d)", d).group(1)
        t[f"section {n}"] = os.path.join(P1, d, "README.md")
    return t


LINK_SPAN = re.compile(r"\[[^\]]*\]\([^)]*\)|<!--.*?-->|<[^>]+>|`[^`]*`")
RULE_SEQ = re.compile(r"\b([Rr]ules?)\s+(\d\.\d{1,2}(?:(?:,\s*|\s+and\s+|\s+or\s+|\s+thru\s+|\s+to\s+)\d\.\d{1,2})*)")
NUM = re.compile(r"\d\.\d{1,2}")
GR = re.compile(r"\bGR-(\d)\b")
SECTION = re.compile(r"\b([Ss]ection)\s+(\d)\b(?![.\d])")


def link_line(line, path, targets):
    protected = [m.span() for m in LINK_SPAN.finditer(line)]
    edits = []  # (start, end, replacement)

    def free(a, b):
        return all(b <= s or a >= e for s, e in protected + [(x, y) for x, y, _ in edits])

    def add(a, b, text, key):
        target = targets.get(key)
        if target and os.path.abspath(target) != os.path.abspath(path) and free(a, b):
            edits.append((a, b, f"[{text}]({rel(path, target)})"))

    for m in RULE_SEQ.finditer(line):
        base = m.start(2)
        for n in NUM.finditer(m.group(2)):
            add(base + n.start(), base + n.end(), n.group(0), n.group(0))
    for m in GR.finditer(line):
        add(m.start(), m.end(), m.group(0), m.group(0))
    for m in SECTION.finditer(line):
        add(m.start(), m.end(), m.group(0), f"section {m.group(2)}")
    for a, b, rep in sorted(edits, reverse=True):
        line = line[:a] + rep + line[b:]
    return line


def link_sri_line(line, path, targets):
    """Subject-to-rule index: link the bare rule numbers in the last table cell."""
    if not line.startswith("|") or line.startswith("|---"):
        return line
    cells = line.split("|")
    if len(cells) < 4:
        return line
    cell = cells[-2]
    if "](" in cell:
        return line

    def sub(m):
        tok = m.group(0)
        if tok.endswith("#"):
            key = f"section {tok[0]}"
        else:
            key = tok
        target = targets.get(key)
        return f"[{tok}]({rel(path, target)})" if target else tok

    cells[-2] = re.sub(r"GR-\d|\b\d\.\d{1,2}\b|\b\d#", sub, cell)
    return "|".join(cells)


def link_cross_references(rules):
    targets = link_targets(rules)
    skip = {"CONVENTIONS.md", "page-map.md", "index.md"}
    for path in md_files(ROOT):
        if os.path.basename(path) in skip:
            continue
        fm, body = split_front_matter(read(path))
        out, fence = [], False
        is_sri = os.path.basename(path) == "subject-to-rule-index.md"
        for line in body.split("\n"):
            if line.lstrip().startswith("```"):
                fence = not fence
            elif not fence and not line.startswith("#"):
                line = link_sri_line(line, path, targets) if is_sri else line
                line = link_line(line, path, targets)
            out.append(line)
        text = ("---\n" + fm + "\n---\n" if fm is not None else "") + "\n".join(out)
        if text != read(path):
            write(path, text)


if __name__ == "__main__":
    rules = load_rules()
    print(f"rules/GRs: {len(rules)}")
    fill_section_readmes(rules)
    part1_index(rules)
    entries = load_dictionary()
    print(f"dictionary headwords: {len(entries)}")
    dictionary_index(entries)
    part2_index()
    link_cross_references(rules)
    page_map()
