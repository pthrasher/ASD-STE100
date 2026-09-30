---
title: "Rule 6.4"
rule: "6.4"
section: "Section 6 - Descriptive writing"
topic: "Paragraphs"
inherits: "../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-04.md"
status: unchanged
mechanical-check: none
---

# Rule 6.4 – Paragraphs

> **Rule 6.4** **Use paragraphs to show related information.**

Source: [Issue 9, Rule 6.4](../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-04.md) gives the full text and the original examples.

## In software text

Start each paragraph with a topic sentence. The topic sentence tells the reader the topic of the paragraph. The sentences after it give more information about that topic.

- **Commit messages and pull requests.** Put the change, the cause, and the other information in different paragraphs ([Rule 6.1](rule-6-01.md)). A reader who reads only the first sentence of each paragraph must know the structure of the change. Refer to [commit messages](../../text-types/commit-messages.md) and [pull requests](../../text-types/pull-requests.md).
- **Code comments and docstrings.** A long comment block also has paragraphs. Put a blank comment line between two paragraphs. Refer to [code comments](../../text-types/code-comments.md).
- **API reference.** Put the information about each parameter or each error in its own paragraph or list item. Refer to [API reference](../../text-types/api-reference.md).

In Markdown and in commit messages, a blank line starts a new paragraph. A new line without a blank line does not start a paragraph. Many commit messages start a new line after 72 characters. These new lines do not divide the text into paragraphs.

## Examples

- [Non-STE] Moves rate limiting from the API gateway into the service. The gateway limit was global so one noisy tenant could block everyone. Also bumped the Redis client to 5.x since the old one didn't support Lua scripts. Limits are now per-tenant and configurable in `limits.yaml`.
- [STE] This commit moves the rate limit from the API gateway into the service. The service uses a different limit for each tenant. The limits are in `limits.yaml`.<br>
  <br>
  Before this change, the gateway used one limit for all tenants. Thus, when one tenant sent too many requests, the gateway stopped the requests of all tenants.<br>
  <br>
  This commit also updates the Redis client to version 5. The rate limit uses Lua scripts, and version 4 of the client cannot send Lua scripts.
  (Three paragraphs: the change, the cause, and a related change. The first sentence of each paragraph gives its topic.)

## Review notes

- The reviewer must find the topic sentence of each paragraph, and make sure that it is the first sentence. A mechanical check cannot tell which sentence gives the topic.
- A check can find paragraphs, but only from blank lines. It cannot see the paragraphs in a code comment that has no blank comment lines, or in a log message.
- The reviewer must make sure that the information in each paragraph is related. Only a reader who knows the subject can see if two sentences are related.
