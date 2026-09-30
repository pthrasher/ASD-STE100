---
title: "Rule 1.2"
rule: "1.2"
section: "Section 1 – Words"
topic: "Part of speech"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-02.md"
status: unchanged
mechanical-check: suggests
---

# Rule 1.2 – Part of speech

> **Rule 1.2** **Use approved words from the dictionary only as the specified part of speech.**

Source: [Issue 9, Rule 1.2](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-02.md) gives the full text and the original examples.

## In software text

Software text frequently uses a noun as a verb. The Issue 9 dictionary gives many of these words as approved nouns only, for example TEST (n), CHECK (n), OUTPUT (n), and DROP (n). You cannot write “test the endpoint,” “check the log,” “the command outputs JSON,” or “drop the table.”

Technical nouns and technical verbs also have a part of speech. The heading of each entry in [verbs.md](../../dictionary/verbs.md) and [nouns.md](../../dictionary/nouns.md) gives it, for example “commit (v)” and “commit (TN).” If the profile gives a word only as a noun, do not use it as a verb ([Rule 1.7](rule-1-07.md)). If the profile gives a word only as a verb, do not use it as a noun ([Rule 1.13](rule-1-13.md)).

A commit subject and the first line of a docstring start with a verb in the imperative ([commit messages](../../text-types/commit-messages.md), [code comments](../../text-types/code-comments.md)). Make sure that this verb is an approved verb or a technical verb. “Test,” “Check,” “Log,” and “Cache” are frequent at the start of a commit subject, and none of them is approved as a verb.

## Examples

- [Non-STE] Test the endpoint with an expired token.
- [STE] Do a test of the endpoint with an expired token.
  (TEST (n) is approved. “Test (v)” is not approved.)
- [Non-STE] Check the logs for errors.
- [STE] Examine the log for errors.
  (CHECK (n) is approved. “Check (v)” is not approved.)
- [Non-STE] Drop the `sessions` table before you execute the migration.
- [STE] Delete the `sessions` table before you execute the migration.
  (DROP (n) is approved with the meaning “A small quantity of liquid in a spherical shape.” “Drop (v)” is not approved.)
- [Non-STE] The command outputs JSON.
- [STE] The output of the command is JSON.
- [Non-STE] Log request IDs in the upload client
- [STE] Record request IDs in the log of the upload client
  (A commit subject. “Log (v)” is not approved. Refer to [log (v)](../../dictionary/verbs.md#log-v).)

## Review notes

- The reviewer must find the part of speech of each word from its function in the sentence. The spelling of the word does not tell you the part of speech. In “Examine the test log,” “test” is part of a noun. In “Test the log,” it is a verb.
- A mechanical check that compares words with a word list cannot find this error. “Test,” “check,” and “output” are in the dictionary.
- A check with a part-of-speech tagger can show possible problems. It frequently gives an incorrect part of speech for the first word of a commit subject or a heading, because these lines have no subject. Thus, it shows correct text as a problem and does not find some errors.
- Do not replace the verb with the approved noun word for word. “Test the endpoint” does not become STE if you only change the word. Use a different sentence construction: “Do a test of the endpoint” ([Rule 9.1](../section-9-writing-practices/rule-9-01.md)).
