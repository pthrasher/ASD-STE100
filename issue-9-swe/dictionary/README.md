---
title: "Dictionary"
kind: guidance
---

# Dictionary

The profile does not have a full dictionary. It uses the [Issue 9 dictionary](../../issue-9/part-2-dictionary/README.md) and adds decisions for software words.

| File | Contents |
|---|---|
| [verbs.md](verbs.md) | Software verbs: technical verbs that you can use, and alternatives for verbs that are not approved |
| [nouns.md](nouns.md) | Software technical nouns, with one term for each item |
| [index.md](index.md) | All words of Issue 9 and of this profile in one table. A script makes this file. Do not change it. |

## How to find a word

1. Find the word in [index.md](index.md). The Profile column shows the decision of the profile, if there is one.
2. If the Profile column has a decision, read the entry in [verbs.md](verbs.md) or [nouns.md](nouns.md). Use the profile entry, not the Issue 9 entry.
3. If the Profile column is empty, read the Issue 9 entry. Issue 9 is applicable without a change.
4. If the word is not in the index, it is not approved, unless it is a technical noun (Rule 1.5) or a technical verb (Rule 1.12). For a technical verb, make sure that no approved verb gives the same information (Rule 1.12).

You can search the two dictionaries with one command, because the entries have the same heading format:

```sh
grep -rn -A12 '^## run (v)' issue-9-swe/dictionary issue-9/part-2-dictionary/words
```

## Letter case

In Issue 9, UPPERCASE shows an approved word and lowercase shows a word that is not approved. The profile writes its headwords in lowercase, because a technical noun or a technical verb is not an approved word of the dictionary. Use the `Profile status` field. Do not use the letter case.

## Decisions

Each entry has a Decision field: `standard`, `proposed`, or `accepted`. [PROFILE.md](../PROFILE.md#3-decisions) gives the meaning of each value. To change a decision, change the entry and write the cause in the Note field.
