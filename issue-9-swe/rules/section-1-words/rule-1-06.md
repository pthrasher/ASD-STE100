---
title: "Rule 1.6"
rule: "1.6"
section: "Section 1 – Words"
topic: "Technical nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-06.md"
status: adapted
mechanical-check: none
---

# Rule 1.6 – Technical nouns

> **Rule 1.6** **Use a word that is not approved in the dictionary, only when it is a technical noun or part of a technical noun.**

Source: [Issue 9, Rule 1.6](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-06.md) gives the full text and the original examples.

## In software text

The profile uses this rule for some nouns that are not approved in Issue 9 in their general meaning. [nouns.md](../../dictionary/nouns.md) gives each of them as a technical noun with a software meaning only:

| Word | Issue 9 status and alternative | Technical noun in the profile |
|---|---|---|
| build (n) | not approved, STRUCTURE (n) | [build (TN)](../../dictionary/nouns.md#build-tn): the procedure that makes packages from source code, or its result |
| exception (n) | not approved | [exception (TN)](../../dictionary/nouns.md#exception-tn): an object that code raises to show an error |
| process (n) | not approved, PROCEDURE (n) | [process (TN)](../../dictionary/nouns.md#process-tn): a program that is in operation |
| request (n) | not approved, TELL (v), WRITE (v) | [request (TN)](../../dictionary/nouns.md#request-tn): a message that a client sends to a server |

Use each of these words only with its software meaning. For the general meaning, use the Issue 9 alternative.

A word that is not approved can also be part of a technical noun. In “the `main` branch,” `main` is the name of the branch. The profile writes the name in code format. It is not the adjective “main,” and you must not replace it with PRIMARY (adj).

## Examples

- [Non-STE] Send a request to the platform team for access to the database.
- [STE] Tell the platform team that you must have access to the database.
  (“Request” is a technical noun only for a message between programs: “The server rejects requests that do not have a token.”)
- [Non-STE] The release process has five steps.
- [STE] The release procedure has five steps.
  (“Process” is a technical noun only for an operating-system process: “Stop the process.”)
- [Non-STE] All endpoints need a token, with the exception of `/health`.
- [STE] A token is necessary for all endpoints, but not for `/health`.
  (“Exception” is a technical noun only for an error object in code.)
- [Non-STE] The main configuration file is `app.yaml`.
- [STE] The primary configuration file is `app.yaml`.
  (“Main” is not approved and is not part of a technical noun here.)

## Review notes

- For each of these words, the reviewer must find if the sentence uses the software meaning or the general meaning. Only the sentence shows the meaning.
- The reviewer must find if a word is part of a technical noun, as “main” is part of “main landing gear” in Issue 9. If a writer uses the word as a general adjective, it is not part of a technical noun.
- A mechanical check cannot help. A check that uses the Issue 9 dictionary shows “request” and “process” as not approved in all sentences, also in correct sentences. A check that uses the profile dictionary accepts these words in all sentences, also in incorrect sentences.
