# Transcription conventions

This transcription of ASD-STE100 Issue 9 was made by reading the rendered page images directly. It was not produced by a text-extraction or conversion tool. This file describes how each visual element of the PDF is written in markdown. It is the specification for transcribers and a legend for readers.

**The rule above all others:** transcribe what is printed. Do not correct, modernize, normalize, complete or "improve" anything. If the source has a typo, keep the typo.

---

## 1. Files, front matter and page markers

Every file starts with YAML front matter that names its source pages:

```yaml
---
title: "Rule 1.2"
pages:
  pdf: [46, 47]              # 1-based PDF page index
  printed: ["1-1-2", "1-1-3"]  # page label printed in the footer
---
```

Rule files add three fields: `rule: "1.2"`, `section: "Section 1 – Words"` and `topic: "Part of speech"`. The topic is the blue topic heading that the rule is under. GR files use `gr: "GR-1"` in place of `rule`.

**Page markers.** Put a marker at the start of the content from each source page, including the first page of the file:

```
<!-- page 47 | 1-1-3 -->
```

- The format is `page <pdf index> | <printed label>`. If a page has no printed label (p1, p2), write `—`.
- When one page's content is split across two files, both files get a marker for that page.
- A sentence or paragraph that breaks across a page is **rejoined**. Put the marker before the paragraph where the page break falls, not in the middle of the sentence.

**Always drop:**
- the running header: the ASD logo and "ASD-STE100 Simplified Technical English" (sometimes "ASD STE100 …")
- the footer: issue, date, part name and page label (the label goes into the page marker)
- "Blank Page" pages
- the dictionary column-header row that repeats on every page

## 2. General typography

| Source | Markdown |
|---|---|
| **bold** | `**bold**` |
| *italic* | `*italic*` |
| underlined | `<u>underlined</u>`. Include any underlined trailing punctuation or space inside the tags. |
| bold + underlined | `**<u>text</u>**` |
| superscript (1st) | `1<sup>st</sup>` |
| hyperlink (blue underlined) | `[www.asd-europe.org](https://www.asd-europe.org)`, keeping the printed text |
| an image in the source | `![short alt](relative/path/to/assets/file.jpg)` plus a one-paragraph *Figure description:* in italics |

**Characters.** Copy them exactly:
- curly quotes `“ ” ‘ ’` versus straight quotes `" '`
- the ellipsis character `…` versus three dots `...` (both occur), and `….`
- the en dash `–` versus the hyphen `-`
- `°`, `Ω`, `≠`, `½`, `¼`, `″`
- accented letters (Trône, René, disposición)
- lowercase units inside UPPERCASE text (`800 kPa`, `5 mm`, `24 °C`, `No. 1`); never uppercase them

Never convert straight quotes to curly or the reverse.

**Line wrapping.**
- Join text that wraps only because the column is narrow.
- Join a word hyphenated only by a line wrap, e.g. `ELECTROMAG-` / `NETIC` becomes `ELECTROMAGNETIC`.
- Keep a real hyphen that happens to fall at a line end: `HIGH-PRESSURE`, `carbon-fiber-reinforced`.
- If you cannot tell which case it is, use the higher-resolution crops. If still unsure, keep the hyphen and add `<!-- unclear: wrap hyphen? -->`.

**Hard line breaks.** A line break inside a paragraph, cell or band that is *not* caused by the column width is kept as `<br>`. The test: if the first word of the next line would have fit on the current line, the break is hard.

**Lists in body text** (outside example bands) use markdown lists:
- `-` for printed dash items
- `*` for printed bullet (•) items
- `1.` for numbered items
- Letter or parenthesized markers (`a)`, `A.`, `(1)`) are literal text lines ending with `<br>`

A round, centered dot that appears as a character in running text is `•` (U+2022).

