---
title: "Rule 6.1"
rule: "6.1"
section: "Section 6 - Descriptive writing"
topic: "Content structure"
inherits: "../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-01.md"
status: adapted
mechanical-check: none
---

# Rule 6.1 – Content structure

> **Rule 6.1** **Give information gradually.**

Source: [Issue 9, Rule 6.1](../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-01.md) gives the full text and the original examples.

## In software text

The profile adds a sequence of information for each type of software text. Give the most important information first. Then give the information that the reader must have to use it. Issue 9 also tells you to make sure that each sentence contains only one subject.

| Type of text | Sequence |
|---|---|
| [Commit message](../../text-types/commit-messages.md) body, [pull request](../../text-types/pull-requests.md) description | 1. The change. 2. The cause of the change, for example the problem that it corrects. 3. More information: limits, tests, related issues. |
| [Error message](../../text-types/error-messages.md) | 1. The problem. 2. The cause, if the program knows it. 3. The next step for the reader. |
| [Log message](../../text-types/log-messages.md) | 1. The operation, the change of condition, or the error. 2. The data that identifies the item, for example an ID or a path. |
| [API reference](../../text-types/api-reference.md), docstring | 1. The result of the function or the endpoint. 2. The parameters. 3. The errors and the exceptions. |

A reader who stops after the first sentence must know the most important information. This is frequently true for a person who reads a list of commits, and for an agent that reads the first part of a long file.

## Examples

- [Non-STE] Because the upload client didn't retry on 503s from the storage gateway, which started rate-limiting us after the March config change, nightly exports were silently dropped, so this adds exponential backoff with jitter (max 5 attempts).
- [STE] This commit changes the upload client. When the storage gateway sends status `503`, the client tries the request again.<br>
  Before this change, the client stopped after the first `503` response. As a result, the client did not upload some of the export files each night, and the client recorded no error. The storage gateway sends `503` when a client sends too many requests.<br>
  The client tries the request again a maximum of five times. The time between two requests increases after each request.
  (Paragraph 1 gives the change. Paragraph 2 gives the cause. Paragraph 3 gives more information.)
- [Non-STE] Returns users, paginated, filtered by the optional `role` param (defaults to all roles) and sorted by `created_at` unless `sort` is given.
- [STE] The `GET /users` endpoint returns a list of users. Each response contains a maximum of 100 users. If you give the `role` parameter, the list contains only the users that have that role. If you do not give the `sort` parameter, the list is in the sequence of `created_at`.

## Review notes

- The reviewer must read the first sentence of the text alone, and make sure that it gives the most important information. A mechanical check cannot know which information is the most important.
- The reviewer must make sure that each sentence has one subject. A check can count clauses, but it cannot tell if two clauses are about one subject.
- A text can obey all the other rules and give the information in an incorrect sequence. For example, a commit body can start with the history of a bug and give the change in its last sentence. Only a reader can find this problem.
