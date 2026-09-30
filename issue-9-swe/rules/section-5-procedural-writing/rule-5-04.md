---
title: "Rule 5.4"
rule: "5.4"
section: "Section 5 - Procedural writing"
topic: "Descriptive statements in instructions"
inherits: "../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-04.md"
status: unchanged
mechanical-check: none
---

# Rule 5.4 – Descriptive statements in instructions

> **Rule 5.4** **When there is a condition that the reader must know about first, start the instruction with a descriptive statement. Then, divide that descriptive statement from the command with a comma.**

Source: [Issue 9, Rule 5.4](../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-04.md) gives the full text and the original examples.

## In software text

Put the condition first, then a comma, then the command. This is applicable to runbooks, to the instruction in an [error message](../../text-types/error-messages.md), and to [agent instructions](../../text-types/agent-instructions.md).

- **Runbooks.** A reader who does an incident procedure reads quickly. If the condition is at the end of the sentence, the reader can execute the command before the reader reads the condition.
- **Agent instructions.** An agent must know the condition before the instruction. If a condition is at the end of a long sentence, it is not clear which part of the sentence the condition is applicable to. Examples of conditions are the environment, the branch, and the result of a previous command.
- **Error messages.** Give the condition first when the next step is different for different causes: “If you use a proxy, set `HTTPS_PROXY`.”

## Examples

- [Non-STE] Stop the deployment if the migration shows an error.
- [STE] If the migration shows an error, stop the deployment.
- [Non-STE] Delete the old branch once the PR is merged.
- [STE] After you merge the pull request, delete the branch.
- [Non-STE] Roll back the deployment if the error rate goes above 5% in the first 10 minutes.
- [STE] If the error rate is more than 5% during the first 10 minutes, roll back the deployment.
- [Non-STE] Ask the user for confirmation before running anything destructive like `rm -rf` or `DROP TABLE`.
- [STE] If a command can delete data, do not execute it without the approval of the user.

## Review notes

- The reviewer must find each condition that the reader must know before the step. A condition does not always start with “if” or “when.” It can be a phrase, for example “in the production environment” or “on the `main` branch.”
- Examine the position of each comma. Issue 9 shows that a comma in a different position can change the instruction.
- A mechanical check cannot tell if a clause is a condition that the reader must know first. A clause that starts with “if” or “when” after the command can be correct, for example in a descriptive sentence. Only a reader who knows the task can identify the conditions.
