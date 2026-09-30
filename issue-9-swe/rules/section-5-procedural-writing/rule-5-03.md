---
title: "Rule 5.3"
rule: "5.3"
section: "Section 5 - Procedural writing"
topic: "Verbs in procedures"
inherits: "../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-03.md"
status: adapted
mechanical-check: none
---

# Rule 5.3 – Verbs in procedures

> **Rule 5.3** **Write instructions in the imperative (command) form.**

Source: [Issue 9, Rule 5.3](../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-03.md) gives the full text and the original examples.

## In software text

The profile adds two decisions:

1. **Commit subjects and docstrings.** The subject line of a commit message and the first line of a docstring use the imperative: “Correct the date parser,” “Return the user that has the given ID.” The remaining text of the commit message or the docstring is descriptive text ([Section 6](../section-6-descriptive-writing/README.md)). Refer to [commit messages](../../text-types/commit-messages.md) and [code comments](../../text-types/code-comments.md).
2. **MUST in agent instructions.** Use the imperative for an instruction: “Do not push to the `main` branch.” Do not write “you must” before the imperative. Issue 9 lets you write “must” before the imperative only for an instruction that is very important for safety, or for an important condition. You can also use MUST for a limit or a condition of an item, for example “The commit subject must have a maximum of 50 characters.” That sentence is not an instruction to the reader.

For a permission, use CAN: “You can change the files in `docs/`.” Do not use “should” or “may.” The agent cannot know if the instruction is mandatory ([should](../../dictionary/verbs.md#should-v), [may](../../dictionary/verbs.md#may-v)).

Do not give an instruction as information about the team, for example “We prefer small commits.” An agent can read this sentence as information only. Write the instruction: “Put only one change in each commit.”

If a file contains instructions for persons and for agents, start the instructions for agents with a condition: “If you are an agent, …” ([Rule 5.4](rule-5-04.md)).

## Examples

- [Non-STE] Tests should be run before pushing.
- [STE] Execute the tests before you push your branch.
- [Non-STE] Added retry logic to the upload client
- [STE] Send the file again after a timeout
  (A commit subject. The profile uses the imperative for commit subjects.)
- [Non-STE] It is recommended that generated files are not edited by hand.
- [STE] Do not change the files in the `gen/` directory. A script makes these files.
- [Non-STE] Before you deploy the release, you must run the migrations.
- [STE] Before you deploy the release, execute the migration script.
- [Non-STE] We generally prefer that agents avoid adding new dependencies.
- [STE] Do not add a dependency without the approval of the user.
  (The Non-STE text does not tell the agent if the instruction is mandatory. Before the writer changes the text, the writer must make a decision.)

## Review notes

- The reviewer must find each sentence that has the function of an instruction, and then make sure that it uses the imperative. Only a reader who knows the function of the text can find these sentences. “The tests are run before merge” can be information about the pipeline or an instruction to the reader.
- In agent instructions, the reviewer must make sure that each “must” is necessary. It is correct in an instruction that is very important for safety, for an important condition, and for the limit of an item.
- A mechanical check can find words that are not approved, for example “should,” “please,” or “is to be.” That is a check for [Rule 1.1](../section-1-words/rule-1-01.md). It cannot tell if a sentence is an instruction. It cannot tell if the first word of a sentence is a verb in the imperative or a noun (“Test results are in `out/`” and “Test the parser”).
- A commit subject in the imperative is not an error in descriptive text. It is a decision of this profile.
