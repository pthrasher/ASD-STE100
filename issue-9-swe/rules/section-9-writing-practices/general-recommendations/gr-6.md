---
title: "GR-6 Latin abbreviations"
gr: "GR-6"
section: "Section 9 - Writing practices"
topic: "General recommendations"
inherits: "../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-6.md"
status: adapted
mechanical-check: detects
---

# GR-6 Latin abbreviations

This recommendation tells you not to use Latin abbreviations, for example “e.g.,” “i.e.,” and “etc.” Use English words.

Source: [Issue 9, GR-6](../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-6.md) gives the full text and the original examples.

## In software text

The profile adds English words for three abbreviations that Issue 9 does not give: vs., cf., and N.B. The table shows them.

Latin abbreviations are very frequent in documentation, code comments, and pull request descriptions. Write English words, or change the sentence:

| Latin abbreviation | Write |
|---|---|
| e.g. | for example |
| i.e. | that is. Frequently, a different sentence construction is better. |
| etc. | Give the full list, or write “and other …”. If the list is not necessary, remove it. |
| vs. | “or,” or “compared with” |
| cf. | refer to |
| N.B. | Write a note ([Rule 5.5](../../section-5-procedural-writing/rule-5-05.md)). |

Issue 9 gives the English words for “e.g.,” “i.e.,” and “etc.” The words for “vs.,” “cf.,” and “N.B.” are decisions of the profile.

“Via” is not an abbreviation, but it is also Latin, and it is frequent in software text. The Issue 9 dictionary gives “via (prep)” as not approved. Its alternative is THROUGH (prep). In software text, IN, WITH, or FROM is frequently more accurate.

Text in code format is not part of this recommendation. The directory `/etc` and a flag `--via` are names in the code ([Rule 10.1](../../section-10-code-in-text/rule-10-01.md)).

## Examples

- [Non-STE] Set a short timeout (e.g., 5s) for health checks.
- [STE] For health checks, set a short timeout (for example, 5 seconds).
- [Non-STE] Supported formats: JSON, YAML, TOML, etc.
- [STE] The tool can read configuration files in JSON, YAML, and TOML.
- [Non-STE] Pass the token via the `Authorization` header.
- [STE] Send the token in the `Authorization` header.
- [Non-STE] Only use `--force` on a fresh clone, i.e. one with no local changes.
- [STE] Use the `--force` flag only on a local repository that has no changes.

## Review notes

- A check can find all Latin abbreviations of its list, and “via.” It must first remove code spans, code blocks, and URLs. If it does not, it shows `/etc/hosts` and a URL that contains “via” as areas to review.
- A check does not find a Latin abbreviation that has no periods (“eg,” “ie”), unless these are also in its list.
- Do not replace “etc.” with “and other items” automatically. The reader then knows no more than before. The writer must give the full list, or remove the list. Only a person who knows the items can do this.
- Do not replace “i.e.” with “that is” automatically. Frequently, the text after “i.e.” gives the meaning of a term. Write it as a relative clause or as a new sentence.
