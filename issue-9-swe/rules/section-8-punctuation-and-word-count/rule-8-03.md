---
title: "Rule 8.3"
rule: "8.3"
section: "Section 8 - Punctuation and word count"
topic: "Punctuation"
inherits: "../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-03.md"
status: adapted
mechanical-check: none
---

# Rule 8.3 – Punctuation

> **Rule 8.3** **You can use parentheses:**
> - **To make references to illustrations or text**
> - **To include letters or numbers that identify items on an illustration or in a text**
> - **To identify the work steps in a procedure**
> - **To include abbreviations**
> - **To give the singular and plural forms of a noun at the same time**
> - **To explain words or a part of a sentence**
> - **To include an alternative.**

Source: [Issue 9, Rule 8.3](../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-03.md) gives the full text and the original examples.

## In software text

The profile adds one recommendation for agent instructions. If an instruction has an alternative, write the condition that selects the alternative. Do not only put the alternative in parentheses. An agent cannot know when to use the alternative if the text does not give the condition.

Software text uses parentheses for these functions:

- A reference to a different text: “(refer to `docs/setup.md`)”. Some hosting services add a number to the commit subject when they merge a pull request, for example “(#1234)”. This number is also a reference.
- An abbreviation: write the full term, then the abbreviation in parentheses, for example “pull request (PR)”. Then use one of the two terms in all of the text ([Rule 9.4](../section-9-writing-practices/rule-9-04.md), [nouns.md](../../dictionary/nouns.md#pull-request-tn)).
- An explanation: “Set the timeout to 30 seconds (the maximum time for one request).”
- The singular and the plural: “Delete the file(s).”

Parentheses in a code span are part of the code, for example `close()`. They are not the parentheses of this rule ([Section 10](../section-10-code-in-text/README.md)).

## Examples

- [Non-STE] Open a PR and wait for CI.
- [STE] Open a pull request (PR). Then wait until all pipeline checks pass.
- [Non-STE] Install deps with npm (or yarn).
- [STE] If the repository has a `yarn.lock` file, install the dependencies with `yarn install`. If the repository does not have this file, install them with `npm install`.
  (An agent instruction. The condition tells the agent which command to use.)
- [Non-STE] Timeout for the request, defaults to 30.
- [STE] The `timeout` parameter sets the maximum time for the request (in seconds). The default value is 30.
- [Non-STE] See the setup docs for details.
- [STE] Install the dependencies (refer to `docs/setup.md`).

## Review notes

- A check cannot tell the function of parentheses. It cannot know if the text in parentheses is a reference, an explanation, or an alternative. It cannot find a function that Rule 8.3 does not give.
- A check that looks for parentheses must first remove code spans and code blocks. Function calls, for example `close()`, contain parentheses.
- The reviewer must find the text in parentheses that is not necessary. Long text in parentheses is frequently a second sentence. Write it as a sentence (Rule 8.5).
- An abbreviation in parentheses after a term tells the reader that the two terms are for the same item. Make sure that the text then uses the same term each time.
