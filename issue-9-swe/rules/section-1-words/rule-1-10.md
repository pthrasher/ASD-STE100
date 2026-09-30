---
title: "Rule 1.10"
rule: "1.10"
section: "Section 1 – Words"
topic: "Technical nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-10.md"
status: adapted
mechanical-check: suggests
---

# Rule 1.10 – Technical nouns

> **Rule 1.10** **Do not use regional, slang, or jargon words as technical nouns.**

Source: [Issue 9, Rule 1.10](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-10.md) gives the full text and the original examples.

## In software text

The profile gives short forms and slang words that you must not use as technical nouns. They are in the “Do not use” field of the entries in [nouns.md](../../dictionary/nouns.md), for example “repo,” “config,” “creds,” “dep,” and “prod.” Some entries let you use a short form if the text gives its meaning first, for example “PR” for “pull request.”

The profile uses this test to find the difference between a term of the industry ([Rule 1.8](rule-1-08.md)) and jargon: the documentation of a standard, a programming language, or a tool uses a term of the industry. “Deployment” and “stack trace” are terms of the industry. “Prod” and “repo” are jargon.

Software text has much slang. Examples are nouns such as “deps,” “creds,” and “yak shaving,” and verbs such as “nuke,” “bump,” “ship,” and “spin up.” Many readers of software text do not have English as their first language. An agent can think that a slang word has its usual English meaning.

The names of internal tools and the code names of projects are also jargon, if only one team knows them. The first time that the text uses the name, write the type of the item after it, for example “Relay (the deployment tool).”

## Examples

- [Non-STE] Nuke `node_modules` and reinstall.
- [STE] Delete the `node_modules` directory. Then install the dependencies again.
- [Non-STE] Bump the dep to 2.4.
- [STE] Upgrade the `requests` package to version 2.4.
- [Non-STE] Don't ship config changes to prod on Fridays.
- [STE] Do not deploy configuration changes to the production environment on a Friday.
- [Non-STE] Spin up a local DB with Docker.
- [STE] Start a database container on your computer with Docker.

## Review notes

- The reviewer must find if a word is a term of the industry or jargon. Use the test in this page. A word can be frequent in software text and not be a term of the industry.
- A mechanical check can compare the text with the “Do not use” fields of nouns.md and with a list of slang words. It shows possible problems.
- The check shows correct text as a possible problem. “Config” in a path or an identifier that is not in code format is an example. The correct change is code format (`config/app.yaml`), not a different word.
- The check does not find slang that is not in its list, new slang, or the code names of internal projects.
- A word-for-word replacement can change the meaning. “Ship” can have the meaning of deploy or of release. If the check replaces “ship” with SEND (v), the meaning is incorrect ([Rule 9.1](../section-9-writing-practices/rule-9-01.md)).
