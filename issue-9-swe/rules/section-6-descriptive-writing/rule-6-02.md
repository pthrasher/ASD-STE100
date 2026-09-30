---
title: "Rule 6.2"
rule: "6.2"
section: "Section 6 - Descriptive writing"
topic: "Content structure"
inherits: "../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-02.md"
status: unchanged
mechanical-check: none
---

# Rule 6.2 – Content structure

> **Rule 6.2** **Use key words and key phrases to give your text a logical structure.**

Source: [Issue 9, Rule 6.2](../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-02.md) gives the full text and the original examples.

## In software text

In software text, the key words are usually the technical nouns and the identifiers of the text: the name of the service, the function, the endpoint, or the configuration value. Use the same key word each time that you refer to the same item. Use the term that [nouns.md](../../dictionary/nouns.md) gives, and do not use the terms in its “Do not use” field ([Rule 1.11](../section-1-words/rule-1-11.md)).

A different term tells the reader that there is a different item. If a pull request description uses “the job,” “the task,” and “the work item” for one item, a reader and an agent can think that there are three items.

If an identifier is a key word, write it in code format each time, and do not change it. Do not write `retry_limit` in one sentence and “the retry setting” in the next sentence.

Use connecting words to show how the sentences are related: “and,” “but,” “then,” “thus,” “as a result,” and “at the same time” ([Rule 4.4](../section-4-sentences/rule-4-04.md)). Do not use “however,” “therefore,” or “moreover.” They are not approved.

## Examples

- [Non-STE] The worker picks up jobs from the queue. Each task is retried three times. If the job runner crashes, pending work is lost.
- [STE] The worker gets tasks from the queue. If the worker cannot complete a task, the worker tries the task again three times. If the worker stops suddenly, the queue does not keep the tasks that the worker did not complete.
  (“Worker” and “task” are the key words. The Non-STE text uses three terms for the task and two terms for the worker.)
- [Non-STE] The cache is invalidated on each deploy; however, the CDN keeps stale copies for 60 s.
- [STE] Each deployment removes all data from the cache. But the CDN keeps its copies of the pages for 60 seconds after the deployment.
- [Non-STE] Set `max_connections` in the config. Raising the connection cap above 100 can exhaust the pool.
- [STE] Set `max_connections` in `config/db.yaml`. If `max_connections` is more than 100, the pool can have no free connections.

## Review notes

- The reviewer must find the key words of the text, and make sure that each key word is the same in all of the text. A mechanical check cannot know that “the job,” “the task,” and “the runner” refer to the same item ([LIMITS.md](../../review/LIMITS.md)).
- A check can compare the text with the “Do not use” terms in [nouns.md](../../dictionary/nouns.md). That is a check for Rule 1.11. It does not find a different term that the list does not contain, or a key phrase that changes from one sentence to the next.
- The reviewer must make sure that each connecting word gives the correct relation. If “but” connects two sentences that do not give opposite information, it is an error. No check can find this error.
