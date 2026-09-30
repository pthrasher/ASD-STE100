---
title: "Rule 1.1"
rule: "1.1"
section: "Section 1 – Words"
topic: "Which words can you use?"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-01.md"
status: adapted
mechanical-check: suggests
---

# Rule 1.1 – Which words can you use?

> **Rule 1.1** **Use words that are:**
> - **Approved in the dictionary**
> - **Technical nouns**
> - **Technical verbs.**

Source: [Issue 9, Rule 1.1](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-01.md) gives the full text and the original examples.

## In software text

The profile adds two items to this rule:

- **Text in code format.** An identifier, a command, a path, or a value in code format is not a word of the text. This rule is not applicable to it. [Rule 10.1](../section-10-code-in-text/rule-10-01.md) tells you which text to write in code format.
- **The profile dictionary.** The Help text of Issue 9 tells you to use the glossary of your company. For software text, the glossary is [dictionary/](../../dictionary/README.md). It gives technical verbs in [verbs.md](../../dictionary/verbs.md) and technical nouns in [nouns.md](../../dictionary/nouns.md).

Find each word that you are not sure about in the dictionary. [dictionary/README.md](../../dictionary/README.md#how-to-find-a-word) gives the procedure. Many words that software text uses frequently are not approved, for example “run,” “check,” “should,” “need,” and “fix.” [verbs.md](../../dictionary/verbs.md) gives an alternative for each of them.

This rule is applicable to all types of text in [SCOPE.md](../../SCOPE.md). In [agent instructions](../../text-types/agent-instructions.md), a word that is not approved can have more than one meaning. The agent cannot get the correct meaning from you. An agent that writes STE must find each word in the dictionary. It must not think that a word is approved because software text uses it frequently.

## Examples

- [Non-STE] Utilize the retry helper to handle transient errors.
- [STE] Use the `with_retry()` function for requests that can have temporary errors.
  (“Utilize,” “handle,” and “transient” are not approved. `with_retry()` is in code format.)
- [Non-STE] Once the tests are green, go ahead and commit.
- [STE] When all tests pass, commit the changes.
  (“Pass” and “commit” are technical verbs in [verbs.md](../../dictionary/verbs.md). TEST (n) and CHANGE (n) are approved.)
- [Non-STE] Grab the token from the dashboard.
- [STE] Copy the API token from the dashboard.
  (“Copy” is a technical verb, Rule 1.12, category 2 b. “API token” and “dashboard” are technical nouns, Rule 1.5, category 19.)

## Review notes

- For each word that is not in the Issue 9 dictionary, find if it is a technical noun or a technical verb. Refer to [Rule 1.5](rule-1-05.md) and [Rule 1.12](rule-1-12.md). If it is not, the word is not permitted.
- A mechanical check can compare each word with the Issue 9 dictionary and the profile dictionary. It shows possible problems. The reviewer must examine each result.
- The check shows correct words as possible problems. Technical nouns that are not in [nouns.md](../../dictionary/nouns.md), for example “schema,” “webhook,” and “cluster,” are correct in their category. A check that does not remove code spans shows each identifier.
- The check does not find an approved word with a meaning that is not approved ([Rule 1.3](rule-1-03.md)), for example “Kill the process.” It does not find an approved word as a different part of speech ([Rule 1.2](rule-1-02.md)), for example “Test the endpoint.” It does not find a word of a Rule 1.12 category that is not in its subject field, for example “fire” in “Fire an event.”
- Do not replace each word that the check shows with its alternative. The meaning can change. Write a different sentence construction ([Rule 9.1](../section-9-writing-practices/rule-9-01.md)).
