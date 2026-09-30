---
title: "Rule 6.3"
rule: "6.3"
section: "Section 6 - Descriptive writing"
topic: "Sentences"
inherits: "../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-03.md"
status: unchanged
mechanical-check: suggests
---

# Rule 6.3 – Sentences

> **Rule 6.3** **Write short sentences. Use a maximum of 25 words in each sentence.**

Source: [Issue 9, Rule 6.3](../../../issue-9/part-1-writing-rules/section-6-descriptive-writing/rule-6-03.md) gives the full text and the original examples.

## In software text

The limit of 25 words is applicable to each descriptive sentence: the body of a commit message, a pull request description, API reference text, code comments and docstrings, log messages, and the first part of an error message. It is also applicable to each sentence of a note in a procedure ([Rule 5.5](../section-5-procedural-writing/rule-5-05.md)).

Count the words with the rules of Section 8 and Section 10. Each code span counts as one word, and the text in a code block does not count ([Rule 10.2](../section-10-code-in-text/rule-10-02.md)). A colon before a vertical list shows the end of a sentence ([Rule 8.4](../section-8-punctuation-and-word-count/rule-8-04.md)).

If a sentence has more than 25 words, divide it into two or more sentences. Put one subject in each sentence ([Rule 6.1](rule-6-01.md)). Do not remove articles or other words to make it shorter ([Rule 4.2](../section-4-sentences/rule-4-02.md)).

## Examples

- [Non-STE] This PR refactors the session middleware so that tokens are validated once per request instead of in every handler, which removes about 40 lines of duplicated code and fixes the bug where expired tokens were occasionally accepted by the `/export` endpoint.
- [STE] This pull request refactors the session middleware. The middleware validates the token one time for each request. Before this change, each handler validated the token. The change removes approximately 40 lines of code from the handlers. It also corrects a bug: the `/export` endpoint accepted some expired tokens.
  (The Non-STE sentence has 41 words. The STE text has five sentences, and each sentence has less than 15 words.)
- [Non-STE] Returns the cached value for `key` if it exists and has not expired, otherwise calls `loader` to compute the value, stores it in the cache with the configured TTL, and returns it.
- [STE] Return the value for `key` from the cache.<br>
  If the cache does not contain `key`, or if the value is expired, this method calls `loader`. It then keeps the new value in the cache for the time that `ttl` gives, and returns the new value.
  (A docstring. Its first line uses the imperative. Refer to [Rule 5.3](../section-5-procedural-writing/rule-5-03.md).)

## Review notes

- A word count shows sentences that have more than 25 words. These results are areas to examine.
- Where a word count gives incorrect results:
  - It can count a code span, a URL, or a path as more than one word. Section 10 counts each as one word. Thus, the count is too high.
  - It cannot find the end of a sentence in a code comment that continues on many lines, in a log message that has no period, or in a table cell.
  - It does not know if the sentence is an instruction (20 words, [Rule 5.1](../section-5-procedural-writing/rule-5-01.md)) or descriptive text (25 words). The reviewer must identify the type of each sentence.
  - It counts the text of a vertical list as one sentence if it does not use Rule 8.4.
- A sentence of 25 words or less is not necessarily clear. The reviewer must also make sure that the sentence has one subject.
