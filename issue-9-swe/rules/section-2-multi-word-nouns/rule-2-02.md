---
title: "Rule 2.2"
rule: "2.2"
section: "Section 2 – Multi-word nouns"
topic: "Multi-word nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-2-multi-word-nouns/rule-2-02.md"
status: adapted
mechanical-check: suggests
---

# Rule 2.2 – Multi-word nouns

> **Rule 2.2** **When a technical noun has more than three words, write it in full.**<br>
> **Then, you can use one of these methods to make the technical noun clear:**
> - **Give a shorter form of the technical noun.**
> - **Use hyphens (-) between words that you use as one unit.**

Source: [Issue 9, Rule 2.2](../../../issue-9/part-1-writing-rules/section-2-multi-word-nouns/rule-2-02.md) gives the full text and the original examples.

## In software text

The profile adds one interpretation. For method 1, the unit of text is one page. An agent frequently reads only one page. Thus, write the full technical noun the first time that it occurs on each page.

Software text contains many long technical nouns that you cannot change, for example the names of protocols, standards, cloud services, and products. Write each of these names as its owner writes it. Do not divide it, and do not change its letters or its hyphens.

Obey these instructions:

- **Shorter form (method 1).** Write the full name the first time that it occurs on the page. Then give the abbreviation in parentheses, and use only the abbreviation in the remaining text of the page. This is not applicable to an abbreviation that is a technical noun, for example [API (TN)](../../dictionary/nouns.md#api-tn).
- **Hyphens (method 2).** Use a hyphen between words that are one unit, for example “end-to-end test” or “command-line tool.” [Rule 8.7](../section-8-punctuation-and-word-count/rule-8-07.md) counts a hyphenated word as one word. Do not connect more than three words with hyphens.
- **Code format.** Do not add hyphens to text in code format, and do not remove them. A hyphen in `max-retries` is part of the name. Refer to [Rule 10.1](../section-10-code-in-text/rule-10-01.md).

If a technical noun has three words or less, an abbreviation or hyphens are not necessary. For example, write “pull request,” not “PR.” Refer to [pull request (TN)](../../dictionary/nouns.md#pull-request-tn). But if a technical noun has a hyphen, for example “command-line tool,” do not remove the hyphen.

## Examples

- [Non-STE] The service uses mTLS client cert auth.
- [STE] The service uses mutual Transport Layer Security (mTLS) for authentication. With mTLS, each client must send a certificate to the server.
  (The first sentence gives the full name and the abbreviation. The subsequent text uses the abbreviation.)
- [Non-STE] Disable the billing legacy DB write-back flag, then make sure the WB flag is off.
- [STE] Disable the `billing_legacy_write_back` feature flag (the feature flag that lets the billing service write to the previous database, referred to in this procedure as the “write-back flag”).
  (The procedure then uses only “write-back flag.” The Non-STE text uses two different short forms and does not give them in full.)
- [Non-STE] Do the end to end test suite before the release.
- [STE] Execute the end-to-end test suite before the release.
- [Non-STE] Replace the payment-service-database-read-replica credentials.
- [STE] Replace the credentials of the read replica for the payment-service database.
  (Groups of two words: “read replica” and “payment-service database.” The hyphens connect only words that are one unit.)

## Review notes

- The reviewer must find if a long technical noun is a name that the writer cannot change, for example the name of a product. If it is, the reviewer must make sure that the page gives it in full before the short form.
- The reviewer must make sure that each hyphen connects words that are one unit. An incorrect hyphen connects words that are not one unit. Then the reader can connect the words of the multi-word noun incorrectly.
- A mechanical check can find an abbreviation that has no full form on the same page. It incorrectly shows a problem for abbreviations that are technical nouns, for example “API” and “HTTP.” It cannot know if two different short forms refer to the same item ([Rule 1.11](../section-1-words/rule-1-11.md)).
- A mechanical check cannot find a technical noun of more than three words, because it cannot know where a technical noun starts and stops. It cannot know if a hyphen connects words that are related.
