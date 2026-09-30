---
title: "Rule 3.1"
rule: "3.1"
section: "Section 3 - Verbs"
topic: "Verb forms and tenses of verbs"
inherits: "../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-01.md"
status: adapted
mechanical-check: suggests
---

# Rule 3.1 – Verb forms and tenses of verbs

> **Rule 3.1** **Use only the verb forms that are given in the dictionary.**

Source: [Issue 9, Rule 3.1](../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-01.md) gives the full text and the original examples.

## In software text

The profile adds one decision. [verbs.md](../../dictionary/verbs.md) gives technical verbs, but it does not give their forms. For a technical verb, use its standard English forms: commit, commits, committed; build, builds, built; rebase, rebases, rebased. [Rule 3.2](rule-3-02.md) and [Rule 3.5](rule-3-05.md) limit the forms that you can use.

For an approved verb, use only the forms that the [Issue 9 dictionary](../../../issue-9/part-2-dictionary/index.md) gives. For example, SET has the forms SETS, SET, SET.

Software text frequently uses a noun, a command name, or an HTTP status code as a verb. These words have no verb forms in a dictionary:

- A noun as a verb: “The script errors out,” “Setup the environment.” Refer to [Rule 1.7](../section-1-words/rule-1-07.md).
- A command name as a verb: “grep the log,” “curl the endpoint.” Put the command in code format, and use an approved verb: “Find the request ID with `grep`.” Refer to [Rule 10.4](../section-10-code-in-text/rule-10-04.md).
- Jargon verbs: “The endpoint 404s,” “The worker was OOM-killed,” “Bump the version.”

In agent instructions, a jargon verb is possibly not clear to the agent. Use a verb from the dictionaries. Refer to [agent instructions](../../text-types/agent-instructions.md).

## Examples

- [Non-STE] Setup the environment variables before you start the service.
- [STE] Set the environment variables before you start the service.
  (“Setup” is a noun. It is not a form of the verb SET.)
- [Non-STE] Grep the access log for the request ID.
- [STE] Find the request ID in the access log with `grep`.
- [Non-STE] If the endpoint 404s, the client errors out.
- [STE] If the endpoint returns status code `404`, the client shows an error and stops.
- [Non-STE] Bump the version and cut a release.
- [STE] Increase the version number. Then release the new version.

## Review notes

- The reviewer must find the part of speech of each word in its sentence. In software text, many words are nouns and verbs, for example “log,” “error,” “test,” and “build.” In “The build logs errors,” “logs” is a verb, and log (v) is not approved.
- A mechanical check can compare each word with the forms in the Issue 9 dictionary. It incorrectly shows a problem for the forms of technical verbs, for example “rebased” and “committed,” because the profile does not give these forms.
- A check finds “setup,” because “setup” is not in the dictionary. But a check that examines one word at a time does not find “set up.” The two words make a phrasal verb ([Rule 9.3](../section-9-writing-practices/rule-9-03.md)). SET and UP are approved words.
- A check that gives an alternative for a verb can cause a new error. “Errors out” becomes “error out” or “errors” with no change to the construction. A new sentence construction is necessary ([Rule 9.1](../section-9-writing-practices/rule-9-01.md)).
