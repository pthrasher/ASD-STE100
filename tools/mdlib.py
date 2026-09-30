"""Shared helpers for the tools that work on the transcribed markdown.

Nothing here reads the PDF: these helpers only parse markdown that was
transcribed from page images.
"""

import os
import re
import unicodedata

PAGE_MARKER = re.compile(r"<!-- page (\d+) \\?\| (.+?) -->")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def split_front_matter(text):
    """Return (front_matter_text or None, body)."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[4:end], text[end + 5:]
    return None, text


def front_matter_field(fm, key):
    if not fm:
        return None
    m = re.search(rf'^{re.escape(key)}:\s*"?(.*?)"?\s*$', fm, re.M)
    return m.group(1) if m else None


def page_markers(text):
    """List of (pdf_page:int, printed_label:str) in order of appearance."""
    return [(int(p), label.strip()) for p, label in PAGE_MARKER.findall(text)]


def pages_front_matter(markers):
    seen, pdf, printed = set(), [], []
    for p, label in markers:
        if p not in seen:
            seen.add(p)
            pdf.append(p)
            printed.append(label)
    return (
        "pages:\n"
        f"  pdf: [{', '.join(str(p) for p in pdf)}]\n"
        f"  printed: [{', '.join(yaml_str(l) for l in printed)}]\n"
    )


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def github_slug(heading):
    """GitHub's heading-anchor algorithm (without the duplicate suffix)."""
    s = heading.strip().lower()
    out = []
    for ch in s:
        cat = unicodedata.category(ch)
        if ch in " -_" or cat[0] in ("L", "N") or cat == "Mn":
            out.append(ch)
    return "".join(out).replace(" ", "-")


class Slugger:
    def __init__(self):
        self.counts = {}

    def slug(self, heading):
        base = github_slug(heading)
        n = self.counts.get(base, 0)
        self.counts[base] = n + 1
        return base if n == 0 else f"{base}-{n}"


def strip_inline_md(s):
    """Plain text of a line of inline markdown (for headings and index text)."""
    s = re.sub(r"<!--.*?-->", "", s)
    s = re.sub(r"</?u>", "", s)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = s.replace("**", "").replace("\\", "")
    s = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def md_files(root):
    for d, dirs, files in os.walk(root):
        dirs.sort()
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.join(d, f)
