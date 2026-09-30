---
title: "Rule 8.6"
rule: "8.6"
section: "Section 8 - Punctuation and word count"
topic: "Word count"
inherits: "../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-06.md"
status: adapted
mechanical-check: suggests
---

# Rule 8.6 – Word count

> **Rule 8.6** **Count each of these elements as one word:**
> - **Numbers**
> - **Numbers together with units of measurement**
> - **Abbreviations**
> - **Alphanumeric identifiers**
> - **Quoted text**
> - **Titles, headings, and text on placards and labels**
> - **Proper nouns of individuals, groups, organizations,<br>and geopolitical entities.**

Source: [Issue 9, Rule 8.6](../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-06.md) gives the full text and the original examples.

## In software text

The profile adds one element to this list: each code span counts as one word ([Rule 10.2](../section-10-code-in-text/rule-10-02.md)). A code span can be an identifier, a command, a path, a flag, or a value. For example, `git push --force origin main` is one word.

The elements of Issue 9 occur in software text as follows:

- Numbers: 3, 200, 404.
- Numbers together with units of measurement: 30 seconds, 512 MB, 100 ms.
- Abbreviations: API, CLI, URL, JSON, HTTP. If the reader possibly does not know an abbreviation, give the full term first ([Rule 8.3](rule-8-03.md)).
- Alphanumeric identifiers: a version number (2.4.1), an issue number (#1234), a commit hash (3de91f1), an error code (E1203).
- Quoted text: the label of a control in a user interface (“Approve”), or the text of an error message from a different program. You cannot change this text. It counts as one word, as the text of a placard does in Issue 9.
- Titles and headings: the title of a document or a heading in a README.
- Proper nouns of organizations, for example Python Software Foundation.

## Examples

- [Non-STE] Set max connections in the postgres conf file to 200, then restart postgres so the server process picks up the new value.
- [STE] Set `max_connections` to 200 in `postgresql.conf`. &emsp;(6 words)<br>
  Then start the database server again. &emsp;(6 words)
- [Non-STE] If you get E1203 on upload, the file is over the 5 GB limit.
- [STE] Error `E1203` occurs when a file is larger than 5 GB. &emsp;(10 words)
- [Non-STE] Hit Approve once the checks go green.
- [STE] When all checks pass, click “Approve.” &emsp;(6 words)
- [Non-STE] See the Getting Started section of the README for how to install it.
- [STE] To install the package, refer to “Getting Started” in the README. &emsp;(10 words)

## Review notes

- A basic word count counts `git push --force` as three words and a URL as many words. A check must count each code span as one word.
- A check can find numbers, abbreviations, code spans, and quoted text. It cannot find a title, a heading, or a proper noun that is not in quotation marks. It counts “Python Software Foundation” as three words. The reviewer must count these sentences again.
- Do not put usual words in code format or in quotation marks to make a sentence shorter. Code format is only for code ([Section 10](../section-10-code-in-text/README.md)). The reviewer must examine each code span and each quoted text. A check cannot find this problem.
- Issue 9 does not count the numbers that identify paragraphs or steps. A check that counts “1.” at the start of a Markdown list item gives a number that is too high.
- Issue 9 does not include the names of products in this list, for example the name of a cloud service. The profile does not give a decision about them. The reviewer must count them and write the decision in the report.
