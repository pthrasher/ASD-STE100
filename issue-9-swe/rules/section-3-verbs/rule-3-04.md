---
title: "Rule 3.4"
rule: "3.4"
section: "Section 3 - Verbs"
topic: "Verb forms and tenses of verbs"
inherits: "../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-04.md"
status: unchanged
mechanical-check: suggests
---

# Rule 3.4 – Verb forms and tenses of verbs

> **Rule 3.4** **Do not use auxiliary verbs to make complex verb constructions.**

Source: [Issue 9, Rule 3.4](../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-04.md) gives the full text and the original examples.

## In software text

Software text frequently contains these complex verb constructions:

- The present perfect in commit bodies and release text: “has been deployed,” “have been removed.”
- A modal verb and the passive in API reference text: “can be overridden,” “must be set,” “should be called.”
- Constructions that give an instruction without a subject: “needs to be restarted,” “is to be run.”

For each construction, find if the text is procedural or descriptive ([Rule 3.6](rule-3-06.md)):

- In a procedure, a runbook, or an agent instruction, write the imperative: “Clear the cache.”
- In descriptive text, write the agent as the subject and a simple tense: “The pipeline deployed the release.” If the reader is the agent, write “you.”

In API reference text, “can be” frequently tells the reader that a step is permitted. Write “You can” and the verb. If the text is about an optional value, write that the value is optional.

## Examples

- [Non-STE] The cache must be cleared before the migration is run.
- [STE] Clear the cache before you execute the migration.
- [Non-STE] This value can be overridden with the `--timeout` flag.
- [STE] You can change this value with the `--timeout` flag.
- [Non-STE] The release has been deployed to all regions.
- [STE] The pipeline deployed the release to all regions.
- [Non-STE] The API key needs to be rotated every 90 days.
- [STE] Replace the API key at intervals of 90 days or less.

## Review notes

- The reviewer must find the agent of each sentence, and find if the text is procedural or descriptive. The correct new text is different for each decision.
- A mechanical check can find these patterns: HAVE and a past participle, a modal verb and “be” and a past participle, “is to be,” and “needs to be.”
- The check incorrectly shows a problem when HAVE is the primary verb (“The table has deleted rows”), and when a past participle after “be” is an adjective (“The token must not be expired”). [Rule 3.3](rule-3-03.md) lets you use the adjective.
- A check can cause a new error. To remove the pattern, a writer can add an agent that is not correct, for example “The system must clear the cache,” when the reader must do the step. The reviewer must make sure that the agent is correct.
