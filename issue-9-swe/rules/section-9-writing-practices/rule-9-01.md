---
title: "Rule 9.1"
rule: "9.1"
section: "Section 9 - Writing practices"
topic: "Different sentence constructions"
inherits: "../../../issue-9/part-1-writing-rules/section-9-writing-practices/rule-9-01.md"
status: unchanged
mechanical-check: none
---

# Rule 9.1 – Different sentence constructions

> **Rule 9.1** **Use a different sentence construction to write a sentence when a word-for-word replacement is not sufficient.**

Source: [Issue 9, Rule 9.1](../../../issue-9/part-1-writing-rules/section-9-writing-practices/rule-9-01.md) gives the full text and the original examples.

## In software text

Because of this rule, a mechanical replacement of words does not give STE. A tool or an agent can find a word that is not approved and put the first alternative from the dictionary in its position. The result frequently has a different meaning, or it has no meaning.

An example from software text: “Run the unit tests.” The Issue 9 dictionary gives OPERATE (v) as the alternative for “run.” A word-for-word replacement gives “Operate the unit tests.” This sentence has no clear meaning. OPERATE has the meaning “to put, keep, or be in action.” You do not put a test in action. The profile gives the technical verb “execute” for programs, scripts, commands, and tests ([execute (v)](../../dictionary/verbs.md#execute-v)): “Execute the unit tests.” For other meanings of “run,” the profile gives other alternatives ([run (v)](../../dictionary/verbs.md#run-v)). Thus, before you replace a word, find the meaning that the word has in the sentence.

If you are an agent that changes text to STE, do these steps for each sentence:

1. Find the information that the sentence gives, and the task that the reader must do.
2. Find the approved words and the technical words that give the same information. Find the words in the profile dictionary first ([dictionary/README.md](../../dictionary/README.md)).
3. Write a new sentence with these words. If necessary, change the structure, divide the sentence, or put the information in a list or a table.
4. Compare the meaning of the new sentence with the meaning of the initial sentence. If the meaning is different, write the sentence again.

## Examples

- [Non-STE] Run the unit tests before you push.
- [Non-STE] Operate the unit tests before you push.
  (A word-for-word replacement with the Issue 9 alternative for “run.” The meaning is not clear.)
- [STE] Execute the unit tests before you push the branch.
- [Non-STE] The worker handles connection errors.
- [Non-STE] The worker uses connection errors.
  (A word-for-word replacement with USE (v), an Issue 9 alternative for “handle.” The meaning changed.)
- [STE] The worker catches connection errors and records them in the log.
- [Non-STE] Fix the date parsing bug.
- [Non-STE] Set the date parsing bug.
  (SET (v) is an Issue 9 alternative for “fix.” Its meaning is “to put something into a given adjustment, condition, or mode.” The result has no meaning.)
- [STE] Correct the bug in the date parser.
- [Non-STE] The deploy failed, so the old version is still live.
- [STE] The deployment stopped before its end. Thus, the previous version continues to operate.

## Review notes

- A check can show the alternatives of the dictionary for a word that is not approved. It cannot select the alternative that has the correct meaning. It cannot find a new sentence construction. Only a person or an agent who knows the meaning of the text can use Rule 9.1.
- A correction that adds errors: a tool that replaces words automatically can make correct English sentences that give incorrect information. A check for approved words then shows no problem, because it cannot find the error. Only a reader who compares the meaning of the two texts can find it.
- The reviewer must compare the initial text and the new text, sentence by sentence. The reviewer must make sure that the new text does not add, remove, or change information. If the reviewer does not know the meaning of the initial text, the reviewer must speak to the writer.
- Do not think that the result of an automatic replacement is almost correct. Start from the meaning of the text.
