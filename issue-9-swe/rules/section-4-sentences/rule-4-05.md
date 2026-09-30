---
title: "Rule 4.5"
rule: "4.5"
section: "Section 4 – Sentences"
topic: "Articles and demonstrative adjectives"
inherits: "../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-05.md"
status: adapted
mechanical-check: none
---

# Rule 4.5 – Articles and demonstrative adjectives

> **Rule 4.5** **When applicable, use an article (the, a, an) or a demonstrative adjective (this, these) before a noun or a multi-word noun.**

Source: [Issue 9, Rule 4.5](../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-05.md) gives the full text and the original examples.

## In software text

The profile adds two interpretations and one decision for identifiers.

- **Interpretation: an identifier after the noun.** Issue 9 tells you that “the” is incorrect before a noun that has an alphanumeric identifier after it (“Tag circuit breaker 36L7”). In software text, do not use “the” in this construction: “Revert commit `a1b2c3d`,” “Refer to issue #123,” “Upgrade the database to version 16.”
- **Interpretation: an identifier in parentheses.** This instruction is not applicable to an identifier in parentheses. Issue 9 uses “the” before a noun that has an item number in parentheses: “Install the nuts (2) and the bolts (3).” Thus, write “Change the configuration file (`config.yaml`).”
- **Decision of the profile: a name before the noun.** Issue 9 does not give an instruction for a name that comes before the noun. The profile tells you to use an article: “the `main` branch,” “the `--output` flag,” “the `config.yaml` file.” Issue 9 uses an article in an equivalent construction in [Rule 4.3](../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-03.md): “A completed REC-1 form.” Do not write “Merge into `main`.”

Developer text frequently has no articles: “Returns user object,” “Restart service after config change,” “See config file.” Commit subjects, log messages, code comments, and agent instructions have this problem most frequently. Without an article, the reader cannot know if the text is about one specified item or about all items of that type.

Do not use an article in a sentence about all items of a type: “Credentials must not be in the repository.”

In a series, an adjective after “the” can refer to all items or only to the first item. “Delete the expired tokens, sessions, and keys” is not clear. Write “Delete the expired tokens, the sessions, and the keys” if only the tokens are expired.

## Examples

- [Non-STE] Returns user object or null if not found.
- [STE] Return the user object. If the database does not contain the user, return `null`.
  (The first line of a docstring, in the imperative.)
- [Non-STE] Restart service after config change.
- [STE] Start the service again after you change the configuration.
- [Non-STE] Revert the commit a1b2c3d.
- [STE] Revert commit `a1b2c3d`.
  (The identifier comes after the noun. Thus, the text has no article.)
- [Non-STE] Merge into main.
- [STE] Merge the pull request into the `main` branch.

## Review notes

- The reviewer must find if each noun refers to a specified item, to one item of a type, or to all items of a type. Only a reader who knows the text can make this decision.
- The reviewer must examine each series for an adjective that can refer to one item or to all items.
- A mechanical check cannot find a missing article, because a correct general sentence also has no article. A check that adds “the” before each noun makes errors, for example “the commit `a1b2c3d`.”
- A check can find “the” before a noun and an identifier. But it cannot know if the identifier is a name (“the `main` branch”) or a number that identifies the item (“commit `a1b2c3d`”).
