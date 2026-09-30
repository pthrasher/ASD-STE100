---
title: "GR-4 The pronoun “this”"
gr: "GR-4"
section: "Section 9 - Writing practices"
topic: "General recommendations"
inherits: "../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-4.md"
status: unchanged
mechanical-check: suggests
---

# GR-4 The pronoun “this”

This recommendation tells you to make sure that the reader knows the item that the pronoun “this” refers to.

Source: [Issue 9, GR-4](../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-4.md) gives the full text and the original examples.

## In software text

“This” without a noun is very frequent in commit messages, pull request descriptions, and code comments. For example: “This fixes the bug,” “This is needed because …,” “This can cause a deadlock.” The reader must then find the item: the commit, the last change in the list, the function, or the condition in the previous sentence.

Put a noun after “this”: “This commit,” “This function,” “This condition.” If the item is a condition or a result, give the condition again, as the Issue 9 examples do.

## Examples

- [Non-STE] Bump the upload timeout to 60s and add retries. This fixes the flaky upload test.
- [STE] Increase the upload timeout to 60 seconds. With the longer timeout, the upload test does not fail randomly.
- [Non-STE] Don't call `flush()` inside the loop (this slows down large imports).
- [STE] Do not call `flush()` in the loop. If you call `flush()` in the loop, the import of a large file is slow.
- [Non-STE] The cache and the queue are cleared on restart. This can cause a latency spike.
- [STE] When the service starts again, it deletes the data in the cache and in the queue. The empty cache can cause slow responses for some minutes.

## Review notes

- A check can find “this” when a verb follows it, for example “This fixes” or “This is.” These are areas to review, not errors. The reviewer must make sure that the reader knows the item.
- A check does not find “this” before a noun that does not identify the item, for example “this problem” when the text gives two problems.
- “This commit” and “this pull request” at the start of a commit body or a pull request description are clear. The reader knows the item.
