---
title: "Rule 6.6"
rule: "6.6"
section: "Section 6 - Descriptive writing"
topic: "Paragraphs"
inherits: "../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-06.md"
status: unchanged
mechanical-check: suggests
---

# Rule 6.6 – Paragraphs

> **Rule 6.6** **Make sure that no paragraph has more than six sentences.**

Source: [Issue 9, Rule 6.6](../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-06.md) gives the full text and the original examples.

## In software text

If a paragraph has more than six sentences, divide it into two paragraphs. Each new paragraph must have one topic and a topic sentence ([Rule 6.5](rule-6-05.md), [Rule 6.4](rule-6-04.md)).

This is applicable to the body of a commit message, a pull request description, a README section, a long docstring, and a long code comment. A pull request description that is one large paragraph is a frequent problem. A reader cannot find the information about the tests or the deployment quickly. Refer to [pull requests](../../text-types/pull-requests.md).

In the Issue 9 example for this rule, a sentence that ends with a colon and a vertical list is one sentence of the paragraph. A code block is not a sentence, and it divides the text into two paragraphs.

## Examples

- [Non-STE] The importer reads CSV files from the inbox bucket. It validates each row against the schema. Invalid rows go to a quarantine table. Valid rows are upserted into `customers`. After each file it writes a summary to the audit log. Then it moves the file to the archive bucket. If the file is larger than 1 GB, it is split first. Splitting uses the `split_csv` helper.
- [STE] The importer reads CSV files from the `inbox` bucket. It makes sure that each row agrees with the schema. It writes the incorrect rows to the `quarantine` table and the correct rows to the `customers` table. After each file, it writes the result to the audit log. Then, it moves the file to the `archive` bucket.<br>
  <br>
  If a file is larger than 1 GB, the importer divides the file before it reads it. The `split_csv` function divides the file.
  (The Non-STE paragraph has eight sentences and two topics. The STE text has two paragraphs: one paragraph with five sentences and one paragraph with two sentences.)

## Review notes

- A mechanical check can count the sentences in each paragraph and show paragraphs with more than six. These results are areas to examine.
- Where the count gives incorrect results:
  - The check can count a period in a version number, a file name, or an abbreviation as the end of a sentence (“v1.2.3,” “config.yaml,” “e.g.”). If the check ignores text in code format, `v1.2.3` does not cause this problem.
  - If the check starts a new paragraph at each new line, it finds too many paragraphs in a commit body that has a new line after 72 characters.
  - In a code comment, each line starts with `#`, and a line with only `#` divides two paragraphs. A check that finds paragraphs only from blank lines cannot find these paragraphs.
  - A list item without a period can be one sentence or part of a sentence. The check cannot know.
- A paragraph with six sentences or less is not necessarily correct. It must also have one topic ([Rule 6.5](rule-6-05.md)). Do not divide a paragraph only to make the count less than seven. Divide it where the topic changes.
