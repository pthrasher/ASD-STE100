---
title: "Rule 4.4"
rule: "4.4"
section: "Section 4 – Sentences"
topic: "Connecting words and connecting phrases"
inherits: "../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-04.md"
status: unchanged
mechanical-check: none
---

# Rule 4.4 – Connecting words and connecting phrases

> **Rule 4.4** **Use connecting words and connecting phrases to connect sentences that contain related topics.**

Source: [Issue 9, Rule 4.4](../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-04.md) gives the full text and the original examples.

## In software text

A commit body, a pull request description, and an incident note usually tell a cause and a result. Use a connecting word or a connecting phrase to show the relation between the sentences. For example, use AND, BUT, THEN, THUS, ALSO, “as a result,” and “at the same time.” You can also use THIS or THESE: “This change …,” “These tests …”.

Software text frequently uses connecting words that are not approved. Use an approved alternative:

- “However” → BUT
- “Therefore,” “so,” “hence” → THUS or “as a result”
- “Additionally,” “moreover,” “furthermore” → ALSO
- “Otherwise” → IF … NOT, as a full sentence: “If the token is not correct, …”.

Without a connecting word, an agent can read each sentence as an instruction or a fact that has no relation to the other sentences. For example, if a sentence gives the cause of the next instruction, start the next sentence with THUS.

## Examples

- [Non-STE] The cache key didn't include the locale. Users saw pages in the wrong locale.
- [STE] The cache key did not include the locale. As a result, some users saw pages in an incorrect locale.
- [Non-STE] Moreover, the endpoint now validates the email field.
- [STE] The endpoint also validates the `email` field.
- [Non-STE] Delete node_modules. Otherwise stale packages may remain.
- [STE] Delete the `node_modules/` directory. Then install the dependencies again. This procedure removes the packages that are not in the lock file.
- [Non-STE] The migration locks the table, so do it outside business hours.
- [STE] For approximately 5 minutes, the migration prevents changes to the `orders` table. Thus, execute the migration when the number of users is low.

## Review notes

- The reviewer must find if two sentences have a relation that the reader must know, and if the connecting word gives the correct relation. THUS must connect a cause and its result. BUT must connect two facts that do not agree.
- A mechanical check can find connecting words that are not approved, for example “however” and “therefore.” That is a check for [Rule 1.1](../section-1-words/rule-1-01.md), not for this rule.
- A check cannot find a missing connecting word, because it cannot know the relation between two sentences. It also cannot find an incorrect connecting word, for example THUS between two sentences that are not a cause and a result.
- A check that replaces “however” with BUT in each sentence can give an incorrect relation. The reviewer must read the two sentences.
