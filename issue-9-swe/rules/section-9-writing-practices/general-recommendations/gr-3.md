---
title: "GR-3 How to use pronouns"
gr: "GR-3"
section: "Section 9 - Writing practices"
topic: "General recommendations"
inherits: "../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-3.md"
status: unchanged
mechanical-check: none
---

# GR-3 How to use pronouns

This recommendation tells you to use only the pronouns of the dictionary, and to make sure that each pronoun refers to only one noun.

Source: [Issue 9, GR-3](../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-3.md) gives the full text and the original examples.

## In software text

Software text frequently has two or more items in one sentence: a client and a server, a branch and a commit, a file and a function. Then “it” or “they” can refer to more than one of them. Write the noun again.

In agent instructions, a clear pronoun is very important. The instruction “Read the configuration and the schema, and update it” can refer to two files. The agent must select one file, and it can update the incorrect file. Write the name of the file.

Do not use “he” or “she” for a user, a developer, or a reviewer. These pronouns are not in the dictionary ([GR-7](gr-7.md)). Write the noun again, for example “the user.”

## Examples

- [Non-STE] If the client sends a request to the server and it doesn't respond in 30s, it closes the connection.
- [STE] If the server does not send a response in 30 seconds, the client closes the connection.
- [Non-STE] Read the config and the schema, and update it if it's out of date.
- [STE] Read `config.yaml` and `schema.json`. If `schema.json` does not agree with `config.yaml`, update `schema.json`.
- [Non-STE] When a user resets his password, he gets a confirmation email.
- [STE] When a user sets a new password, the service sends an e-mail to the user.

## Review notes

- A check can find pronouns that are not in the dictionary, for example “he,” “she,” and “whose.” It cannot know if an approved pronoun, for example “it,” refers to one noun or to two.
- The reviewer must find the noun for each “it,” “they,” and “them.” If the reviewer finds two possible nouns, the pronoun is not clear.
- A pronoun in a code comment can refer to a variable or to a value. Make sure that the reader can find the item, or write its name in code format.
