---
title: "Rule 1.9"
rule: "1.9"
section: "Section 1 – Words"
topic: "Technical nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-09.md"
status: unchanged
mechanical-check: none
---

# Rule 1.9 – Technical nouns

> **Rule 1.9** **When you must select a technical noun, use one which is short and easy to understand.**

Source: [Issue 9, Rule 1.9](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-09.md) gives the full text and the original example.

## In software text

The names of software items frequently become long, because each word adds a condition: “the asynchronous background job queue retry handler.” First, look for a term of the industry or the project ([Rule 1.8](rule-1-08.md)). If there is no term, select a term of a maximum of three words. [Rule 2.1](../section-2-multi-word-nouns/rule-2-01.md) gives the same limit for multi-word nouns.

If the item has a name in the code, you can write the name in code format. A code span counts as one word ([Rule 10.2](../section-10-code-in-text/rule-10-02.md)). In [agent instructions](../../text-types/agent-instructions.md), the name in the code is frequently the best term, because the agent can find it in the repository.

A short term is correct only if the reader can identify the item. If a system has two caches, “the cache” is not sufficient. Add one or two words: “the session cache.”

## Examples

- [Non-STE] Restart the distributed in-memory key-value cache cluster.
- [STE] Start the cache cluster again.
- [Non-STE] The asynchronous background task processing queue retries failed tasks three times.
- [STE] If a task stops before its end, the task queue tries it again a maximum of three times.
- [Non-STE] Update the user notification preference settings configuration object.
- [STE] Update the `NotificationSettings` object.

## Review notes

- The reviewer must find if the reader can identify the item from the short term. If the text has two items with the same short term, the term is not sufficient.
- A short term must not change the meaning. If you remove “distributed” from “distributed lock,” the reader can think that it is a lock in one process.
- A mechanical check cannot help. A check can count the words in a noun cluster ([Rule 2.1](../section-2-multi-word-nouns/rule-2-01.md)). It cannot tell if a shorter term is clear, or if a long term is the term of the industry.
