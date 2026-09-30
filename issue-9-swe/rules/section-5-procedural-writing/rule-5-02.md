---
title: "Rule 5.2"
rule: "5.2"
section: "Section 5 - Procedural writing"
topic: "Sentences"
inherits: "../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-02.md"
status: adapted
mechanical-check: none
---

# Rule 5.2 – Sentences

> **Rule 5.2** **Write only one instruction in each sentence unless two or more actions occur at the same time.**

Source: [Issue 9, Rule 5.2](../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-02.md) gives the full text and the original examples.

## In software text

The profile adds one decision for commands. A code block after an instruction can contain more than one command only if the reader executes all the commands as one step. If the reader must examine the output of a command before the next command, put each command in a different step ([Rule 10.3](../section-10-code-in-text/rule-10-03.md)).

Give each step a number when the sequence is important. This is applicable to README installation steps, runbooks, and the test steps of a [pull request](../../text-types/pull-requests.md).

In [agent instructions](../../text-types/agent-instructions.md), write one instruction in each list item. If a list item contains two instructions, an agent can do the first instruction and not do the second.

In software text, two actions that occur at the same time are usually in a user interface, for example when you hold a key and click. You can also write two sentences in one step when the second sentence gives the result or the limit of the first (Issue 9 gives this case).

## Examples

- [Non-STE] Pull the latest changes, install deps and spin up the dev server.
- [STE] 1. Pull the `main` branch.<br>
  2. Install the dependencies.<br>
  3. Start the development server.
- [Non-STE] Update the changelog, bump the version in pyproject.toml and tag the release.
- [STE] 1. Add an entry for the change to `CHANGELOG.md`.<br>
  2. Increase the version number in `pyproject.toml`.<br>
  3. Make a Git tag for the release.
- [STE] Hold `Ctrl` and click the link.
  (The two actions occur at the same time. Thus, one sentence is correct.)
- [STE] 4. Execute this command:

  ```sh
  make test
  ```

  The output must show `0 failed`.
  (The last sentence gives the limit for the result of the step. It is part of step 4.)

## Review notes

- The reviewer must make sure that two actions in one sentence occur at the same time. A mechanical check cannot know the sequence of actions in a task.
- The word “and” between two verbs is an area to examine. But “and” also connects two objects of one verb (“Stop the service and the worker.”). A check cannot tell if a word, for example “test,” “build,” or “log,” is a verb or a noun. Thus, a count of verbs does not help.
- Examine each code block. A chain of commands with `&&` or `;` is one step only if the reader does not examine a result between the commands. A check cannot know if the reader must examine a result.
- An instruction can be in a table cell, in a YAML comment, or in the text of an error message. The reviewer must find these instructions and examine them.
