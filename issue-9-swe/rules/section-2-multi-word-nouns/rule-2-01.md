---
title: "Rule 2.1"
rule: "2.1"
section: "Section 2 – Multi-word nouns"
topic: "Multi-word nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-2-multi-word-nouns/rule-2-01.md"
status: adapted
mechanical-check: suggests
---

# Rule 2.1 – Multi-word nouns

> **Rule 2.1** **Write multi-word nouns of no more than three words.**

Source: [Issue 9, Rule 2.1](../../../issue-9/part-1-writing-rules/section-2-multi-word-nouns/rule-2-01.md) gives the full text and the original examples.

## In software text

The profile adds one decision. Text in code format counts as one word ([Rule 10.2](../section-10-code-in-text/rule-10-02.md)). Thus, an identifier, for example `user_session_cache`, is one word. It is not a multi-word noun, and you do not count its parts.

Software text frequently contains long groups of nouns, for example “user session token cache invalidation.” The primary noun is the last word. The reader must find the relation between the four words before it. An agent can connect these words in an incorrect sequence.

To make a multi-word noun shorter, use a preposition (of, for, in, on), a clause that starts with “that,” or a verb ([Rule 3.7](../section-3-verbs/rule-3-07.md)).

Use this rule for these types of text:

- **Commit messages and pull requests.** The subject line has a small quantity of space. Do not put more nouns in a group to make the subject line shorter. Write a shorter sentence, and put the other information in the body. Refer to [commit messages](../../text-types/commit-messages.md).
- **Error messages and log messages.** A long group of nouns in an error message does not tell the reader which item has the problem. Write a sentence that has a verb. Refer to [error messages](../../text-types/error-messages.md) and [log messages](../../text-types/log-messages.md).
- **API reference and code comments.** A text can give the name of a code item as words, for example “the retry policy configuration loader.” Then write the identifier in code format, or divide the multi-word noun.

Do not use code format only to make a multi-word noun shorter. Use code format only for an item that is in the code or that the reader types ([Rule 10.1](../section-10-code-in-text/rule-10-01.md)).

## Examples

- [Non-STE] Fix user session token cache invalidation race condition
- [STE] Correct a race condition in the token cache
  (The Non-STE commit subject has a multi-word noun of seven words. In the STE commit subject, “race condition” and “token cache” have two words each. The subject has 43 characters. The body of the commit gives the other information.)
- [Non-STE] Error: payment provider webhook signature key missing.
- [STE] Error: The service cannot find the key that it uses to validate the signatures of payment webhooks.
- [Non-STE] The API rate limit exceeded response body contains the retry delay.
- [STE] If a client sends too many requests, the API returns status code `429`. The body of this response gives the number of seconds that the client must wait.
- [Non-STE] Set the database connection pool max idle timeout to 300.
- [STE] Set `pool.max_idle_timeout` to `300`. This value is the maximum time in seconds that a connection in the pool can stay open without requests.
  (The identifier in code format counts as one word.)

## Review notes

- The reviewer must find the primary noun of each group of nouns. Then the reviewer must find if the reader can see the relation between the primary noun and each word before it.
- A mechanical check can show a sequence of four or more words that are not verbs, articles, or prepositions. To do this, it must know the part of speech of each word. Many software words are nouns and verbs, for example “log,” “build,” “cache,” and “test.” Thus, the check shows groups that are not multi-word nouns, and it does not show some groups that are multi-word nouns.
- A check incorrectly shows a problem for the name of a product or a standard that the writer must not change ([Rule 2.2](rule-2-02.md)). It also shows a problem for text in quotation marks ([Rule 8.6](../section-8-punctuation-and-word-count/rule-8-06.md)).
- A check can cause a new error. To make the result of the check zero, a writer can put a long group of nouns in code format, for example `user_session_token_cache`. The reviewer must make sure that each code span is the name of an item that is in the code.
