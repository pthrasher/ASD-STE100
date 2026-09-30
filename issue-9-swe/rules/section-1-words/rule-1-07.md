---
title: "Rule 1.7"
rule: "1.7"
section: "Section 1 – Words"
topic: "Technical nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-07.md"
status: unchanged
mechanical-check: none
---

# Rule 1.7 – Technical nouns

> **Rule 1.7** **Do not use words that are technical nouns as verbs.**

Source: [Issue 9, Rule 1.7](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-07.md) gives the full text and the original examples.

## In software text

Software text frequently uses a technical noun as a verb: “cache the result,” “log the error,” “version the API,” “e-mail the owner,” “branch off `main`.” Use a different sentence construction that keeps the word as a noun. [nouns.md](../../dictionary/nouns.md) gives the technical nouns that you cannot use as verbs, for example [cache (TN)](../../dictionary/nouns.md#cache-tn) and [log (TN)](../../dictionary/nouns.md#log-tn).

Some words are a technical noun and a technical verb, because the profile gives the two entries. Examples are commit ([TN](../../dictionary/nouns.md#commit-tn), [v](../../dictionary/verbs.md#commit-v)), build ([TN](../../dictionary/nouns.md#build-tn), [v](../../dictionary/verbs.md#build-v)), and release ([TN](../../dictionary/nouns.md#release-tn), [v](../../dictionary/verbs.md#release-v)). “Update” is also the two: Rule 1.5 gives it in category 19, and Rule 1.12 gives it in category 2 c. You can use these words as nouns and as verbs.

A word is a technical verb only if [verbs.md](../../dictionary/verbs.md) gives it, or if you can put it in a category of [Rule 1.12](rule-1-12.md). For example, “query” is a technical noun, but [query (v)](../../dictionary/verbs.md#query-v) is not approved.

[Rule 10.4](../section-10-code-in-text/rule-10-04.md) gives the same rule for commands, product names, and identifiers. Do not write “`grep` the log” or “`curl` the endpoint.”

## Examples

- [Non-STE] Cache the response for 60 seconds.
- [STE] Keep the response in the cache for 60 seconds.
- [Non-STE] Log the request ID and the status code.
- [STE] Record the request ID and the status code in the log.
- [Non-STE] Branch off `main` for each change.
- [STE] For each change, make a branch from the `main` branch.
- [Non-STE] Email the on-call engineer if the backup fails.
- [STE] If the backup stops before its end, send an e-mail to the on-call engineer.
  (“Fail” is a technical verb only for tests and checks. Refer to [fail (v)](../../dictionary/verbs.md#fail-v).)
- [Non-STE] Query the `orders` table for the row count.
- [STE] Get the row count from the `orders` table.

## Review notes

- The reviewer must find each technical noun that has the function of a verb in its sentence. Commit subjects and the first lines of docstrings frequently start with a technical noun as a verb, for example “Cache user sessions” or “Version the export format.”
- If a word is a technical noun and a technical verb in the profile, it is correct in the two functions. Examine [verbs.md](../../dictionary/verbs.md) and [nouns.md](../../dictionary/nouns.md) before you write a report about a problem.
- If no approved verb gives the meaning, and writers use the noun as a verb frequently, tell the owner of the profile. The owner can add an entry to verbs.md ([Rule 1.12](rule-1-12.md)). Do not accept the verb without an entry.
- A mechanical check cannot help. A word-list check accepts “cache” and “log” because they are in nouns.md. A part-of-speech tagger frequently gives an incorrect part of speech for the first word of a commit subject.
