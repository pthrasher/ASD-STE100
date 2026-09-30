---
title: "How to review a text"
kind: guidance
---

# How to review a text

A review is the check of a text against this profile. A person or an agent who reads the text does the review. A mechanical check cannot do it. [LIMITS.md](LIMITS.md) gives the causes.

## Who does the review

- The reviewer must not be the writer of the text. An agent can review the text of a different agent, but it must start without the context of the writer.
- The reviewer must know the information that the text must give. If the reviewer does not know it, the reviewer must get it from the writer before the review.

## Procedure

1. Find the type of text in [SCOPE.md](../SCOPE.md). Read the guide for that type in [text-types/](../text-types/README.md).
2. Read all of the text one time. Find the information that the text must give to the reader.
3. Examine the words:
   - Make sure that each word is approved, in its approved meaning and part of speech (Rules 1.1 to 1.4).
   - Make sure that each word that is not approved is a technical noun or a technical verb (Rules 1.5 to 1.13). Use the lookup procedure in [dictionary/README.md](../dictionary/README.md).
   - Make sure that the text uses one term for one item (Rule 1.11).
4. Examine the sentences:
   - Examine the length (Rule 5.1 and Rule 6.3). Count words as Section 8 and Section 10 tell you.
   - Make sure that each instruction has one action (Rule 5.2) and uses the imperative (Rule 5.3).
   - Examine the verb forms and the voice (Section 3).
5. Examine the structure:
   - Make sure that the information is in the sequence that is necessary for the reader (Rule 6.1).
   - Make sure that each paragraph has one topic (Rule 6.5).
   - Make sure that each safety instruction obeys Section 7.
6. Read the text again as its reader. If the reader is an agent, read each sentence as an instruction that the agent does exactly as it is written. Find each sentence that can have two meanings for the reader.

## Report

For each finding, give:

- the rule number
- the text that has the problem
- the cause, in one sentence
- a new text that keeps the meaning

Do not replace one word with its alternative if the meaning changes (Rule 9.1). Write a different sentence construction.

At the end of the report, write the rules that you did not examine. Do not write that the text “is compliant” or “passes.” Write “No findings for the rules that I examined.”

## Calibration

Before you review a type of text for the first time, read some examples in Issue 9. The `[STE]` and `[Non-STE]` pairs in [../../issue-9/part-1-writing-rules/](../../issue-9/part-1-writing-rules/README.md) show how the authors of the standard use each rule.

## Instructions for an agent that reviews

You can give these instructions to a review agent:

```text
Review the text below against the ASD-STE100 software profile in issue-9-swe/.
Read issue-9-swe/review/README.md and do the procedure in it.
Find each word that you are not sure about in the dictionary. Do not guess the status of a word.
Report each finding with the rule number, the text, the cause, and a new text.
Do not report the result of a mechanical check as a finding without your own examination.
At the end, write the rules that you did not examine.
```
