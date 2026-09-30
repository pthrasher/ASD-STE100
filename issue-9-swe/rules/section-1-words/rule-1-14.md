---
title: "Rule 1.14"
rule: "1.14"
section: "Section 1 – Words"
topic: "Spelling"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-14.md"
status: adapted
mechanical-check: suggests
---

# Rule 1.14 – Spelling

> **Rule 1.14** **Use American English spelling unless other official directives tell you differently.**

Source: [Issue 9, Rule 1.14](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-14.md) gives the full text and the original examples.

## In software text

The profile adds this to the Help text of Issue 9: text in code format keeps the spelling of the code. An identifier, a field name, a configuration key, a command, or a value in code format is not a word of the text ([Rule 10.1](../section-10-code-in-text/rule-10-01.md)). If an API has a `colour` field, write `colour` in code format. In the words of the sentence, write “color.”

Quoted text also keeps its spelling ([Rule 8.6](../section-8-punctuation-and-word-count/rule-8-06.md)). Examples are the labels on a screen and the error messages of a different program.

If the style guide of a project tells you to use British English spelling, obey it. Use one spelling in all of the text.

In software text, frequent differences are “color” and “colour,” “canceled” and “cancelled,” and “initialize” and “initialise.” Some of these words are not approved ([Rule 1.1](rule-1-01.md)).

## Examples

- [Non-STE] The `colour` field sets the colour of the status icon.
- [STE] The `colour` field sets the color of the status icon.
  (`colour` is the name of the field in the API. The word “color” in the sentence has the American English spelling.)
- [Non-STE] Click “Color settings.”
  (The screen shows “Colour settings.”)
- [STE] Click “Colour settings.”
- [Non-STE] The request was cancelled by the user.
- [STE] The user canceled the request.

## Review notes

- The reviewer must find if a word is a word of the text, text in code format, or quoted text. Only a word of the text must have the American English spelling.
- A mechanical check can compare the text with a list of British English spellings. It shows possible problems.
- The check shows correct text as a possible problem. An identifier that is not in code format is an example: “Set the colour field.” The correct change is code format (`colour`), not a different spelling. If a project has a directive for British English, the check shows each correct word.
- The check does not find words that are not in its list.
- Do not let a tool replace spellings automatically in code spans or code blocks. A change from `colour` to `color` in a field name makes the code or the API request incorrect.
