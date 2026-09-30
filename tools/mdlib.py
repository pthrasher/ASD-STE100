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


def rule_statement(body, label):
    """Plain text of the rule box (the first block quote) of a rule page, without its label."""
    box = []
    for line in body.splitlines():
        if line.startswith(">"):
            box.append(line.lstrip("> ").strip())
        elif box:
            break
    parts = []
    for b in box:
        if b.startswith("- ") and parts:
            sep = " " if strip_inline_md(parts[-1]).endswith(":") else "; "
            parts[-1] += sep + b[2:]
        else:
            parts.append(b)
    statement = strip_inline_md(" ".join(parts))
    return re.sub(rf"^{re.escape(label)}\s*", "", statement)


def heading_anchors(path, _cache={}):
    """The GitHub anchors of the headings in a markdown file (code fences ignored)."""
    if path not in _cache:
        s, out, fence = Slugger(), set(), False
        for line in read(path).splitlines():
            if line.lstrip().startswith("```"):
                fence = not fence
            m = None if fence else re.match(r"(#{1,6}) (.*)", line)
            if m:
                out.add(s.slug(strip_inline_md(m.group(2))))
        _cache[path] = out
    return _cache[path]


def link_errors(files, relp):
    """Messages for relative markdown links whose file or anchor does not exist."""
    out = []
    for p in files:
        text = re.sub(r"^(\s*)(```|~~~).*?^\1\2[^\n]*$", "", read(p), flags=re.M | re.S)
        text = re.sub(r"(`+)[^`\n]*?\1", "", text)
        for m in re.finditer(r"\]\(([^)\s]+)\)", text):
            target = m.group(1)
            if re.match(r"[a-z]+:", target):
                continue
            file_part, _, frag = target.partition("#")
            dest = os.path.normpath(os.path.join(os.path.dirname(p), file_part)) if file_part else p
            if not os.path.exists(dest):
                out.append(f"{relp(p)}: broken link {target}")
            elif frag and dest.endswith(".md") and frag not in heading_anchors(dest):
                out.append(f"{relp(p)}: missing anchor {target}")
    return out
