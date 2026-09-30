---
title: "Rule 1.13"
rule: "1.13"
section: "Section 1 – Words"
topic: "Technical verbs"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-13.md"
status: unchanged
mechanical-check: none
---

# Rule 1.13 – Technical verbs

> **Rule 1.13** **Do not use technical verbs as nouns.**

Source: [Issue 9, Rule 1.13](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-13.md) gives the full text and the original examples.

## In software text

Software text frequently uses a technical verb as a noun: “do a deploy,” “the install,” “after the upgrade,” “a quick reboot.” Write the verb as a verb. If the profile gives a technical noun for the item, you can use that noun. For example, use [deployment (TN)](../../dictionary/nouns.md#deployment-tn), not “deploy” as a noun.

Some words are a technical verb and a technical noun, because the profile gives the two entries: commit, build, and release. “Update” is in Rule 1.5, category 19, and in Rule 1.12, category 2 c. You can use these words as verbs and as nouns. Refer to [Rule 1.7](rule-1-07.md).

You can use the past participle of a technical verb as an adjective: “the merged branch,” “the deleted file,” “the deployed version.”

## Examples

- [Non-STE] Do a deploy to the test environment.
- [STE] Deploy the release to the test environment.
- [Non-STE] After the upgrade, clear the cache.
- [STE] After you upgrade the database, clear the cache.
- [Non-STE] If you get conflicts during the rebase, resolve them and continue.
- [STE] If a merge conflict occurs when you rebase the branch, correct it. Then execute `git rebase --continue`.
- [Non-STE] Delete the branches after the merge.
- [STE] Delete the merged branches.

## Review notes

- The reviewer must find each technical verb that has the function of a noun. Words such as “a,” “the,” and “after the” before the verb show this function.
- If a word is in [verbs.md](../../dictionary/verbs.md) and in [nouns.md](../../dictionary/nouns.md), it is correct as a verb and as a noun. Examine the two files before you write a report about a problem.
- A mechanical check cannot help. A word-list check accepts “deploy” and “rebase” in all positions, because they are in verbs.md.
