---
title: "Rule 7.2"
rule: "7.2"
section: "Section 7 - Safety instructions"
topic: "How to write safety instructions"
inherits: "../../../issue-9/part-1-writing-rules/section-7-safety-instructions/rule-7-02.md"
status: adapted
mechanical-check: none
---

# Rule 7.2 – How to write safety instructions

> **Rule 7.2** **Start a safety instruction with a clear and accurate command or condition.**

Source: [Issue 9, Rule 7.2](../../../issue-9/part-1-writing-rules/section-7-safety-instructions/rule-7-02.md) gives the full text and the original examples.

## In software text

The profile adds one decision. Put the safety instruction immediately before the step or the command that has the risk. Do not put it after the command, or at the end of a README. A person or an agent can execute a command before they read the text after it.

Start the safety instruction with a command or with a condition:

- A command tells the reader a step that they must not do, or a step that they must do first: “Do not push with the `--force` flag to the `main` branch.”
- A condition tells the reader when the risk occurs: “Before you deploy to the production environment, …” or “If the migration shows an error, …” ([Rule 5.4](../section-5-procedural-writing/rule-5-04.md)).

The command must be accurate. “Be careful” does not tell the reader which step to do or not to do. Give the environment, the branch, the table, or the command that the instruction is applicable to.

In [agent instructions](../../text-types/agent-instructions.md), put the safety instructions in the part of the file that the agent reads before the tasks. Also put each safety instruction again directly before the step that it is applicable to.

## Examples

- [Non-STE] CAUTION: Force-pushing rewrites history. Don't do it on shared branches.
- [STE] CAUTION: Do not push with the `--force` flag to a branch that other persons use. This flag can remove their commits from the remote branch.
- [Non-STE] CAUTION: This migration can't be rolled back, so take a snapshot first if you're on prod.
- [STE] CAUTION: Before you execute this migration in the production environment, make a backup of the database. You cannot roll back this migration.
- [Non-STE] Be careful with the prod database.
- [STE] CAUTION: Do not change data in the production database. Changes to this database are permanent, and users see them immediately.
- [STE] WARNING: While you install the firmware on the pump controller, do not disconnect the power supply of the controller. The pump can stop, and patients can get an incorrect dose.
  (The command follows a condition. The risk is to persons. Thus, the word is WARNING.)

## Review notes

- The reviewer must make sure that the first sentence is a command or a condition, and that it is accurate. “Be careful,” “Use caution,” and “This is dangerous” are not accurate commands. A mechanical check cannot tell if a sentence is accurate.
- The reviewer must make sure that each safety instruction is before the step that has the risk. A check cannot know which step has the risk.
- Examine each safety instruction in agent instructions for a command that is not clear to an agent. For example, “Do not change production” does not tell the agent if it can read production data.
