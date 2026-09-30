---
title: "Rule 4.2"
rule: "4.2"
section: "Section 4 – Sentences"
topic: "Short sentences and clear sentence structures"
inherits: "../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-02.md"
status: adapted
mechanical-check: suggests
---

# Rule 4.2 – Short sentences and clear sentence structures

> **Rule 4.2** **Do not omit words or use contractions to make your sentences shorter.**

Source: [Issue 9, Rule 4.2](../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-02.md) gives the full text and the original examples.

## In software text

The profile adds these interpretations:

1. **The imperative is a full sentence.** The subject of an imperative sentence is the reader. Thus, a commit subject line in the imperative (“Add a timeout to the upload client”) and the first line of a docstring (“Return the user that has the given ID.”) have no missing subject. Refer to [commit messages](../../text-types/commit-messages.md) and [code comments](../../text-types/code-comments.md).
2. **Structured data is not a sentence.** A key and a value in a structured log (`status=503 retry_in=4s`) are data in code format. This rule is applicable to the text of the log message that is not data.
3. **Headings and table labels are not sentences.** A heading can be a noun, for example “Installation.” But a table cell that gives an instruction or information is a sentence.

Software text frequently has missing words:

- **Log messages and error messages** without a subject or a verb: “File not found,” “Connection refused,” “Invalid token.” Write a full sentence, and put the values in code format. Refer to [error messages](../../text-types/error-messages.md) and [log messages](../../text-types/log-messages.md).
- **Docstrings and API reference that have the format of a heading:** “Returns user if found, else None.” Write full sentences.
- **Agent instructions as short labels:** “No force push.” Write the instruction: “Do not use `git push --force`.”
- **Contractions:** “don't,” “can't,” “isn't,” “won't.” These are frequent in error messages. Write the words in full.

## Examples

- [Non-STE] Error: file not found: config.yaml
- [STE] Error: The service cannot find the `config.yaml` file.
- [Non-STE] Can't connect to DB, retrying in 5s
- [STE] The service cannot connect to the database. It will try again after 5 seconds.
- [Non-STE] Returns user if found, else None.
- [STE] Return the user that has the given ID. If no user has this ID, return `None`.
  (The first line of a docstring, in the imperative. The subject is not missing.)
- [Non-STE] Timeout for upload client
- [STE] Add a timeout to the upload client
  (A commit subject line. The Non-STE text has no verb.)
- [Non-STE] Clear cache and restart.
- [STE] Clear the cache. Then start the service again.

## Review notes

- The reviewer must find if each text is a sentence, a heading, a label, or data. Rule 4.2 is applicable only to sentences.
- The reviewer must find missing articles in a series. In “Remove the token and cache,” the reader cannot know if “the” refers to “cache.”
- A mechanical check can find all contractions. It incorrectly shows a problem for the possessive (“the user's token”) and for text in code format.
- A check can show lines that have no verb or that start with a past participle or an adjective, for example “File not found” and “Invalid token.” It incorrectly shows a problem for headings, table labels, and structured data.
- A check that examines each sentence for a subject shows each imperative sentence as a problem. The profile decision is that an imperative sentence has no missing subject.
- A check does not find missing articles in the middle of a sentence. Only a reader who knows the items can find them.
