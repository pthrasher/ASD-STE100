---
title: "Rule 1.8"
rule: "1.8"
section: "Section 1 – Words"
topic: "Technical nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-08.md"
status: adapted
mechanical-check: none
---

# Rule 1.8 – Technical nouns

> **Rule 1.8** **Use technical nouns that are approved in your company, industry, or subject field.**

Source: [Issue 9, Rule 1.8](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-08.md) gives the full text and the original example.

## In software text

The profile uses this rule to select software terms that are different from the terms of Issue 9. The primary decision is [bug (TN)](../../dictionary/nouns.md#bug-tn). Issue 9 uses DEFECT (TN) for items that are not software. In software text, use “bug,” because it is the term of the software industry. Do not use the two terms for the same item.

The terms of the software industry are in the documentation of standards, programming languages, and tools, for example “pull request,” “stack trace,” and “merge conflict.” Use these terms. Do not make a new term that only your text uses. [nouns.md](../../dictionary/nouns.md) gives the terms that the profile selects.

The code of a project also has approved terms: the names of its classes, modules, and data. If the code has the name `Workspace` for an item, use the term “workspace” in the text. Do not use “project” or “folder” for it. This is important for [agent instructions](../../text-types/agent-instructions.md) and [error messages](../../text-types/error-messages.md): the reader must find the item in the code or on the screen with the same term.

## Examples

- [Non-STE] This commit corrects a defect in the date parser.
- [STE] This commit corrects a bug in the date parser.
- [Non-STE] Paste the chain of function calls from the crash into the issue.
- [STE] Put the stack trace into the issue.
- [Non-STE] Open a change proposal for your branch.
- [STE] Open a pull request for your branch.
- [Non-STE] Each project can have a maximum of 10 members.
- [STE] Each workspace can have a maximum of 10 members.
  (The code and the screen use the name `Workspace` for this item.)

## Review notes

- The reviewer must know the terms of the industry and of the project. Examine the code, the documentation of the tools, and [nouns.md](../../dictionary/nouns.md).
- When two tools use different terms for the same item, the reviewer must select one. For example, one platform uses “pull request” and a different platform uses “merge request.” nouns.md gives “pull request.”
- A term of the industry must also obey [Rule 1.9](rule-1-09.md) and [Rule 1.10](rule-1-10.md). Many developers use slang terms, for example “repo.” A frequent term can be slang and not a term of the industry.
- A mechanical check cannot help. It does not know which term the industry or the project uses for an item.
