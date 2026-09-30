---
title: "GR-2 The preposition “with”"
gr: "GR-2"
section: "Section 9 - Writing practices"
topic: "General recommendations"
inherits: "../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-2.md"
status: unchanged
mechanical-check: none
---

# GR-2 The preposition “with”

This recommendation tells you to make sure that the preposition “with” does not give a sentence two possible meanings.

Source: [Issue 9, GR-2](../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-2.md) gives the full text and the original examples.

## In software text

In software text, “with” can show a tool (“Install the package with `pip`”), a part of an item (“the branch with the old migration”), or a condition (“Do the test with the cache enabled”). If the reader can think of two meanings, write the sentence again:

- For a part of an item, write “that has” or “that contains.”
- For a condition, write the condition first, as a clause at the start of the sentence ([Rule 5.4](../../section-5-procedural-writing/rule-5-04.md)).
- For a tool, give the primary action verb, then the tool: “Revert the commit with `git revert`.” Do not write “Use `git revert` to …” when the verb of the task is “revert.”

If a sentence can have two meanings, an agent can select the incorrect meaning. It does not know which meaning the writer wants, and it frequently does not tell you.

## Examples

- [Non-STE] Delete the branch with the old migration.
- [STE] Delete the branch that contains the previous version of the migration.
- [Non-STE] Benchmark the endpoint with caching.
- [STE] Enable the cache. Then do the performance test of the endpoint.
- [Non-STE] Use `git revert` to undo the commit.
- [STE] Revert the commit with `git revert`.

## Review notes

- A check can find each “with,” but most of them are correct. The reviewer must read each sentence and find the sentences that can have two meanings.
- A check cannot know which meaning the writer wants. Only the writer, or a reviewer who knows the task, can select the correct meaning.
- An automatic replacement of “with” by “that has” changes the meaning when “with” shows a tool. “Revert the commit that has `git revert`” is incorrect.
