---
title: "Rule 5.1"
rule: "5.1"
section: "Section 5 - Procedural writing"
topic: "Sentences"
inherits: "../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-01.md"
status: unchanged
mechanical-check: suggests
---

# Rule 5.1 – Sentences

> **Rule 5.1** **Write short sentences. Use a maximum of 20 words in each sentence.**

Source: [Issue 9, Rule 5.1](../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-01.md) gives the full text and the original examples.

## In software text

The limit of 20 words is applicable to each instruction in software text:

- a step in a README, a runbook, or an installation procedure
- a test step in a pull request ([pull requests](../../text-types/pull-requests.md))
- the instruction at the end of an error message ([error messages](../../text-types/error-messages.md))
- each instruction in a file for AI agents, for example `CLAUDE.md` or `AGENTS.md` ([agent instructions](../../text-types/agent-instructions.md))
- each sentence of a safety instruction ([Section 7](../section-7-safety-instructions/README.md))

Count the words with the rules of Section 8 and Section 10. Each code span counts as one word, and the text in a code block does not count ([Rule 10.2](../section-10-code-in-text/rule-10-02.md)). Thus, a command in a code block after the instruction is not part of the sentence ([Rule 10.3](../section-10-code-in-text/rule-10-03.md)).

A note is descriptive text, and its limit is 25 words ([Rule 5.5](rule-5-05.md)). If an instruction has more than 20 words, divide it. If the two parts do not occur at the same time, write two steps ([Rule 5.2](rule-5-02.md)).

## Examples

- [Non-STE] Before you open a PR, make sure you've rebased onto the latest main and that all of the tests, including the slow integration suite, pass locally.
- [STE] 1. Rebase your branch on the `main` branch.<br>
  2. Execute the unit tests and the integration tests on your computer.<br>
  3. Make sure that all the tests pass.<br>
  4. Open a pull request.
  (The Non-STE instruction has 26 words and four steps.)
- [Non-STE] When you're done making changes, run the formatter and then the linter, and if the linter reports anything, fix it before you commit.
- [STE] Before you commit your changes, format the code. Then, execute the linter. If the linter shows problems, correct them.
- [Non-STE] Error: could not connect to the database, so check that DATABASE_URL is set correctly and that the database server is up and reachable from this host.
- [STE] Error: The service cannot connect to the database. Make sure that `DATABASE_URL` has the correct value. Make sure that the database server operates.

## Review notes

- The reviewer must identify each sentence as an instruction (20 words) or as descriptive text (25 words). A README, a pull request, and an error message frequently contain the two types of text. A check that uses one limit for all sentences shows correct descriptive sentences, or it does not show long instructions.
- A simple word count gives a number that is too high for text in code format. It counts `git push --force` as three words, and a URL as many words. Section 10 counts each code span as one word.
- A check cannot find the end of an instruction in a list item, a table cell, or a YAML comment that has no period. The reviewer must find the sentences.
- A short sentence is not necessarily clear. Do not remove articles or other words to make an instruction shorter ([Rule 4.2](../section-4-sentences/rule-4-02.md)). Divide the instruction.