**Source errors.** Keep them as printed and add `<!-- sic -->` right after, e.g. `genetics, geology. geophysics <!-- sic -->`. Use this for typos, wrong punctuation, missing words and inconsistent spellings. Do not use it for deliberate errors inside Non-STE examples. A formatting-only oddity (e.g. one italic parenthesis) gets `<!-- sic: <description> -->`.

**Uncertain readings.** Never guess silently. Write your best reading followed by `<!-- unclear: <what is uncertain> -->`. The verifier resolves these.

**Markdown escaping.**
- Escape characters that markdown would read as syntax: `\*`, `\_`, `\#` at the start of a line, and `\|` inside tables.
- Escape literal list markers that are part of an example so markdown cannot renumber or re-bullet them: `1\.` and `\-` at the start of a line. `A.` and `(1)` do not need escaping.

## 3. Part 1: writing rules

### 3.1 How a section is split into files

A section folder holds a `README.md` and one file per rule (`rule-1-01.md`, …, `rule-1-14.md`). GRs go in `general-recommendations/gr-1.md`, ….

- **Section `README.md`** holds, in source order:
  - the section title, exactly as printed on the section's first page (the separator is sometimes an en dash `–` and sometimes a hyphen `-`; copy it). Use the same string in the rules' `section:` front matter.
  - the **Summary of the rules** box, verbatim (§3.3)
  - each blue topic heading (`## Part of speech`) with any prose or notes printed between that heading and the next rule box, followed by the placeholder line `<!-- rules -->`. The build tool replaces the placeholder with links to the rules whose `topic:` matches the heading. Do not write the link list yourself.
- **Rule file** holds everything from its rule box up to the next rule box or the next blue topic heading, whichever comes first. Set the rule's `topic:` front-matter field to the nearest blue topic heading above it.

### 3.2 Rule and GR boxes

A rule box is pale yellow with a dark-blue border. A GR box is mint green with the same border. Write it as an H1 heading followed by the box as a blockquote. The box text is bold:

```markdown
# Rule 1.1

> **Rule 1.1** **Use words that are:**
> - **Approved in the dictionary**
> - **Technical nouns**
> - **Technical verbs.**
```

```markdown
# GR-1 The conjunction "that"

> **GR-1** **The conjunction “that”**
```

Keep the box wording exactly, including dash lists and final punctuation.

### 3.3 Summary of the rules box

```markdown
## Summary of the rules

> **Which words can you use?**
> - Rule 1.1 Use words that are:
>   - Approved in the dictionary
>   - …
>
> **Part of speech**
> - Rule 1.2 Use approved words …
```

- The bold group labels match the topic headings.
- Follow the printed weight: the rule numbers in the Summary box are regular weight, not bold.
- Dash sub-items become a nested list.
- Transcribe the summary verbatim, because its wording sometimes differs from the rule box. Do not make them agree.

### 3.4 Headings inside a rule file

| Source | Markdown |
|---|---|
| Underlined minor heading ("Method 1", "What is passive voice?") | `## Method 1` |
| Bold numbered sub-heading (8.3 "1. Numbers", 1.5 categories "1. Official parts information") | `### 1. Numbers` |
| Bold run-in label ("Examples:", "Example:", "Examples in STE:", "General examples:") | `**Examples:**` on its own line, with the wording as printed. If the colon is printed non-bold, write `**General examples**:` |

Headings are written as plain text. The heading level already represents the underline or bold on a heading, including a heading that is only partly underlined.

Indented example lines under a label that sit on white (no band) are one paragraph, with `<br>` at the end of each printed line. The indentation is not kept.

### 3.5 Example bands (the colored backgrounds)

Examples are printed on shaded horizontal bands. The band color carries meaning. Record it with a **plain-text tag** at the start of the line, then the printed label in bold, then the example text with its own formatting (italic, underline, …):

| Band color | Tag | Typical printed labels |
|---|---|---|
| green | `[STE]` | STE:, WRITE:, CORRECT:, Active:, (no label) |
| pink / red | `[Non-STE]` | Non-STE:, Incorrect:, NOT:, Do not write: |
| peach / orange | `[Neutral]` | Do not write:, (no label), General examples, intermediate rewrites |

