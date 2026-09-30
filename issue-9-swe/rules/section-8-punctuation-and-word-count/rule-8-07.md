---
title: "Rule 8.7"
rule: "8.7"
section: "Section 8 - Punctuation and word count"
topic: "Word count"
inherits: "../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-07.md"
status: unchanged
mechanical-check: detects
---

# Rule 8.7 – Word count

> **Rule 8.7** **Hyphenated words count as one word.**

Source: [Issue 9, Rule 8.7](../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-07.md) gives the full text and the original examples.

## In software text

The terms read-only, command-line, end-to-end, and third-party count as one word each. Use hyphens only as [Rule 8.2](rule-8-02.md) tells you: to connect words that are directly related.

A hyphen in a code span, for example in the flag `--dry-run`, is part of the code. The full code span counts as one word because it is code ([Rule 10.2](../section-10-code-in-text/rule-10-02.md)), not because it has a hyphen.

## Examples

- [Non-STE] Install the command line tool.
- [STE] Install the command-line tool. &emsp;(4 words)
- [Non-STE] Write end to end tests for the orders endpoint.
- [STE] Write end-to-end tests for the `/orders` endpoint. &emsp;(7 words)
- [Non-STE] Don't write one-off quick-and-dirty data-fix scripts for post-migration clean-up.
  (The hyphens connect words that are not directly related. They only make the count smaller.)
- [STE] Do not write a script to correct data after a migration. Put the correction in the migration. &emsp;(11 words, then 6 words)

## Review notes

- A check can find all hyphenated words and count each one as one word. It must not count a code span, a flag, a range of numbers (for example 1-5), or a dash as a hyphenated word.
- A check cannot know if the hyphen connects words that are directly related. A writer, or an agent that must obey a word limit, can add hyphens only to make the count smaller. The reviewer must examine each long hyphenated term.
- A hyphenated term is one word for the count, but each part must be an approved word, or the full term must be a technical noun (Rule 1.5).
