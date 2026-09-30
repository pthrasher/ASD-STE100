---
title: "Rule 3.7"
rule: "3.7"
section: "Section 3 - Verbs"
topic: "How to describe an action"
inherits: "../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-07.md"
status: unchanged
mechanical-check: suggests
---

# Rule 3.7 – How to describe an action

> **Rule 3.7** **Use an approved verb to describe an action, not a noun or other parts of speech.**

Source: [Issue 9, Rule 3.7](../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-07.md) gives the full text and the original examples.

## In software text

Software text frequently puts the verb in a noun and adds a general verb: “perform validation of,” “make a call to,” “do the deletion of,” “carry out the initialization of.” The verb in these constructions gives no information. Use the verb of the noun if that verb is approved or is a technical verb in [verbs.md](../../dictionary/verbs.md). These are examples:

- “perform validation of the input” → “validate the input” ([validate (v)](../../dictionary/verbs.md#validate-v))
- “make a call to the endpoint” → “call the endpoint” ([call (v)](../../dictionary/verbs.md#call-v))
- “before the deletion of the branch” → “before you delete the branch.”

Rule 3.7 does not let you make a verb from a noun. If the verb is not approved and is not a technical verb, keep the noun. Use an approved verb with the noun. For example, test (v), check (v), and log (v) are not approved. Write “Do a test of the migration,” “Do a lint check,” and “Record the error in the log.” Refer to [test (v)](../../dictionary/verbs.md#test-v), [check (v)](../../dictionary/verbs.md#check-v), and [Rule 1.7](../section-1-words/rule-1-07.md).

The nouns “validation” and “initialization” are not in the Issue 9 dictionary or in [nouns.md](../../dictionary/nouns.md). Thus, the verb is usually the only correct form. Also, do not use a technical verb as a noun, for example “the deploy” or “a push” ([Rule 1.13](../section-1-words/rule-1-13.md)).

## Examples

- [Non-STE] This function performs validation of the request body.
- [STE] This function validates the request body.
- [Non-STE] Before the deletion of the branch, make sure that the pull request is merged.
- [STE] Before you delete the branch, make sure that the pull request is merged.
- [Non-STE] The client makes a call to the `/tokens` endpoint to get a new token.
- [STE] The client calls the `/tokens` endpoint to get a new token.
- [Non-STE] Test the migration on a copy of the production data.
- [STE] Do a test of the migration on a copy of the production data.
  (test (v) is not approved. Thus, the STE text uses the approved noun TEST and the approved verb DO.)

## Review notes

- The reviewer must find if the sentence has a general verb and a noun that contains the important information. Then the reviewer must find if a verb for that noun is approved or is a technical verb in the profile.
- A mechanical check can find a pattern of three parts. The first part is a general verb, for example “perform,” “do,” “make,” “carry out,” or “provide.” The second part is a noun, frequently a noun that ends in “-ion,” “-ment,” or “-al.” The third part is “of.”
- The check incorrectly shows a problem for correct text where the verb is not approved: “Do a test of,” “Do a check of,” “Do an inspection of the log.”
- The check does not find a noun construction that has no general verb, for example “Validation of the input occurs in the handler.”
- A check can cause a new error. A writer can change “Do a test of the migration” to “Test the migration.” This new text is not correct, because test (v) is not approved.
