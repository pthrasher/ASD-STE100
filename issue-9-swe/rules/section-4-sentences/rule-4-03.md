---
title: "Rule 4.3"
rule: "4.3"
section: "Section 4 – Sentences"
topic: "Vertical lists"
inherits: "../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-03.md"
status: adapted
mechanical-check: suggests
---

# Rule 4.3 – Vertical lists

> **Rule 4.3** **Use a vertical list for complex text.**

Source: [Issue 9, Rule 4.3](../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-03.md) gives the full text and the original examples.

## In software text

The profile adds two interpretations for Markdown:

1. **List marks.** A Markdown list mark (`-`, `*`, or `1.`) is the mark or symbol that identifies each item. Use `1.` for steps in a procedure. Use `-` for a list of items or for descriptive text.
2. **Items that start with code.** If an item starts with text in code format, do not change the first letter of the code to uppercase. `npm` stays lowercase. If it is possible, start the item with a word: “The `npm` command …”

The other instructions of Issue 9 are applicable to Markdown lists without a change:

- Put a colon at the end of the sentence before the list.
- Start each item with an uppercase letter.
- If it is applicable, put an article before the noun that is the subject of each item.
- Put a period at the end of an item that is a full sentence. Do not put a period at the end of an item that is not a full sentence. Put a period at the end of the last item.
- Do not put a comma or a semicolon at the end of an item.
- In a safety instruction, write DO NOT in each applicable item, not only before the colon.
- Make sure that each item connects correctly to the sentence before the colon.
- Do not put procedural items and descriptive items in the same list. In agent instructions, put the instructions in one list. Put information about the project in a different paragraph.
- Do not put a second list in an item of a list of parts or items. Sub-steps of a procedure are different. Issue 9 gives sub-steps in [Rule 4.1](../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-01.md).

A command that the reader types can be a code block in a list item.

## Examples

- [Non-STE] Supported formats are JSON, YAML, TOML and INI.
- [STE] The CLI can read configuration files in these formats:
  - JSON
  - YAML
  - TOML
  - INI.
- [Non-STE] Before opening a PR:
  - run the tests,
  - lint;
  - Make sure CI is green
- [STE] Before you open a pull request, do these steps:
  1. Execute the unit tests.
  2. Execute the linter.
  3. Make sure that all pipeline checks pass.
- [Non-STE] Rules:
  - Use pnpm, not npm.
  - The API lives in packages/api.
  - Don't edit generated files.
- [STE] Obey these instructions:
  - Use `pnpm` to install packages. Do not use `npm`.
  - Do not change the files in the `src/generated/` directory. A script makes these files.
  (The Non-STE list mixes instructions and information. Put the information “The API code is in `packages/api/`” in a different paragraph.)

## Review notes

- The reviewer must find if a text is complex and must be a list. The reviewer must also find if each item connects correctly to the sentence before the colon.
- The reviewer must find if a list mixes procedural items and descriptive items. In agent instructions, a mixed list can make the agent read information as an instruction.
- A mechanical check can find these problems in the format of a list:
  - A missing colon before the list
  - An item that ends with a comma or a semicolon
  - An item that starts with a lowercase letter
  - A last item without a period.

  The check incorrectly shows a problem for items that start with code format.
- A check cannot find a long sentence that must be a list. It also cannot find an item that does not connect to the sentence before the colon.
