---
title: "Rule 3.2"
rule: "3.2"
section: "Section 3 - Verbs"
topic: "Verb forms and tenses of verbs"
inherits: "../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-02.md"
status: adapted
mechanical-check: suggests
---

# Rule 3.2 – Verb forms and tenses of verbs

> **Rule 3.2** **Use only these verb forms and tenses of verbs:**
> - **The infinitive form**
> - **The imperative form (command form)**
> - **The simple present tense**
> - **The simple past tense**
> - **The simple future tense**
> - **The past participle form (as an adjective).**

Source: [Issue 9, Rule 3.2](../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-02.md) gives the full text and the original examples.

## In software text

The profile adds these decisions about which form to use:

- **Imperative.** Use the imperative for a commit subject line and for the first line of a docstring: “Add a timeout to the upload client.” The remaining text of a commit body or a docstring is descriptive text. Refer to [commit messages](../../text-types/commit-messages.md) and [code comments](../../text-types/code-comments.md).
- **Simple past tense.** Use the simple past tense for something that occurred at a known time. Examples are a log message about a completed operation, and the previous operation of the code in a commit body: “The parser removed the last line of the file.”
- **Simple present tense.** Use the simple present tense for how the code operates at all times. Examples are API reference text, the body of a docstring, and the operation of the new code in a commit body: “The parser keeps the last line.”
- **Simple future tense.** Use the simple future tense for a result that occurs after a step of the reader: “The service will start again after 30 seconds.”

Software text frequently uses verb forms and tenses that are not approved:

- The present perfect: “This has been broken since version 2.3.” Write the simple past tense and a time: “This bug occurred first in version 2.3.”
- The progressive: “The service is currently returning 500 errors.” For a condition at the time of the text, use the simple present tense and AT THIS TIME. Issue 9 gives AT THIS TIME as the alternative to [now (adv)](../../../issue-9/part-2-dictionary/words/n.md#now-adv). Write: “At this time, the service returns errors.”
- A log message that starts with an “-ing” form: “Downloading packages...” Refer to [Rule 3.5](rule-3-05.md).

## Examples

- [Non-STE] Fixed a bug where the parser was dropping the last line.
- [STE] Correct the parser bug that removed the last line
  (Commit subject line: the imperative for the change, and the simple past tense for the previous operation of the code.)
- [Non-STE] Migration has completed successfully.
- [STE] The migration is completed. It changed 1,204 rows.
- [Non-STE] When called, this function will be returning the cached value.
- [STE] This function returns the value from the cache.
- [Non-STE] We are currently investigating elevated error rates on the API.
- [STE] At this time, the API gives more errors than usual. We are not sure of the cause. We will give more information at 14:00 UTC.

## Review notes

- The reviewer must find if a sentence is about something that occurred one time (simple past tense) or about how the code always operates (simple present tense). A check cannot know this. For example, “The deployment stops” in an incident note is possibly incorrect. The correct text can be “The deployment stopped.”
- A mechanical check can find these patterns:
  - “Has,” “have,” or “had” and a past participle
  - “Is,” “are,” “was,” or “were” and an “-ing” word
  - “Will be” and an “-ing” word.
- The check incorrectly shows a problem for HAVE as the primary verb (“The table has deleted rows”), and for an approved “-ing” adjective after BE (“The value is missing”).
- The check does not find a correct tense that has the incorrect time. It also does not find a verb form in the incorrect clause, for example the imperative in a descriptive sentence.
