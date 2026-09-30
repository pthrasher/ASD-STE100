---
title: "GR-1 The conjunction “that”"
gr: "GR-1"
section: "Section 9 - Writing practices"
topic: "General recommendations"
inherits: "../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-1.md"
status: unchanged
mechanical-check: suggests
---

# GR-1 The conjunction “that”

This recommendation tells you to use the conjunction “that” after verbs, for example “make sure,” “show,” and “recommend.”

Source: [Issue 9, GR-1](../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-1.md) gives the full text and the original examples.

## In software text

Software text frequently does not include “that” after “make sure,” “show,” “tell,” and “recommend.” Write “that” each time. It shows the reader where the first clause stops and the second clause starts.

In agent instructions, the conjunction is important. In “Make sure the tests pass,” an agent can find the instruction easily. In a longer sentence, for example “Make sure the branch the agent pushed passes the checks,” the agent cannot easily find the start of each clause. Use “that,” and write short clauses.

The conjunction also helps a translation tool. Many readers of software documentation read it through a translation tool.

## Examples

- [Non-STE] Make sure the tests pass before merging.
- [STE] Make sure that all tests pass before you merge the pull request.
- [Non-STE] The log shows the connection timed out.
- [STE] The log shows that a timeout occurred on the connection.
- [Non-STE] Confirm the branch is up to date with main.
- [STE] Make sure that the branch contains all commits from the `main` branch.
- [Non-STE] We recommend you pin the version in production.
- [STE] We recommend that you use a specified version of each dependency in the production environment.

## Review notes

- A check can find “make sure,” “show,” “tell,” and “recommend” when “that” does not follow them. It cannot find other verbs that start a clause, unless they are in its list.
- The check shows correct text as areas to review, for example “show the log” or “tell the user.” After these verbs, a noun follows, not a clause.
- An agent that adds “that” after each of these verbs can make incorrect sentences, for example “Show that the error message to the user.” The reviewer must read each sentence that the agent changed.
