---
title: "GR-7 Inclusive language"
gr: "GR-7"
section: "Section 9 - Writing practices"
topic: "General recommendations"
inherits: "../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-7.md"
status: unchanged
mechanical-check: suggests
---

# GR-7 Inclusive language

This recommendation tells you to use gender-neutral language.

Source: [Issue 9, GR-7](../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-7.md) gives the full text.

## In software text

Issue 9 gives two instructions. The profile uses them without a change:

- Do not use “he” or “she.” For a user, a developer, a maintainer, or a reviewer, write the noun again ([GR-3](gr-3.md)).
- Do not use “man” or “woman,” unless they are necessary, for example in a medical text.

The profile does not add a list of other terms.

## Examples

- [Non-STE] Ping the maintainer and ask him to review your PR.
- [STE] Tell the maintainer that the code review of your pull request can start.
- [Non-STE] If the user forgets her password, she can reset it from the login page.
- [STE] If the user does not know the password, the user can set a new password on the login page.

## Review notes

- A check with a list of words can find “he,” “she,” “his,” “her,” “man,” and “woman.” It must first remove code spans and code blocks.
- The check shows correct text as areas to review. For example, “man” can be correct in a medical text, and a word can be in quoted text that you cannot change (Rule 8.6).
- The reviewer must read the full text. A sentence can refer to a person by gender without these words.
