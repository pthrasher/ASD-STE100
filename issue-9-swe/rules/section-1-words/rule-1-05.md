---
title: "Rule 1.5"
rule: "1.5"
section: "Section 1 – Words"
topic: "Technical nouns"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-05.md"
status: adapted
mechanical-check: none
---

# Rule 1.5 – Technical nouns

> **Rule 1.5** **You can use words that you can include in a technical noun category.**

Source: [Issue 9, Rule 1.5](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-05.md) gives the full text, the twenty-two categories, and the original examples.

## In software text

The profile adds [nouns.md](../../dictionary/nouns.md), a glossary of technical nouns for software. It gives one term for each item ([Rule 1.11](rule-1-11.md)), and the terms that you must not use for that item. A noun that is not in nouns.md can be correct. If you can put it in a category of this rule, you can use it.

The categories that are important for software text are:

- **Category 19, computer science, information and communication technology.** Most technical nouns of software text are in this category, for example “repository,” “endpoint,” “cache,” and “stack trace.” Most entries in nouns.md are in category 19.
- **Category 6, systems, components and circuits, their functions, configurations, and parts:** “hardware,” “standby mode.”
- **Category 7, mathematical, scientific, engineering terms, and formulas:** Issue 9 gives “configuration,” “failure,” and “load” in this category.
- **Category 9, numbers, units of measurement and time:** “30 seconds,” “512 MB,” “version 2.4.”
- **Category 10, quoted text:** the labels of buttons, menus, and fields on a screen, for example “Save changes.”
- **Category 11, professional roles, individuals, and groups:** “user,” “on-call engineer,” “platform team.”
- **Category 15, documentation:** “section,” “table,” “figure,” “README.”

The other categories (for example vehicles, parts of the body, food, and animals) are usually not applicable to software text.

A technical noun must refer to a specified concept of a subject field. Words such as “stuff,” “thing,” and “logic” do not refer to a specified item. They are not technical nouns.

## Examples

- [Non-STE] Put the shared stuff for the tests in `conftest.py`.
- [STE] Put the fixtures for all tests in `conftest.py`.
  (“Fixture” is a technical noun, category 19.)
- [Non-STE] Click the blue button at the top.
- [STE] Click “Deploy” at the top of the page.
  (“Deploy” is text on the screen, category 10.)
- [Non-STE] Wait a bit before retrying.
- [STE] Wait 30 seconds. Then try the request again.
  (“30 seconds” is category 9.)
- [Non-STE] If the alert fires, ping the on-call.
- [STE] If the monitoring system sends an alert, tell the on-call engineer.
  (“Alert” and “monitoring system” are category 19. “On-call engineer” is category 11.)
- [Non-STE] See the Troubleshooting bit of the README.
- [STE] Refer to the “Troubleshooting” section of the README.
  (“Section” and “README” are category 15.)

## Review notes

- For each noun that is not in the Issue 9 dictionary, find if it is the name of a specified concept. Then find its category. If it is in no category, the noun is not permitted.
- A technical noun must also obey [Rule 1.9](rule-1-09.md), [Rule 1.10](rule-1-10.md), and [Rule 1.11](rule-1-11.md). A noun that is in a category can also be jargon, for example “repo.”
- If a text uses a technical noun frequently and nouns.md does not give it, tell the owner of the profile. The owner can add an entry to nouns.md.
- A mechanical check cannot put a word in a category. A check that accepts all nouns that are not in the dictionary also accepts “stuff” and “thing.” A check that shows all of these nouns shows each correct technical noun as a possible problem. Rule 1.1 has the check that compares words with the dictionary.
