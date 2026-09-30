---
title: "Scope"
kind: specification
---

# Scope

This file tells you the types of software text that the profile is applicable to, and the types that it is not applicable to.

## The test

Issue 9 has two types of technical text: procedural text (Section 5) and descriptive text (Section 6). If a text is procedural or descriptive technical text, the profile is applicable to it. If the primary function of a text is to persuade, to tell a story, or to show the voice of a brand, the profile is not applicable to it.

## The profile is applicable to these types of text

Many writers think that these types of text are informal. But their readers are the readers that STE is for: readers who do not have English as their first language, readers who must act quickly, and agents that do each instruction as it is written.

| Type of text | STE text type | Guide |
|---|---|---|
| Commit messages | Descriptive | [text-types/commit-messages.md](text-types/commit-messages.md) |
| Pull request descriptions | Descriptive, with procedural steps for tests | [text-types/pull-requests.md](text-types/pull-requests.md) |
| Error messages | Descriptive, then procedural | [text-types/error-messages.md](text-types/error-messages.md) |
| Log messages | Descriptive | [text-types/log-messages.md](text-types/log-messages.md) |
| API reference documentation | Descriptive, with procedural examples | [text-types/api-reference.md](text-types/api-reference.md) |
| Code comments and docstrings | Descriptive | [text-types/code-comments.md](text-types/code-comments.md) |
| Instructions for AI agents, for example `CLAUDE.md` or `AGENTS.md` | Procedural | [text-types/agent-instructions.md](text-types/agent-instructions.md) |

READMEs, runbooks, and installation procedures are also procedural or descriptive technical text. The profile is applicable to them. They do not have a separate guide, because you can use the rules of Sections 5, 6, and 7 directly.

## The profile is not applicable to these types of text

| Type of text | Cause |
|---|---|
| User-interface text | The text of a product has its own style guide, and frequently the voice of a brand. |
| Blog posts | The function of a blog post is to tell a story or to persuade. |
| Postmortems | A postmortem is an analysis and a story of an incident. |
| Release notes | Release notes are written for customers, frequently with the voice of a brand. |

Some text in these types is procedural or descriptive. For example, an error dialog in a user interface is an error message, and the profile is applicable to it. If you are not sure about a text, use [the test](#the-test).