```markdown
- [Non-STE] **Non-STE:** *The circuits are connected by a <u>switching relay</u>.* (Passive)
- [STE] **STE:** A <u>switching relay</u> connects the circuits. (Active)
```

- **The tag records the observed color.** Most of the time the tag and the label agree. Where they do not (for example "Do not write:" on peach on one page and pink on another), the tag follows the color and the label is copied as printed.
- **A band with no printed label** gets the tag only: `- [STE] Clean the filter.`
- **The label is always written `**Label:**`**, whatever its printed style. Everything after the label keeps its printed style. Non-STE text is usually italic: keep `*…*` where it is italic, and do not add italics where it is not.
- **One bullet per band.** Bands that touch form one group; separate groups with a blank line.
- **Commentary** printed under a band on a white background, e.g. `("Clean" is a verb here.)`, goes indented under the band, preceded by a blank line:
  ```markdown
  - [STE] **STE:** Clean the filter.

    (“Clean” is a verb here.)
  ```
- **Right-aligned side notes** such as word counts go at the end of the band line after `&emsp;`: `… the valve. &emsp;(13 words)`
- **Multi-line band content** (procedure steps, lists, WARNING text with hanging indents, stacked alternatives) goes on continuation lines indented two spaces, each ending with `<br>`:
  - Keep the list markers literal and escaped.
  - Show each visible indent level relative to the band's text column as four `&nbsp;`.
  - Normalize the gap between a marker and its text (tab or space) to one space.
  - In italic bands, italicize each line's text and leave the list marker outside the `*…*`.
  ```markdown
  - [Non-STE] **Non-STE:** *Remove these parts:*<br>
    &nbsp;&nbsp;&nbsp;&nbsp;\- *The four screws (3)*<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- *The two O-rings (6)*<br>
  ```
- **An example group split by a page break:** put the page marker on its own line between the bands, with a blank line before and after it.
- **"or" between two alternatives** inside one group: write it as its own line in the group, e.g. `- or`, with a tag only if it sits on a band.
- **Safety instruction examples** (Section 7 and elsewhere) are example text, not callouts. Write them as bands: `- [STE] <u>WARNING</u>: MAKE SURE THAT …`. **Never** use GitHub `> [!WARNING]` / `> [!CAUTION]` alerts.

### 3.6 Help notes (lightbulb icon)

The navy circle with a yellow bulb is the document's **Help** symbol. Wherever it appears, write it as a blockquote with a plain label:

```markdown
> **Help:** In the context of ISO 1087:2019, “subject fields” refer to …
```

A Help block that contains a list keeps the list inside the blockquote.

### 3.7 Tables and diagrams

- Use GFM pipe tables. Use `<br>` for printed line or paragraph breaks inside a cell.
- A header row is a header row only if the source shades or styles it as one. If there is none, use the column names from the nearest printed header, because GFM requires a header.
- **A table that continues across a page break** stays one table. Put the page marker at the start of the first cell of the first row on the new page, with the pipe escaped so that it does not split the cell, e.g. `| <!-- page 32 \| SRI-2 --> Fluid names | 1.5 |`. A comment on its own line would end the table.
- A table printed inside an example band goes directly after that band's bullet line, indented.
- A diagram gets its cropped image from `assets/`, a *Figure description:* in italics, and a Mermaid version where the structure allows (the p73 voice diagram, the p144 flowchart). Mermaid may use `classDef` or `style` with `stroke-dasharray` to keep the difference between dashed and dotted lines.

## 4. Front matter

