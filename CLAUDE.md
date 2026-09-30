# ASD-STE100 markdown transcriptions

This repo turns ASD-STE100 Simplified Technical English PDFs (in `original_pdfs/`) into markdown hierarchies that are easy to discover step by step and easy to search. Each issue gets its own folder (`issue-9/`), and `latest` is a symlink to the newest one.

## Hard rules
- **Never convert PDF to markdown with a script or tool.** That means no pdftotext, pandoc, pdfplumber or similar in the transcription path. Transcription is done by agents that read rendered page images. Text extraction may be used only for rough orientation during exploration, and it must not be trusted.
- Render pages with `tools/render_pages.swift` (macOS PDFKit). **Do not use poppler** (`pdftoppm`/`pdftocairo`): the PDFs reference non-embedded fonts, and poppler renders bold as regular weight.
- Page images are **not** committed. They live in `.work/` (gitignored).
- `issue-N/CONVENTIONS.md` is the specification for how each visual element is written in markdown. Transcription and verification follow it exactly.
- Transcribe what is printed. Never correct the source: mark errors with `<!-- sic -->` and uncertain readings with `<!-- unclear: … -->`.
- Letter case in the dictionary and in the Highlights carries meaning: UPPERCASE = approved, lowercase = not approved. Never change it.

## Tools
- `tools/render_pages.swift`: renders pages to JPEG. Build with `swiftc -O tools/render_pages.swift -o .work/render_pages`.
- `tools/assemble.py`: joins fragments that several agents transcribed (`.work/<issue>/parts/`) into their final files.
- `tools/build_indexes.py`: builds the indexes and navigation **from the transcribed markdown**, never from the PDF.
- `tools/lint.py`: checks structure and coverage of the transcribed markdown.

## Process for a new issue
1. Render every page to `.work/issue-N/pages/` at 140 dpi, plus top and bottom crops at 220 dpi.
2. Adapt `CONVENTIONS.md` to the new issue, then pilot a few difficult pages.
3. For each unit of pages: a transcriber agent, then an independent verifier agent. Both read only the images.
4. Run `tools/assemble.py`, then `tools/build_indexes.py`, then `tools/lint.py`. Spot-check pages against the images.
