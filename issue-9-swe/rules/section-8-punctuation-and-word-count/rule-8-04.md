---
title: "Rule 8.4"
rule: "8.4"
section: "Section 8 - Punctuation and word count"
topic: "Word count"
inherits: "../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-04.md"
status: unchanged
mechanical-check: suggests
---

# Rule 8.4 – Word count

> **Rule 8.4** **In a vertical list, a colon (:) has the same effect on word count as a period and shows the end of a sentence.**

Source: [Issue 9, Rule 8.4](../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-04.md) gives the full text and the original examples.

## In software text

Vertical lists are frequent in READMEs, runbooks, pull request descriptions, and agent instructions. Count the words before the colon as one sentence. Count each item of the list as a different sentence. The limits are 20 words for an instruction ([Rule 5.1](../section-5-procedural-writing/rule-5-01.md)) and 25 words for a description ([Rule 6.3](../section-6-descriptive-writing/rule-6-03.md)).

- If a list item contains a second list, each item of the second list is also a different sentence.
- If a list item is only a code span, for example a file path, it counts as one word ([Rule 10.2](../section-10-code-in-text/rule-10-02.md)).
- A list item can contain more than one sentence. Count the words of each sentence independently.

## Examples

- [Non-STE] To get your change merged quickly and avoid a second round of review, please make sure you have done all of the following before opening a pull request: &emsp;(28 words)
- [STE] Before you open a pull request, do these steps: &emsp;(9 words)<br>
  \- Rebase your branch on the `main` branch. &emsp;(7 words)<br>
  \- Execute the unit tests. &emsp;(4 words)<br>
  \- Add an entry for your change to `CHANGELOG.md`. &emsp;(8 words)
- [Non-STE] The service reads config from:<br>
  \- `config/default.yaml`, which is always loaded first and holds the defaults for every setting the service supports, including ones that aren't documented yet<br>
  \- `config/local.yaml`, if present, which overrides it
- [STE] The service reads its configuration from these files, in this sequence: &emsp;(11 words)<br>
  \- `config/default.yaml`. This file contains the default values. &emsp;(1 word, then 6 words)<br>
  \- `config/local.yaml`. A value in this file replaces the default value. &emsp;(1 word, then 9 words)

## Review notes

- A check can count the words before a colon and in each list item. It cannot know if a sentence is an instruction or a description. Thus, it cannot know if the limit is 20 or 25 words.
- A colon that is not before a vertical list does not end a sentence, for example “Error: the file is missing.” A check that counts each colon as the end of a sentence gives a number that is too low.
- In Markdown, a list item can continue on a second line. A table cell or a YAML comment can contain a list with no colon. A check that reads lines, not list items, counts incorrectly.
- Do not remove words from the sentence before the colon only to make it shorter. From that sentence, the reader must know which items the list contains.