- **Highlights** is a two-column table, "Subject | Change".
  - A **band** is a full-width shaded row with an empty Change column. Each band becomes a heading:
    - `##` for top-level groups: "General changes", "Preliminary pages and general introduction", "Part 1 – Writing rules", "Part 2 – Dictionary"
    - `###` for bands inside a Part: sections, "General recommendations (GR)", "Introduction", "Word list", "Detailed changes"
  - A shaded row that has text in its Change column is an ordinary row.
  - The rows under each band go in a pipe table with the header `| Subject | Change |`.
  - Printed line or paragraph breaks inside a cell become `<br>`. Sentences printed as one paragraph stay on one line.
  - Indentation of the Subject (e.g. "Rule 1.1" under a section band) is not kept.
  - **Keep the case of dictionary headwords exactly**: case is the approved / not-approved signal.
  - A NOTE printed outside the table is a paragraph, e.g. `<u>NOTE</u>: …`.
- **Table of contents** and **Subject-to-rule index**: pipe tables with the printed columns. Keep the printed page labels and rule numbers as text. Links are added later by tooling.
- **Q&A headings** in the General introduction become `##` headings.
- **The Change form** is an empty form. Reproduce its field labels as a table with empty cells. Do not invent values.

## 5. Part 2: dictionary introduction pages

- Follow §2, §3.6 and §3.7.
- The sample tables in the Guide go in pipe tables, using the entry notation from §6 inside the cells where that is needed.
- **List of recurring errors**: one table, `| Non-STE | STE |`, merged across both pages, with the case kept exactly.
- **List of approved verbs**: a 5-column grid read down each column. Write one line per letter heading: `**A** — ABSORB, ACCEPT, …`. If a letter has no verbs, write `**J** — (none)`. Keep the order in which the verbs appear under each letter.

## 6. Part 2: dictionary entries (`part-2-dictionary/words/<letter>.md`)

The source is a four-column table: Word (part of speech) | Approved meaning / ALTERNATIVES | STE EXAMPLE | Non-STE example.

- A full-width rule separates headwords.
- A partial rule (columns 3–4, or 2–4) separates sub-rows inside one headword.
- Column-1 headwords are **always bold** in the source. The heading expresses that, so do not add `**`.

**Case is the meaning:**
- A headword in UPPERCASE is approved; in lowercase it is not approved.
- Alternatives and STE examples are UPPERCASE, except for units and abbreviations.
- Non-STE examples are in sentence case.

Never change case.

### 6.1 Entry schema

```markdown
<!-- page 150 | 2-1-A2 -->
## ABOUT (prep)
- Status: approved
- Meaning: Concerned with
  - STE: FOR DATA ABOUT THE LOCATION OF CIRCUIT BREAKERS, REFER TO THE WIRING LIST.
- Help: For other meanings, use:
- Alternative: APPROXIMATELY (adv)
  - STE: DRAIN APPROXIMATELY 2 LITERS OF FUEL FROM THE TANK.
  - Non-STE: Drain about 2 liters of fuel from the tank.
- Alternative: AROUND (prep)
  - STE: TURN THE SHAFT AROUND ITS AXIS.
  - Non-STE: Rotate the shaft about its axis.
```

The fields always appear **in source row order**:

| Field | Source | Notes |
|---|---|---|
| `## <headword>` | Column 1 headword and its part-of-speech tag, **exactly as printed**, joined onto one line | `## abandon (v)`, `## little (a little) (adj)`, `## FOR EXAMPLE`, `## re- (prefix)`, `## process (in the process of ) (prep)`. Do not put verb or adjective forms in the heading. |
| `- Status:` | derived from the headword's case | `approved` or `not approved` |
| `- Forms:` | the remaining text in column 1 after the headword and part of speech, joined onto one line with the printed punctuation. The comma printed directly after the part of speech (`CHANGE (v),`) is dropped. | `CHANGES, CHANGED, CHANGED` / `IS, WAS, (also ARE, WERE)` / `(LARGER, LARGEST)` / `DRINKS, DRANK,` / `PROTRUDES PROTRUDED PROTRUDED`. Omit if there are none. |
| `- Help (word column):` | lightbulb note in column 1 | e.g. `No other verb forms.` |
| `- Meaning:` | a definition in column 2 (approved words) | Keep the printed numbering: `- Meaning: 1. To occur, exist`. Nested senses go one level deeper: `  - Meaning: a. …` |
| `- Alternative:` | an UPPERCASE alternative in column 2 (not-approved words, or after "For other meanings, use:") | As printed, with the part of speech, `(TN)`/`(TV)`, ellipses and bracketed qualifiers: `REMOVE (v) (WITH A DRIFT [TN])`, `LET …. STAY (v)`, `NOT SUFFICIENT` |
| `- Help:` | lightbulb note in column 2 | See placement rules below. |
| `  - STE:` | column 3, indented under the Meaning, Alternative or Help it belongs to | One line per example sub-row. |
| `  - Non-STE:` | column 4 | Directly after the STE line of the same sub-row. |

