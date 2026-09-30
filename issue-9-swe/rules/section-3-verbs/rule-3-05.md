---
title: "Rule 3.5"
rule: "3.5"
section: "Section 3 - Verbs"
topic: "Verb forms and tenses of verbs"
inherits: "../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-05.md"
status: adapted
mechanical-check: suggests
---

# Rule 3.5 – Verb forms and tenses of verbs

> **Rule 3.5** **Use the “-ing” form of a verb only as a technical noun or as a modifier in a technical noun.**

Source: [Issue 9, Rule 3.5](../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-05.md) gives the full text and the original examples.

## In software text

The profile adds two interpretations:

1. **Text in code format.** An identifier in code format is not a word of the text ([Section 10](../section-10-code-in-text/README.md)). This rule is not applicable to `is_loading` or `onClosing`.
2. **Log messages and command-line messages.** A log message or a command-line message frequently starts with an “-ing” form: “Downloading packages...,” “Retrying request.” Use the simple present tense for an operation that continues at the time of the message: “The CLI downloads 12 packages.” Use the simple past tense for an operation that is completed. Refer to [log messages](../../text-types/log-messages.md).

These “-ing” forms are frequent in software text, and are not permitted:

- In commit subjects and pull request titles: “Adding support for YAML.” Use the imperative ([Rule 5.3](../section-5-procedural-writing/rule-5-03.md)).
- In headings: “Getting started,” “Running the tests.” Use a noun, for example “Installation.”
- In code comments: “// Checking if the user exists.” Write a sentence.
- As a preposition or a connecting word: “using,” “following,” “including,” “depending on.” Use WITH for “using” and “that follows” for “following.” For the other words, use a different sentence construction.

An “-ing” form can be a technical noun or a part of a technical noun. The technical noun must be the name of a function or a task. Examples are “Troubleshooting” as a heading, “error handling,” and “load balancing.” Do not use it with an object. “Troubleshooting” is a technical noun, but “Troubleshooting the cache” is not a technical noun.

## Examples

- [Non-STE] Retrying request after timeout (attempt 2/5)...
- [STE] A timeout occurred. The client sends the request again (2 of 5).
- [Non-STE] Adding support for YAML config files
- [STE] Let the CLI read YAML configuration files
  (A commit subject in the imperative.)
- [Non-STE] Install the package using the following command:
- [STE] Install the package with this command:
- [Non-STE] Returns all users, excluding deleted ones.
- [STE] Return all users that are not deleted.
- [STE] Troubleshooting
  (A heading. “Troubleshooting” is a technical noun.)

## Review notes

- The reviewer must find if each “-ing” word is a technical noun, a modifier in a technical noun, or a verb form. A technical noun names a function or a task and does not have an object.
- A mechanical check can find all words that end in “-ing.” It incorrectly shows a problem for these words:
  - Approved words (DURING, SOMETHING, MISSING, REMAINING)
  - Technical nouns (“load balancing,” “logging”)
  - Nouns that are not verb forms (“string”)
  - Text in code format, if the check does not remove it.
- The check finds the word, but it cannot give a correct replacement. If you replace “using” with “use,” the sentence becomes incorrect. A new sentence construction is necessary ([Rule 9.1](../section-9-writing-practices/rule-9-01.md)).
- A log message that starts with an “-ing” form frequently also has no subject. Examine it for [Rule 4.2](../section-4-sentences/rule-4-02.md).
