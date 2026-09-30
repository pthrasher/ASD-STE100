---
title: "Rule 9.3"
rule: "9.3"
section: "Section 9 - Writing practices"
topic: "How to use approved words correctly"
inherits: "../../../issue-9/part-1-writing-rules/section-9-writing-practices/rule-9-03.md"
status: adapted
mechanical-check: suggests
---

# Rule 9.3 – How to use approved words correctly

> **Rule 9.3** **When you use two words together, do not make phrasal verbs.**

Source: [Issue 9, Rule 9.3](../../../issue-9/part-1-writing-rules/section-9-writing-practices/rule-9-03.md) gives the full text and the original examples.

## In software text

The profile adds this decision: [roll back (v)](../../dictionary/verbs.md#roll-back-v) is a technical verb, not a phrasal verb. Rule 1.12 also gives technical verbs of two words, for example “zoom in” and “zoom out.” Do not make other phrasal verbs from “roll.” The profile does not give “back up” as a verb. For a backup, use the technical noun “backup” (Issue 9, Rule 1.5, category 19): “Make a backup of the database.”

Phrasal verbs are very frequent in text for developers. Use one verb that gives the meaning:

| Phrasal verb | Write |
|---|---|
| set up | install, prepare, set, or make. Give the steps. |
| spin up | start |
| shut down, tear down | stop, or delete |
| roll out | deploy, or release |
| look up | find |
| check out (a branch) | give the command, for example `git switch release` |
| check out (a document) | refer to, or read |
| clean up | delete, or remove |
| back up | make a backup of |

The correct verb is different for each meaning of the phrasal verb. Find the meaning in the sentence before you select the verb ([Rule 9.1](rule-9-01.md)).

A phrasal verb in code format is part of a command, for example `docker compose up`. It is not a word of the text ([Rule 10.1](../section-10-code-in-text/rule-10-01.md)). The nouns “backup,” “setup,” “cleanup,” “rollout,” and “checkout” are not phrasal verbs. Rule 1.5 and [nouns.md](../../dictionary/nouns.md) control them. For example, “rollout” is a term that you must not use for a [deployment (TN)](../../dictionary/nouns.md#deployment-tn).

## Examples

- [Non-STE] Spin up a Postgres container for the tests.
- [STE] Start a database container for the tests.
- [Non-STE] Back up the database before you migrate.
- [STE] Make a backup of the database before you execute the migration.
- [Non-STE] Clean up the temp files after the build.
- [STE] Delete the temporary files after the build.
- [Non-STE] Roll out the new version to all regions.
- [STE] Deploy the new version to all regions.
- [Non-STE] Set up the project locally.
- [STE] Install the dependencies. Then make a `.env` file from `.env.example`.

## Review notes

- A check with a list of phrasal verbs can find the frequent ones. It does not find a phrasal verb that is not in its list. It does not find a phrasal verb when the object is between the two words, for example “Spin the cluster up.”
- A check shows correct text as areas to review. “Roll back,” “zoom in,” and the approved phrasal verbs of Issue 9 (for example “put on”) are correct. An adverb of direction after a verb is correct: “Move the slider up.” The nouns “backup” and “setup” are not verbs.
- Do not replace a phrasal verb automatically. “Set up” can be install, prepare, set, or make. Only a reader who knows the task can select the verb.
- The reviewer must compare the meaning of the two words together with the meaning of each word. If the meaning is new, the two words are a phrasal verb.
