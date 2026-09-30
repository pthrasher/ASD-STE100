---
title: "Rule 7.1"
rule: "7.1"
section: "Section 7 - Safety instructions"
topic: "How to write safety instructions"
inherits: "../../../issue-9/part-1-writing-rules/section-7-safety-instructions/rule-7-01.md"
status: adapted
mechanical-check: suggests
---

# Rule 7.1 – How to write safety instructions

> **Rule 7.1** **Use an applicable word (for example, “warning” or “caution”) to identify the level of risk.**

Source: [Issue 9, Rule 7.1](../../../issue-9/part-1-writing-rules/section-7-safety-instructions/rule-7-01.md) gives the full text and the original examples.

## In software text

The profile adds three decisions: the level of risk for each word, the format of a safety instruction, and the words that are not safety words.

**1. The level of risk.** The profile keeps the two words of Issue 9 and the level of risk of each word. Issue 9 tells you that a caution is for a risk of damage to objects. In this profile, data, software, and computer systems are also objects.

| Word | Use it when | Examples in software |
|---|---|---|
| WARNING | There is a risk of injury or death. If there are the two levels of risk together, use WARNING. | Software that controls machines, vehicles, medical devices, or alarm systems. A change that can stop an emergency service. |
| CAUTION | There is a risk of damage to objects. In this profile, data, software, and computer systems are also objects. | A command that deletes data permanently. `git push --force` on a branch that other persons use. A change to the production environment. A migration that you cannot roll back. A step that can show credentials to persons who must not see them. |

The profile does not add a third word. A CAUTION for a small risk and a CAUTION for a very large risk use the same word. The explanation tells the reader how large the risk is ([Rule 7.3](rule-7-03.md)). Issue 9 lets you use different words, for example DANGER or NOTICE. If you use them, the safety instructions must obey Rules 7.1 to 7.3.

**2. The format.** STE gives no rules for format. Write the word in uppercase letters, with a colon: `WARNING:` or `CAUTION:`. Do not write the remaining text in uppercase letters. A command, a path, or an identifier in uppercase letters is a different command, path, or identifier. In GitHub Markdown, you can use the alerts `> [!WARNING]` and `> [!CAUTION]`. Use them for the levels of risk in the table. Do not use the levels that the GitHub documentation gives.

**3. Words that are not safety words.** The log levels `WARN`, `WARNING`, `ERROR`, and `CRITICAL` identify the log level of a log message. A log message is not a safety instruction, and Section 7 is not applicable to it ([log messages](../../text-types/log-messages.md)). A warning from a compiler or a linter is also not a safety instruction. Do not write “Warning:” or “Caution:” before information that has no risk. Write a note ([Rule 5.5](../section-5-procedural-writing/rule-5-05.md)) or a step. But if a program shows a prompt before it deletes data, the text of the prompt is a safety instruction.

## Examples

- [Non-STE] Warning: be careful with this command!
- [STE] CAUTION: Before you execute this command, make sure that `DATABASE_URL` identifies the test database. In the production database, this command deletes the `orders` table and all its data permanently.
- [Non-STE] CAUTION: The robot arm moves during calibration.
- [STE] WARNING: Before you execute the calibration script, make sure that no persons are near the robot arm. The arm moves during the calibration and can cause injury.
  (The Non-STE text uses CAUTION, but the risk is injury. Thus, the correct word is WARNING.)
- [Non-STE] `> [!WARNING]` This tool is experimental.
- [STE] NOTE: The commands of this tool can change in a subsequent version.
  (There is no risk of injury and no risk of damage. Thus, this text is a note, not a safety instruction.)
- [Neutral] `WARNING disk usage at 91% on /var`
  (A log message at the level `WARNING`. It is not a safety instruction. Refer to [log messages](../../text-types/log-messages.md).)

## Review notes

- The reviewer must do a risk analysis for each step. Find the result if the reader does the step incorrectly, or in the incorrect environment. Then identify the risk: injury or death (WARNING), damage to objects, for example data, software, or computer systems (CAUTION), or no risk (no safety word). A mechanical check cannot do a risk analysis.
- A mechanical check can show areas to examine:
  - a code block that contains a command that can delete data, and that has no WARNING or CAUTION before it, for example `DROP TABLE`, `TRUNCATE`, `rm -rf`, `git push --force`, `git reset --hard`, `terraform destroy`, or `kubectl delete`
  - each “Warning:” or “Caution:” in prose, to make sure that there is a risk
- Where the check gives incorrect results:
  - It does not find a risk in a command that is not in its list, for example `./scripts/reset.sh`, or in a step that has no command, for example “Change the DNS record.”
  - It shows commands that have no risk, for example `rm -rf build/` for files that the build makes again.
  - It cannot know the environment. The same command can have no risk in a test environment and a large risk in the production environment.
  - It shows log levels and compiler output that contain the word `WARNING`.
- A CAUTION or a WARNING before a command does not show that the level is correct. The reviewer must examine the level.
