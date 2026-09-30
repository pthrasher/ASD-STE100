---
title: "Text-type guides"
kind: guidance
---

# Text-type guides

Each guide in this directory tells you how to use the rules of this profile for one type of software text. A guide gives the structure of the text, the rules that are most important for it, examples, and questions for a reviewer. A guide does not give the full rules. Each guide gives links to the rule pages.

| Guide | Type of text | STE text type |
|---|---|---|
| [commit-messages.md](commit-messages.md) | Commit messages | Descriptive |
| [pull-requests.md](pull-requests.md) | Pull request descriptions | Descriptive and procedural |
| [error-messages.md](error-messages.md) | Error messages | Descriptive and procedural |
| [log-messages.md](log-messages.md) | Log messages | Descriptive |
| [api-reference.md](api-reference.md) | API reference documentation and docstrings | Descriptive and procedural |
| [code-comments.md](code-comments.md) | Code comments | Descriptive |
| [agent-instructions.md](agent-instructions.md) | Instructions for AI agents, for example `CLAUDE.md` or `AGENTS.md` | Procedural |

[../SCOPE.md](../SCOPE.md) gives the types of text that are in the scope of this profile, and the types that are not in its scope. READMEs, runbooks, and installation procedures are in the scope, but they do not have a guide. For these texts, use Section 5, Section 6, and Section 7 directly.

## How to use these guides for a writing task

Before you write or change one of these types of text, read these files in this sequence:

1. The guide for the type of text.
2. The rule pages in the “Rules that matter most” section of the guide.
3. [../dictionary/README.md](../dictionary/README.md). Use its procedure to find each word that you are not sure about.

If the guide and a rule page do not agree, obey the rule page. If the type of text is not in the table, use the test in [../SCOPE.md](../SCOPE.md#the-test).

The review questions in each guide are for a person or an agent who reads the text. A mechanical check cannot make these decisions. [../review/LIMITS.md](../review/LIMITS.md) gives the causes.
