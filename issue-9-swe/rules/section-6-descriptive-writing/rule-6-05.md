---
title: "Rule 6.5"
rule: "6.5"
section: "Section 6 - Descriptive writing"
topic: "Paragraphs"
inherits: "../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-05.md"
status: unchanged
mechanical-check: none
---

# Rule 6.5 – Paragraphs

> **Rule 6.5** **Make sure that each paragraph has only one topic.**

Source: [Issue 9, Rule 6.5](../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-05.md) gives the full text and the original examples.

## In software text

Each paragraph has one topic, and its first sentence gives that topic ([Rule 6.4](rule-6-04.md)). If you put the topic sentences of a text in a list, the list must show the structure of the text.

- **Commit messages.** If a commit body has paragraphs about two changes that are not related, the commit possibly contains two changes. Divide the commit. Refer to [commit messages](../../text-types/commit-messages.md).
- **Pull requests.** Put the steps for deployment or for tests in their own section, not in a paragraph about the change. Refer to [pull requests](../../text-types/pull-requests.md).
- **Code comments.** Do not put information about the code, about the history of the code, and about a subsequent change in one comment paragraph. Refer to [code comments](../../text-types/code-comments.md).

## Examples

- [Non-STE] This adds a `--dry-run` flag to the sync command. I also cleaned up some imports while I was there, and note that this needs the new IAM role before deploy.
- [STE] This pull request adds the `--dry-run` flag to the `sync` command. With this flag, the command shows the changes but does not make them.<br>
  <br>
  This pull request also removes imports that the code does not use.<br>
  <br>
  **Deployment**<br>
  Before you deploy this change, add the `sync-reader` IAM role to the service account.
  (Three topics: the new flag, the imports, and a step for the deployment. The step is procedural text in its own section.)
- [Non-STE] # Parses the header. We used regex here before but it was too slow. TODO: move to the new tokenizer. The header can be empty.
- [STE] # This function parses the header and returns a dictionary. If the header is empty, the function returns an empty dictionary.<br>#<br># TODO: Replace this parser with the tokenizer in `tokenizer.py` (issue #412).
  (The first paragraph gives the operation of the function. The second paragraph gives a subsequent change. The history of the code is in the history of the repository, not in the comment.)

## Review notes

- The reviewer must identify the topic of each paragraph and make sure that each paragraph has only one topic. A mechanical check cannot find the topic of a paragraph.
- To examine a long text, write the topic sentences of the text in a list. If the list does not show a clear structure, the text has a paragraph with more than one topic, or a paragraph that has no topic sentence.
- A paragraph that has six sentences or less can also have two topics ([Rule 6.6](rule-6-06.md)). A count of sentences does not find this problem.
