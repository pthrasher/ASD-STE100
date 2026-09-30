---
title: "Rule 9.2"
rule: "9.2"
section: "Section 9 - Writing practices"
topic: "How to use approved words correctly"
inherits: "../../../issue-9/part-1-writing-rules/section-9-writing-practices/rule-9-02.md"
status: adapted
mechanical-check: none
---

# Rule 9.2 – How to use approved words correctly

> **Rule 9.2** **Use each approved word correctly.**

Source: [Issue 9, Rule 9.2](../../../issue-9/part-1-writing-rules/section-9-writing-practices/rule-9-02.md) gives the full text and the original examples.

## In software text

The profile adds this decision: some approved words of Issue 9 have a second, software meaning, and the profile gives that meaning as a technical verb. These words are [deploy (v)](../../dictionary/verbs.md#deploy-v), [push (v)](../../dictionary/verbs.md#push-v), [pull (v)](../../dictionary/verbs.md#pull-v), [release (v)](../../dictionary/verbs.md#release-v), and [catch (v)](../../dictionary/verbs.md#catch-v). The profile also gives a software meaning of the approved verb [install (v)](../../dictionary/verbs.md#install-v): “To put software on a computer system so that it is ready for use.” You can use these words with the Issue 9 meaning or with the software meaning of the profile. You cannot use them with a third meaning. For all other approved words, only the Issue 9 meaning is correct.

Software text uses many approved words with a meaning that is not approved. Examples:

- KILL (v) has only the meaning “to cause death.” For a process, use STOP (v) ([kill (v)](../../dictionary/verbs.md#kill-v)).
- SEE (v) is only for items that you can see with your eyes. For a reference, use REFER (v).
- GO (v) together with DOWN is a movement. A service that “goes down” stops.
- ABOVE and BELOW are for positions. For a limit, use MORE THAN and LESS THAN.
- TURN (v) is a movement around an axis. An indicator that “turns red” changes its color.

Also use each approved word only as its approved part of speech ([Rule 1.2](../section-1-words/rule-1-02.md)). TEST (n) is approved, but “test (v)” is not ([test (v)](../../dictionary/verbs.md#test-v)). WORK (n) is approved, but “work (v)” is not ([work (v)](../../dictionary/verbs.md#work-v)).

## Examples

- [Non-STE] Kill the worker if it hangs.
- [STE] If the worker does not complete its task in 5 minutes, stop the worker process.
- [Non-STE] See the API reference for all parameters.
- [STE] Refer to the API reference for all parameters.
- [Non-STE] The payments service went down at 02:14 UTC.
- [STE] The `payments` service stopped at 02:14 UTC.
- [Non-STE] Alert when CPU usage stays above 90% for 5 minutes.
- [STE] Send a message to the operations team when the CPU load is more than 90% for 5 minutes.
- [Non-STE] If the fix works, the status badge turns green.
- [STE] If the correction is satisfactory, the color of the status badge changes to green.

## Review notes

- A check finds each approved word in the dictionary and shows no problem. It cannot find an approved word with a meaning that is not approved. “Kill the process,” “see the docs,” and “the service went down” contain only approved words.
- A check that does not know the grammar of the sentence cannot find the part of speech. It cannot find “Test the function,” where “test” is a verb.
- For deploy, push, pull, release, catch, and install, the reviewer must find the meaning that the text uses. “Release the lock” uses the Issue 9 meaning. “Release version 2.0” uses the software meaning of the profile. “Push the button” uses the Issue 9 meaning. A third meaning, for example “push back on a decision,” is not permitted.
- The reviewer must examine each approved word that software text frequently uses with a meaning that is not approved: kill, see, go, turn, hit, hang, fire, and above or below with a number.
