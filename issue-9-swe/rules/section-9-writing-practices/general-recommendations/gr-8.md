---
title: "GR-8 Possessive form"
gr: "GR-8"
section: "Section 9 - Writing practices"
topic: "General recommendations"
inherits: "../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-8.md"
status: adapted
mechanical-check: suggests
---

# GR-8 Possessive form

This recommendation tells you to use the possessive form (“’s”) correctly, and not to use it if you are not sure that the sentence is correct.

Source: [Issue 9, GR-8](../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-8.md) gives the full text and the original examples.

## In software text

The profile adds this decision: do not put the possessive form after a code span. Write “the `name` field of the `User` object,” not “`User`’s name.” The cause is that the apostrophe and the “s” then come immediately after the identifier. A reader or an agent can think that they are part of the identifier, or copy them with it. Also, “`User`’s name” does not tell the reader if “name” is a field, a method, or a value.

In other text, Issue 9 lets you use the possessive form. Make sure that the sentence is correct and clear:

- Do not use two possessive forms together: “the client’s token’s scopes.” Write “the scopes of the client token.”
- For a plural noun, the possessive form has only an apostrophe: “the users’ sessions.” This form is not easy to see. Write “the sessions of the users.”
- “Its” is a possessive adjective. “It’s” is a contraction, and contractions are not permitted ([Rule 4.2](../../section-4-sentences/rule-4-02.md)).

## Examples

- [Non-STE] Update `User`'s name before you save it.
- [STE] Set the `name` field of the `User` object before you save the object.
- [Non-STE] The `config`'s `timeout` value is in seconds.
- [STE] The unit of the `timeout` value in `config` is seconds.
- [Non-STE] Log the client's token's scopes on each request.
- [STE] On each request, record the scopes of the client token in the log.
- [Non-STE] The users' sessions expire after 24h.
- [STE] After 24 hours, the sessions of the users are expired.

## Review notes

- A check can find “’s” and “'s” after a code span. It can also find all other possessive forms, but most of them are correct. These are areas to review.
- The same check also finds contractions, for example “it’s” and “that’s.” These are errors, but for Rule 4.2, not for GR-8.
- A check does not find the possessive form of a plural noun (“users’”), because it has no “s” after the apostrophe. It also does not find a possessive form if the text and the check use different apostrophes (’ and ').
- The reviewer must make sure that each possessive form is clear. If the reader can think that the item is part of two different items, write the sentence with “of.”
