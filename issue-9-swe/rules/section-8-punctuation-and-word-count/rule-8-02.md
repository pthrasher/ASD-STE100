---
title: "Rule 8.2"
rule: "8.2"
section: "Section 8 - Punctuation and word count"
topic: "Punctuation"
inherits: "../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-02.md"
status: unchanged
mechanical-check: none
---

# Rule 8.2 – Punctuation

> **Rule 8.2** **Use hyphens (-) to connect words that are directly related.**

Source: [Issue 9, Rule 8.2](../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-02.md) gives the full text and the original examples.

## In software text

Software text has many terms of two or more words that are adjectives before a noun. Connect the words of these terms with hyphens, as category 1 of the Issue 9 rule shows. For example: read-only file, command-line tool, end-to-end test, third-party service, two-factor authentication.

When the same words are a noun, they do not have a hyphen. For example: “Execute this command on the command line.” But “Install the command-line tool.”

Write each term with the same hyphens each time that it occurs ([Rule 9.4](../section-9-writing-practices/rule-9-04.md)). Do not write “command-line tool” in one step and “command line tool” in a different step. Issue 9 writes “e-mail” with a hyphen in Rule 1.5, category 19.

A hyphen in a code span is part of the code, for example the flag `--dry-run` or the package `python-dateutil`. Do not add a hyphen to code or remove a hyphen from code ([Section 10](../section-10-code-in-text/README.md)). Put flags in code format. Then the reader does not read `--` as a dash.

## Examples

- [Non-STE] Install the command line tool with pip.
- [STE] Install the command-line tool with `pip install`.
- [Non-STE] Write end to end tests for the orders endpoint.
- [STE] Write end-to-end tests for the `/orders` endpoint.
- [Non-STE] Pass --dry run to preview the changes.
- [STE] Add the `--dry-run` flag. The command then shows the changes but does not make them.
- [Non-STE] Mount the volume read only in the build container.
- [STE] Attach the volume to the build container as a read-only volume.

## Review notes

- Only the reviewer can know if the words of a term are directly related. A check cannot know if “data migration script” is one term or a noun cluster. For long noun clusters, refer to [Section 2](../section-2-multi-word-nouns/README.md).
- A check that finds terms without hyphens shows many results that are not errors. “Command line” is correct as a noun and not correct before a noun. A check that does not know the grammar of the sentence cannot find the difference.
- A check that adds hyphens can change code. Flags, package names, and file names in code format must not change.
- A hyphen does not make a word approved. Each word in a hyphenated term must be approved, or the full term must be a technical noun (Rule 1.5).