**Placement rules:**
- **Several STE examples for one meaning or alternative** (separate sub-rows with an empty column 2): repeat `  - STE:` lines. A Non-STE line follows the STE line of its own sub-row.
- **A Help note that is its own column-2 row** goes at the same level as Meaning and Alternative. Examples include "For other meanings, use:", "For safety instructions, use:", a note that replaces an alternative ("Use an accurate verb."), and "Do not use COULD (v) to show possibility". Its examples are nested under it.
- **A Help note printed under an alternative or meaning, inside the same cell** is nested under that item, after its examples: `  - Help: Refer to rule 1.5.`
- **A Help note that introduces further alternatives** ("For other meanings, use:", "For safety instructions, use:", "For electrical systems, use:") is **always** at item level, even when it is printed in the same cell as the meaning above it.
- **A Help bulb can share a row with an unrelated example.**
  - CHANGE (v): the second STE example sits beside the "For other meanings, use:" bulb.
  - CHARGE (v): the bulb sits just below the second STE example.

  In both cases the example belongs to the meaning above. Write all of that meaning's STE lines first, then the `- Help:` line.
- **Omit empty cells.** Do not write `STE:` or `Non-STE:` lines with no text.
- **Multi-line example content** (dash lists, `(1)`/`(a)` sub-steps): continuation lines indented under the example, each ending with `<br>`, list markers escaped.
- **Page marker** `<!-- page N | 2-1-A3 -->` goes immediately before the first entry on each page. Entries never break across pages in this issue.
- **Letter files** start with front matter, then `# <Letter>` (the XYZ file is `# X, Y, Z`). The file contains no other headings besides the entries.
- **Fragments.** When a transcription unit writes a *fragment* (a file under `.work/issue-9/parts/`), the fragment has **no front matter and no title**: only page markers and content. The assembly step adds the front matter and title when it concatenates the fragments in page order.

### 6.2 More examples

```markdown
## abandon (v)
- Status: not approved
- Alternative: GO (v)
  - STE: IF THERE IS A FIRE, IMMEDIATELY GO TO A SAFE AREA.
  - Non-STE: If there is a fire, immediately abandon the area.
- Alternative: STOP (v)
  - STE: IF THE VALUES ARE INCORRECT, STOP THE TEST PROCEDURE.
  - Non-STE: If the values are incorrect, abandon the test procedure.

## PUT (v)
- Status: approved
- Forms: PUTS, PUT
- Help (word column): No other verb forms.
- Meaning: …
  - STE: …
  - STE: …
```

## 7. Figures

Figures are cropped into `issue-9/assets/`:

| File | Source |
|---|---|
| `cover.jpg` | p1 cover picture |
| `general-introduction-vitruvian-man.jpg` | p35 (the caption is part of the image) |
| `part-1-cover-typewriter.jpg` | p43 |
| `rule-3-6-passive-to-active.jpg` | p73 diagram |
| `part-2-cover-typewriter.jpg` | p129 (the Kerouac quote is part of the image) |
| `how-to-select-words-flowchart.jpg` | p144 flowchart |

Text that exists only inside an image (the captions on p35 and p129, the typewriter page on p43) is transcribed in the *Figure description:*, clearly labeled as text in the image.
