---
title: "Limits of mechanical checks"
kind: guidance
---

# Limits of mechanical checks

A mechanical check (a linter, a script, or a word list) can find some possible problems in a text. It cannot tell you that a text is STE. This file tells you how a mechanical check can help, and where it fails.

## What a mechanical check can do

- Find text that has a pattern. For example: a semicolon, a contraction, a sentence with more than 20 words, or a word that is not in the dictionary.
- Show a list of areas for a reviewer to examine.
- Help a reviewer find the same problem in many files.

## What a mechanical check cannot do

- It cannot prove that a text obeys the rules. A text that has no results from a check is not necessarily STE.
- It cannot find the meaning of a word. Rule 1.3 is about meaning.
- It cannot tell if a sentence is clear, if the information is in the correct sequence, or if a paragraph has only one topic.
- It cannot correct a text. Only a person or an agent who knows the information in the text can correct it.

Do not use the result of a mechanical check as a measure of compliance. Do not use it as the condition to merge a change.

## Where a mechanical check fails

### 1. It shows correct text as an error

- **Passive voice.** Rule 3.6 lets you use the passive voice in descriptive text when the agent is unknown. Issue 9 gives this STE example: “During transmission, the data was corrupted.” A check for the passive voice shows it as an error.
- **Words that are not in the dictionary.** Rule 1.5 and Rule 1.6 let you use technical nouns. A check cannot know if `cache`, `endpoint`, or `migration` is a technical noun in your text or an error.
- **Sentence length.** Rule 8.5 and Rule 8.6 tell you to count text in parentheses, quoted text, and identifiers as one word. A simple word count gives a number that is too high.

### 2. It does not find errors

- **Approved words with a different meaning.** DEPLOY is approved in Issue 9 with the meaning “to move from storage into operation.” A check finds DEPLOY in the dictionary and shows no problem. It cannot tell if the text uses the software meaning, which is a technical verb in this profile, or a third meaning that is not permitted (Rule 1.3).
- **Part of speech.** Rule 1.2 lets you use an approved word only as its part of speech. A check that does not know the grammar of the sentence cannot find “Test the function” (“test (v)” is not approved, TEST (n) is approved).
- **Structure.** A text can obey all of the rules that a check can count, and not be clear. Rule 4.1 says “short and clear.” A check can count “short.” It cannot measure “clear.”
- **Consistency.** Rule 1.11 and Rule 9.4 are about the use of one term for one item in all of a text. A check cannot know that “the job,” “the task,” and “the worker” are the same item.

### 3. It gives corrections that make the text less clear

- **Word-for-word replacement.** A check can suggest the approved alternative for a word. Rule 9.1 tells you that a word-for-word replacement is frequently not sufficient, and that it can change the meaning. Then you must use a different sentence construction.
- **Word count.** To make a sentence shorter, a writer can remove articles and other words. Rule 4.2 and Rule 4.5 do not let you do this.

### 4. It gives a false confidence

A result of zero problems is not a proof. When a check is part of a pipeline, writers and agents change the text until the check shows zero problems. The text then obeys the check, not the standard.

## What each rule lets a check do

