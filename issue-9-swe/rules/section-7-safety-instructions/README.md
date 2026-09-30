---
title: "Section 7 - Safety instructions"
section: "Section 7 - Safety instructions"
inherits: "../../../issue-9/part-1-writing-rules/section-7-safety-instructions/README.md"
---

# Section 7 - Safety instructions

Source: [Issue 9, Section 7 - Safety instructions](../../../issue-9/part-1-writing-rules/section-7-safety-instructions/README.md) gives the full text and the original examples.

## In software text

This profile uses Section 7 for risks to persons, and for risks to data, software, and computer systems. Examples are commands that delete data permanently, for example `DROP TABLE` or a command that deletes a storage bucket. Other examples are `git push --force`, changes to the production environment, text that can show credentials to other persons, and migrations that you cannot roll back. Issue 9 uses WARNING for a risk of injury or death, and CAUTION for a risk of damage to objects. The profile keeps these two words and their levels of risk. In this profile, data, software, and computer systems are also objects. Thus, CAUTION is the word for a risk of damage to them ([Rule 7.1](rule-7-01.md)). The log levels `WARNING` and `ERROR` are not safety words, and a log message is not a safety instruction.

<!-- index:start -->
## Rules

| Rule | Statement | Status | Mechanical check |
|---|---|---|---|
| [Rule 7.1](rule-7-01.md) | Use an applicable word (for example, “warning” or “caution”) to identify the level of risk. | adapted | suggests |
| [Rule 7.2](rule-7-02.md) | Start a safety instruction with a clear and accurate command or condition. | adapted | none |
| [Rule 7.3](rule-7-03.md) | Give an explanation to show the risk or possible result. | adapted | none |
<!-- index:end -->
