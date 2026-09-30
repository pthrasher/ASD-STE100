---
title: "Rule 1.3"
rule: "1.3"
section: "Section 1 – Words"
topic: "Approved meaning"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-03.md"
status: adapted
mechanical-check: none
---

# Rule 1.3 – Approved meaning

> **Rule 1.3** **Use approved words only with their approved meanings.**

Source: [Issue 9, Rule 1.3](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-03.md) gives the full text and the original examples.

## In software text

The profile adds a software meaning to five approved verbs. In Issue 9, DEPLOY, PUSH, PULL, RELEASE, and CATCH have approved meanings that are not software meanings. [verbs.md](../../dictionary/verbs.md) gives a software meaning for each of them as a technical verb ([Rule 1.12](rule-1-12.md)): [deploy (v)](../../dictionary/verbs.md#deploy-v), [push (v)](../../dictionary/verbs.md#push-v), [pull (v)](../../dictionary/verbs.md#pull-v), [release (v)](../../dictionary/verbs.md#release-v), and [catch (v)](../../dictionary/verbs.md#catch-v). You can use an Issue 9 meaning or the software meaning. You cannot use a different meaning. For example, “release the lock” uses the Issue 9 meaning (to let go), and “release version 2.4” uses the software meaning. “The tests catch the regression” uses a different meaning (to find), and it is not permitted.

The profile does not give a software meaning to KILL (v). Its only approved meaning is “To cause death.” To stop a process, use STOP (v). Refer to [kill (v)](../../dictionary/verbs.md#kill-v). A command in code format, for example `kill -9`, is not a word of the text.

Software text frequently uses other approved words with a meaning that is not approved:

| Word | Approved meaning | Software use that is not permitted | Write |
|---|---|---|---|
| FOLLOW (v) | To come after, to go after | “Follow the steps in the README.” | OBEY (v), DO (v) |
| HANG (v) | To attach or to be attached to something above with no support from below | “The process hangs.” | The condition that the reader can see: “The process does not show output.” |
| PATCH (n) | A piece of material that you use to repair a surface or hole | “Apply the security patch.” | update (TN) |
| SEE (v) | To know with the eyes | “See the API reference.” | REFER (v) |

In [agent instructions](../../text-types/agent-instructions.md), “follow” is very frequent: “Follow the conventions in `CONTRIBUTING.md`.” Write “Obey the instructions in `CONTRIBUTING.md`.”

## Examples

- [Non-STE] Follow the release checklist before you deploy.
- [STE] Obey the release checklist before you deploy the release.
- [Non-STE] If the worker hangs, kill it.
- [STE] If the process does not show output for 5 minutes, stop it.
- [Non-STE] The integration tests catch this regression.
- [STE] The integration tests find this regression.
  (“Catch” has the software meaning “to receive an exception” only.)
- [Non-STE] Apply the security patch to all hosts.
- [STE] Install the security update on all hosts.
  (“Update” is a technical noun, Rule 1.5, category 19.)
- [Non-STE] See the API reference for the full list of parameters.
- [STE] Refer to the API reference for all parameters.

## Review notes

- The reviewer must know the meaning that the writer wants to give. Then the reviewer compares it with the meaning in the dictionary entry. The spelling of the word does not show if the meaning is correct.
- For DEPLOY, PUSH, PULL, RELEASE, and CATCH, make sure that the sentence uses the Issue 9 meaning or the meaning in [verbs.md](../../dictionary/verbs.md). Also examine the Limit field. For example, the profile gives “push” and “pull” only for version control.
- An approved word that is part of a technical noun is part of the name of the item, for example “leak” in “memory leak.” Rule 1.3 is applicable to the word when it is not part of a technical noun. Issue 9 gives an example of this for a word that is not approved: “main landing gear” ([Rule 1.6](rule-1-06.md)).
- A mechanical check cannot find the meaning of a word. A word-list check shows no problem in “Kill the process,” because KILL is in the dictionary. Refer to [LIMITS.md](../../review/LIMITS.md#2-it-does-not-find-errors).
