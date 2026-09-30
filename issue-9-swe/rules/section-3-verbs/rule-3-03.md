---
title: "Rule 3.3"
rule: "3.3"
section: "Section 3 - Verbs"
topic: "Verb forms and tenses of verbs"
inherits: "../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-03.md"
status: unchanged
mechanical-check: none
---

# Rule 3.3 – Verb forms and tenses of verbs

> **Rule 3.3** **Use the past participle form as an adjective.**

Source: [Issue 9, Rule 3.3](../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-03.md) gives the full text and the original examples.

## In software text

Software text frequently gives the condition of an item with a past participle: “the merged branch,” “the flag is disabled,” “the token is expired.” This is not the passive voice. The sentence tells the condition of the item. It does not tell about a change.

When you use a past participle as an adjective, obey these instructions:

- **Condition or change.** “The feature flag is disabled” gives a condition. “The feature flag was disabled by the deployment script” tells about a change and its agent. This second sentence is in the passive voice, and [Rule 3.6](rule-3-06.md) is applicable to it.
- **Only permitted verbs.** Use the past participle of an approved verb, or of a technical verb in [verbs.md](../../dictionary/verbs.md). Do not use the past participle of a verb that is not approved. For example, “cached,” “configured,” and “hardcoded” are not permitted, because cache (v), configure (v), and hardcode (v) are not approved verbs or technical verbs.
- **Approved adjectives.** Some past participles are approved adjectives, for example EXPIRED, DAMAGED, and PERMITTED. You can use them.

In API reference text and error messages, a condition is frequently the most important information: “The token is expired.” A past participle as an adjective gives it clearly.

## Examples

- [Non-STE] Returns the cached response if one exists.
- [STE] Return the response from the cache if the cache contains it.
  (“Cached” is the past participle of cache (v), which is not approved. The STE text is the first line of a docstring.)
- [Non-STE] The configured timeout is ignored.
- [STE] The service ignores the timeout value in the configuration.
- [Non-STE] Delete branches that have been merged.
- [STE] Delete the merged branches.
- [Non-STE] The feature flag was disabled by the deployment script.
- [STE] The deployment script disabled the feature flag. When the feature flag is disabled, the API returns status code `404` for this endpoint.
  (The Non-STE sentence tells about a change in the passive voice, and the agent is known ([Rule 3.6](rule-3-06.md)). In the STE text, the first sentence tells about the change in the active voice. The second sentence gives a condition with a past participle as an adjective.)

## Review notes

- The reviewer must find if BE and a past participle give a condition or a change. Use this test: if you can add “by” and an agent, and the sentence then tells about a change at a time, it is the passive voice. “The branch is merged” is a condition. “The branch was merged by the release script at 10:02” is a change.
- The reviewer must make sure that the past participle comes from an approved verb or a technical verb, or is an approved adjective.
- A mechanical check cannot tell a condition from a change, because the two constructions have the same words. A check for the passive voice shows each correct condition as a problem. For this cause, the profile gives this rule no mechanical check.
- A check can find a past participle that is not in the dictionaries. That is a check for [Rule 1.1](../section-1-words/rule-1-01.md), not for this rule.
