---
title: "Rule 8.5"
rule: "8.5"
section: "Section 8 - Punctuation and word count"
topic: "Word count"
inherits: "../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-05.md"
status: unchanged
mechanical-check: suggests
---

# Rule 8.5 – Word count

> **Rule 8.5** **When you put text in parentheses, it counts as one word in that sentence.**

Source: [Issue 9, Rule 8.5](../../../issue-9/part-1-writing-rules/section-8-punctuation-and-word-count/rule-8-05.md) gives the full text and the original examples.

## In software text

In software text, parentheses frequently contain a default value, a unit, an abbreviation, an issue number, or a commit hash. Count all the text in the parentheses as one word of the sentence. If the text in the parentheses is a sentence, count its words again as a different sentence. The limits of [Rule 5.1](../section-5-procedural-writing/rule-5-01.md) and [Rule 6.3](../section-6-descriptive-writing/rule-6-03.md) are applicable to it.

Parentheses in a code span, for example `close()` or `f(x)`, are part of the code. The full code span counts as one word ([Rule 10.2](../section-10-code-in-text/rule-10-02.md)).

Do not put information in parentheses only to make a sentence shorter. If the text in parentheses is long, write it as a different sentence ([Rule 8.3](rule-8-03.md)).

## Examples

- [Non-STE] Increase the upload timeout (currently 10s, which is too short for large files on slow connections, see #812) to 30s.
- [STE] Increase the upload timeout to 30 seconds (refer to issue #812). &emsp;(7 words)<br>
  A timeout of 10 seconds is too short for large files. &emsp;(10 words)
  (The text in parentheses in the first sentence has 4 words and counts as a different sentence.)
- [Non-STE] Revert the commit that caused the checkout regression (3de91f1, merged last Friday by the payments team after a rushed review).
- [STE] Revert the commit that caused the regression (`3de91f1`). &emsp;(8 words)
- [Non-STE] Set the timeout to 30s (default: 10s, which causes spurious timeouts under load).
- [STE] Set the timeout to 30 seconds (the default value is 10 seconds). &emsp;(6 words)
  (The sentence in parentheses has 5 words.)

## Review notes

- A check can count text in parentheses as one word. It must first remove code spans, because a function call in code format contains parentheses.
- A check must also count the words in the parentheses as a different sentence. If it does not, it does not find long text in parentheses.
- A parenthesis that is not part of a pair, for example the list number “1)”, causes an incorrect count. The reviewer must count these sentences again.
- The reviewer must find the text in parentheses that is not necessary. A sentence that is short only because most of its information is in parentheses is not short in the meaning of Rule 5.1 and Rule 6.3.
