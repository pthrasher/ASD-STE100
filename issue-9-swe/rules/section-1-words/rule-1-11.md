---
title: "Rule 1.11"
rule: "1.11"
section: "Section 1 – Words"
topic: "Technical nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-11.md"
status: adapted
mechanical-check: suggests
---

# Rule 1.11 – Technical nouns

> **Rule 1.11** **Do not use different technical nouns for the same item.**

Source: [Issue 9, Rule 1.11](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-11.md) gives the full text and the original example.

## In software text

The profile gives one term for each frequent item of software in [nouns.md](../../dictionary/nouns.md). The “Do not use” field of each entry gives the other terms for the same item. This rule is the basis for these fields. For example:

- Use “directory.” Do not use “folder.”
- Use “configuration.” Do not use “config” or “settings.”
- Use “pull request.” Do not use “merge request.”

The profile also uses this rule for two technical verbs that have the same meaning. Use “raise” or “throw” for exceptions, as the programming language of the text does. Do not use the two verbs in the same text. Refer to [raise (v)](../../dictionary/verbs.md#raise-v).

If the code has a name for an item, use the same term in all text: comments, commit messages, and error messages ([Rule 1.8](rule-1-08.md)). An agent that reads “the worker,” “the job runner,” and “the consumer” can think that these are three different items. [Rule 9.4](../section-9-writing-practices/rule-9-04.md) tells you to use consistent terminology in all of a text.

## Examples

- [Non-STE] 1\. Open the config file.<br>
  2\. Set `timeout` to 30 in the settings.<br>
  3\. Start the service again to load the new configuration.<br>
- [STE] 1\. Open the configuration file.<br>
  2\. Set `timeout` to 30 in the configuration file.<br>
  3\. Start the service again.<br>
- [Non-STE] Open a PR against `main`. After the merge request gets two approvals, merge the change.
- [STE] Open a pull request for the `main` branch. When two reviewers give their approval, merge the pull request.
- [Non-STE] The parser raises `ValueError` if the input is empty. It throws `KeyError` if the key is missing.
- [STE] The parser raises `ValueError` if the input is empty. It raises `KeyError` if the key is missing.

## Review notes

- The reviewer must read all of the text, not one sentence at a time. For a pull request, read the terms in the code and in the text.
- The reviewer must find if two terms are for the same item or for two items. For example, “process” and “container” are two different items.
- A mechanical check can compare the text with the “Do not use” fields of nouns.md. It shows possible problems.
- The check shows correct text as a possible problem. “Settings” is correct in quoted text from the screen, for example Click “Settings” (Rule 1.5, category 10). “Issue” is correct for an item in an issue tracker ([issue (TN)](../../dictionary/nouns.md#issue-tn)).
- The check does not find synonyms that are not in nouns.md, or the terms that one project uses for its items. [LIMITS.md](../../review/LIMITS.md#2-it-does-not-find-errors) gives an example.
- A replacement in all of a text can change the meaning. If the check replaces each “issue” with “bug,” an item in the tracker becomes an error in code.
