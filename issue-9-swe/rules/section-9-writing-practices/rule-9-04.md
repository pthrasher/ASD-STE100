---
title: "Rule 9.4"
rule: "9.4"
section: "Section 9 - Writing practices"
topic: "Consistent style"
inherits: "../../../issue-9/part-1-writing-rules/section-9-writing-practices/rule-9-04.md"
status: adapted
mechanical-check: none
---

# Rule 9.4 – Consistent style

> **Rule 9.4** **When you select terminology or wording, always use a consistent style.**

Source: [Issue 9, Rule 9.4](../../../issue-9/part-1-writing-rules/section-9-writing-practices/rule-9-04.md) gives the full text and the original examples.

## In software text

The profile adds this decision: the text of a repository is one text for Rule 9.4. This text includes the READMEs, the runbooks, the API documentation, the commit messages, the error messages, and the agent instructions, for example `CLAUDE.md` or `AGENTS.md`. Use the same term for the same item in all of these texts. Use the same sentence for the same task each time that the task occurs.

An agent that reads the repository cannot know that two terms are for the same item. If `CLAUDE.md` tells it to “run the checks” and `CONTRIBUTING.md` tells it to “run the test suite,” the agent can think that these are two different tasks. A person who reads English as a second language has the same problem.

- Use the terms of [nouns.md](../../dictionary/nouns.md). Each entry gives one term and the terms that you must not use for the same item ([Rule 1.11](../section-1-words/rule-1-11.md)).
- If the code has a name for an item, use a term that agrees with that name. If the class is `Job`, do not call the item a “task” in the documentation.
- Write the same task with the same sentence and the same command in each file. For example, write “Execute the unit tests with `make test`.” in the README, in `CONTRIBUTING.md`, and in `CLAUDE.md`.
- Use the same structure for the same type of text. For example, all commit subjects use the imperative ([commit messages](../../text-types/commit-messages.md)), and all error messages give the error first and then the next step ([error messages](../../text-types/error-messages.md)).

## Examples

- [Non-STE] 1. Copy `config.example.yaml` to `config.yaml`.<br>
  2. Set `db_url` in the config file.<br>
  3. Start the app. It reads its settings from `config.yaml`.<br>
  4. If you change a setting, restart the server.
- [STE] 1. Copy `config.example.yaml` to `config.yaml`.<br>
  2. In the configuration file, set `db_url` to the URL of the database.<br>
  3. Start the service. The service reads its configuration from `config.yaml`.<br>
  4. If you change the configuration file, start the service again.
  (The Non-STE text uses four terms for two items: “config file” and “settings” for the configuration, and “app” and “server” for the service.)
- [Non-STE] `CLAUDE.md`: Run `make test` before committing. `CONTRIBUTING.md`: Make sure the test suite is green before you push.
- [STE] `CLAUDE.md`: Execute the unit tests with `make test` before you commit. `CONTRIBUTING.md`: Execute the unit tests with `make test` before you commit.
- [Non-STE] Commit subjects in one repository: “Fixed login redirect”, “Adds retry to uploads”, “refactoring: cache layer”.
- [STE] Commit subjects in one repository: “Correct the redirect after authentication”, “Make the upload client try a request again after an error”, “Refactor the cache code”.

## Review notes

- A check cannot know that two terms are for the same item. It cannot know that “job,” “task,” and “worker” are the same item. [LIMITS.md](../../review/LIMITS.md) gives this example.
- A check can find the terms in the “Do not use” lists of [nouns.md](../../dictionary/nouns.md), for example “repo,” “config,” and “PR.” That check is for Rule 1.11. It finds only the terms in the list, not the terms of your repository.
- A check that examines one file cannot find two files that give the same task with different words. The reviewer must read the files that the same reader uses together. For an agent, these are the agent instructions and all files that they refer to.
- When you correct one term, correct it in all files. If you change a term in the README only, the repository then has two terms for the same item.
