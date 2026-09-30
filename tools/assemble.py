#!/usr/bin/env python3
"""Assemble transcription fragments (.work/<issue>/parts/) into their final files.

Some files were transcribed by more than one agent, e.g. a dictionary letter
split into page ranges. Each agent wrote a fragment with page markers and
content only. This script concatenates the fragments in page order, and adds
front matter and a title. It works on transcribed markdown only.

Usage: tools/assemble.py [issue-dir]   (default: issue-9)
"""

import glob
import os
import sys

from mdlib import (page_markers, pages_front_matter, read, split_front_matter,
                   write, yaml_str)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISSUE = sys.argv[1] if len(sys.argv) > 1 else "issue-9"
OUT = os.path.join(REPO, ISSUE)
PARTS = os.path.join(REPO, ".work", ISSUE, "parts")


def join_fragments(paths):
    return "\n\n".join(read(p).strip("\n") for p in paths) + "\n"


def first_page(path):
    m = page_markers(read(path))
    return m[0][0] if m else 10**9


def emit(dest, title, body, extra_fm=""):
    fm = f"---\ntitle: {yaml_str(title)}\n{extra_fm}{pages_front_matter(page_markers(body))}---\n\n"
    write(dest, fm + body)
    print(f"wrote {os.path.relpath(dest, REPO)}")


def need(*names):
    paths = [os.path.join(PARTS, n) for n in names]
    missing = [p for p in paths if not os.path.exists(p)]
    if missing:
        sys.exit(f"missing fragments: {missing}")
    return paths


# Dictionary letters
letters = {}
for p in glob.glob(os.path.join(PARTS, "dict", "dict-*.md")):
    letters.setdefault(os.path.basename(p).split("-")[1], []).append(p)
for letter, paths in sorted(letters.items()):
    paths.sort(key=first_page)
    heading = "X, Y, Z" if letter == "xyz" else letter.upper()
    body = f"# {heading}\n\n" + join_fragments(paths)
    emit(os.path.join(OUT, "part-2-dictionary", "words", f"{letter}.md"),
         f"Dictionary – {heading}", body, f"letter: {yaml_str(heading)}\n")

# Highlights, Part 2
body = "# Highlights\n\n" + join_fragments(need("highlights-2a.md", "highlights-2b.md"))
emit(os.path.join(OUT, "front-matter", "highlights", "part-2-dictionary.md"),
     "Highlights – Part 2 – Dictionary", body)

# Guide to the dictionary
body = join_fragments(need("guide-a.md", "guide-b.md"))
emit(os.path.join(OUT, "part-2-dictionary", "introduction", "guide-to-the-dictionary.md"),
     "Guide to the dictionary", body)

# Section 1 README: append the second agent's topic headings
readme = os.path.join(OUT, "part-1-writing-rules", "section-1-words", "README.md")
extra, = need("section-1-readme-b.md")
fm, body = split_front_matter(read(readme))
if "<!-- appended: section-1-readme-b -->" not in body:
    body = body.rstrip("\n") + "\n\n<!-- appended: section-1-readme-b -->\n" + read(extra).strip("\n") + "\n"
title = next((l.split(":", 1)[1].strip().strip('"') for l in (fm or "").splitlines() if l.startswith("title:")),
             "Section 1")
emit(readme, title, body)

# Part covers become the start of each part's README
for part, frag, title in [("part-1-writing-rules", "part-1-cover.md", "Part 1 – Writing rules"),
                          ("part-2-dictionary", "part-2-cover.md", "Part 2 – Dictionary")]:
    body = read(need(frag)[0]).strip("\n") + "\n\n<!-- index:start -->\n<!-- index:end -->\n"
    emit(os.path.join(OUT, part, "README.md"), title, body)
