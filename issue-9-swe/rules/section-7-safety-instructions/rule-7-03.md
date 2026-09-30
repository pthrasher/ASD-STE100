---
title: "Rule 7.3"
rule: "7.3"
section: "Section 7 - Safety instructions"
topic: "How to write safety instructions"
inherits: "../../../issue-9/part-1-writing-rules/section-7-safety-instructions/rule-7-03.md"
status: adapted
mechanical-check: none
---

# Rule 7.3 – How to write safety instructions

> **Rule 7.3** **Give an explanation to show the risk or possible result.**

Source: [Issue 9, Rule 7.3](../../../issue-9/part-1-writing-rules/section-7-safety-instructions/rule-7-03.md) gives the full text and the original examples.

## In software text

The profile adds one decision. Issue 9 tells you to give the explanation “if it is possible.” In [agent instructions](../../text-types/agent-instructions.md), the explanation is mandatory. An agent uses the explanation to obey the instruction in a case that the text does not give. For example, an agent that knows the risk of the `--force` flag can find the same risk in the command `git push origin +main`.

Tell the reader the result of the risk accurately:

- the data that the step deletes, and if the step deletes it permanently
- the service or the users that the step can stop
- the persons who can see a credential, and the systems that they can then get access to
- the commits that the step can remove, and the persons who made them

If you know the quantity, give it: “all rows,” “all users in the EU region,” “the last 24 hours of data.” A general statement, for example “Data loss can occur” or “This can cause problems,” does not tell the reader how large the risk is. Issue 9 gives the same problem in its example about oxygen tubes.

## Examples

- [Non-STE] NEVER force push!!!
- [STE] CAUTION: Do not push with the `--force` flag or the `--force-with-lease` flag. These flags can remove the commits of other persons from the remote branch. If the remote repository does not accept your commits, tell the user.
  (An instruction for an agent. The second sentence gives the risk. The agent can use the risk to find other commands that remove commits.)
- [Non-STE] Don't print secrets.
- [STE] CAUTION: Do not write the values of credentials in log messages or in command output. All persons who can read the log can then use the credentials to get access to the production systems.
- [Non-STE] CAUTION: Run this in staging only.
- [STE] CAUTION: Execute this command only in the test environment. In the production environment, it deletes the data of all users permanently. The last backup does not contain the data that users added after it.
- [Non-STE] CAUTION: Deleting this bucket may have consequences.
- [STE] CAUTION: Do not delete the `assets-prod` bucket. It contains all images of the website. If you delete it, the website shows no images until you upload all the images again.

## Review notes

- The reviewer must make sure that the explanation tells an accurate and specified result. Only a person or an agent who knows the system can tell if the result is correct, and if the explanation gives all of the risk.
- A mechanical check cannot tell if a sentence is an explanation of a risk. A count of the sentences in a safety instruction does not help, because the second sentence can be a second command.
- In agent instructions, examine each “Do not” instruction that has no explanation. If there is a risk, the instruction must be a safety instruction with an explanation.