Each rule page has a `mechanical-check` field. [PROFILE.md](../PROFILE.md#5-rule-pages) gives the values. The table shows the value for each rule.

<!-- index:start -->
### `detects` (3)

A check can find all text with the pattern. A person finds if each result is an error.

[8.1](../rules/section-8-punctuation-and-word-count/rule-8-01.md), [8.7](../rules/section-8-punctuation-and-word-count/rule-8-07.md), [GR-6](../rules/section-9-writing-practices/general-recommendations/gr-6.md)

### `suggests` (34)

A check can show possible problems. It misses some, and it shows some correct text.

[1.1](../rules/section-1-words/rule-1-01.md), [1.2](../rules/section-1-words/rule-1-02.md), [1.4](../rules/section-1-words/rule-1-04.md), [1.10](../rules/section-1-words/rule-1-10.md), [1.11](../rules/section-1-words/rule-1-11.md), [1.14](../rules/section-1-words/rule-1-14.md), [2.1](../rules/section-2-multi-word-nouns/rule-2-01.md), [2.2](../rules/section-2-multi-word-nouns/rule-2-02.md), [3.1](../rules/section-3-verbs/rule-3-01.md), [3.2](../rules/section-3-verbs/rule-3-02.md), [3.4](../rules/section-3-verbs/rule-3-04.md), [3.5](../rules/section-3-verbs/rule-3-05.md), [3.6](../rules/section-3-verbs/rule-3-06.md), [3.7](../rules/section-3-verbs/rule-3-07.md), [4.2](../rules/section-4-sentences/rule-4-02.md), [4.3](../rules/section-4-sentences/rule-4-03.md), [5.1](../rules/section-5-procedural-writing/rule-5-01.md), [5.5](../rules/section-5-procedural-writing/rule-5-05.md), [6.3](../rules/section-6-descriptive-writing/rule-6-03.md), [6.6](../rules/section-6-descriptive-writing/rule-6-06.md), [7.1](../rules/section-7-safety-instructions/rule-7-01.md), [8.4](../rules/section-8-punctuation-and-word-count/rule-8-04.md), [8.5](../rules/section-8-punctuation-and-word-count/rule-8-05.md), [8.6](../rules/section-8-punctuation-and-word-count/rule-8-06.md), [9.3](../rules/section-9-writing-practices/rule-9-03.md), [GR-1](../rules/section-9-writing-practices/general-recommendations/gr-1.md), [GR-4](../rules/section-9-writing-practices/general-recommendations/gr-4.md), [GR-7](../rules/section-9-writing-practices/general-recommendations/gr-7.md), [GR-8](../rules/section-9-writing-practices/general-recommendations/gr-8.md), [10.1](../rules/section-10-code-in-text/rule-10-01.md), [10.2](../rules/section-10-code-in-text/rule-10-02.md), [10.3](../rules/section-10-code-in-text/rule-10-03.md), [10.4](../rules/section-10-code-in-text/rule-10-04.md), [10.5](../rules/section-10-code-in-text/rule-10-05.md)

### `none` (29)

Only a person or an agent who reads the text can use the rule.

[1.3](../rules/section-1-words/rule-1-03.md), [1.5](../rules/section-1-words/rule-1-05.md), [1.6](../rules/section-1-words/rule-1-06.md), [1.7](../rules/section-1-words/rule-1-07.md), [1.8](../rules/section-1-words/rule-1-08.md), [1.9](../rules/section-1-words/rule-1-09.md), [1.12](../rules/section-1-words/rule-1-12.md), [1.13](../rules/section-1-words/rule-1-13.md), [3.3](../rules/section-3-verbs/rule-3-03.md), [4.1](../rules/section-4-sentences/rule-4-01.md), [4.4](../rules/section-4-sentences/rule-4-04.md), [4.5](../rules/section-4-sentences/rule-4-05.md), [5.2](../rules/section-5-procedural-writing/rule-5-02.md), [5.3](../rules/section-5-procedural-writing/rule-5-03.md), [5.4](../rules/section-5-procedural-writing/rule-5-04.md), [6.1](../rules/section-6-descriptive-writing/rule-6-01.md), [6.2](../rules/section-6-descriptive-writing/rule-6-02.md), [6.4](../rules/section-6-descriptive-writing/rule-6-04.md), [6.5](../rules/section-6-descriptive-writing/rule-6-05.md), [7.2](../rules/section-7-safety-instructions/rule-7-02.md), [7.3](../rules/section-7-safety-instructions/rule-7-03.md), [8.2](../rules/section-8-punctuation-and-word-count/rule-8-02.md), [8.3](../rules/section-8-punctuation-and-word-count/rule-8-03.md), [9.1](../rules/section-9-writing-practices/rule-9-01.md), [9.2](../rules/section-9-writing-practices/rule-9-02.md), [9.4](../rules/section-9-writing-practices/rule-9-04.md), [GR-2](../rules/section-9-writing-practices/general-recommendations/gr-2.md), [GR-3](../rules/section-9-writing-practices/general-recommendations/gr-3.md), [GR-5](../rules/section-9-writing-practices/general-recommendations/gr-5.md)
<!-- index:end -->

## Use a check correctly

- Call its results “areas to review.” Do not call them “errors,” “failures,” or a “score.”
- Use it before a review, not in place of a review. [README.md](README.md) tells you how to do a review.
- Record the rules that the check does not examine. The reader of the result must know them.
