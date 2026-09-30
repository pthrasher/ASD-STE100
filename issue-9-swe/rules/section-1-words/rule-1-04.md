---
title: "Rule 1.4"
rule: "1.4"
section: "Section 1 – Words"
topic: "Forms of verbs and adjectives"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-04.md"
status: unchanged
mechanical-check: suggests
---

# Rule 1.4 – Forms of verbs and adjectives

> **Rule 1.4** **Use only the approved forms of verbs and adjectives.**

Source: [Issue 9, Rule 1.4](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-04.md) gives the full text and the original examples.

## In software text

The Issue 9 dictionary gives the forms of each approved verb and adjective. For example, START has the forms STARTS, STARTED, STARTED. GET has only the forms GETS and GOT. The “-ing” form is not an approved form of a verb ([Rule 3.5](../section-3-verbs/rule-3-05.md)).

A technical verb obeys the same rules as an approved verb (Rule 1.12). [verbs.md](../../dictionary/verbs.md) does not give the forms of technical verbs. [Rule 3.1](../section-3-verbs/rule-3-01.md) tells you which forms to use.

[Log messages](../../text-types/log-messages.md) and progress messages frequently use the “-ing” form: “Connecting to database…” or “Deploying version 2.4…”. Write a sentence that has a subject and an approved form of the verb.

For adjectives, use the comparative and superlative forms that the dictionary gives, for example FAST (FASTER, FASTEST). If the dictionary gives no forms, use MORE and MOST.

## Examples

- [Non-STE] Starting server on port 8080…
- [STE] The server started on port 8080.
- [Non-STE] Deploying version 2.4 to the test environment.
- [STE] The pipeline deploys version 2.4 to the test environment.
- [Non-STE] The token has expired.
- [STE] The token is expired.
  (EXPIRED (adj) is approved. “Has expired” is not an approved verb form.)

## Review notes

- The reviewer must examine the form of each verb and adjective. Examine the forms of technical verbs also.
- A mechanical check can compare each word with the forms in the dictionary. It can show words that end in “-ing” and constructions such as “has expired.”
- The check shows correct text as a possible problem. Rule 3.5 lets you use an “-ing” word as a technical noun or as a modifier in a technical noun, for example “the logging configuration.” Many nouns also end in “-ing,” for example “string.” The check also shows the forms of technical verbs, for example “committed” and “rebased,” because the dictionary does not give them.
- The check does not find a form that is correct for a different part of speech. “Outputs” is correct as the plural of OUTPUT (n), but not as a verb: “The command outputs JSON” ([Rule 1.2](rule-1-02.md)).
- Do not delete the “-ing” word to make the check show no problem. “Server on port 8080” has no verb. Write a full sentence ([Rule 4.2](../section-4-sentences/rule-4-02.md)).
