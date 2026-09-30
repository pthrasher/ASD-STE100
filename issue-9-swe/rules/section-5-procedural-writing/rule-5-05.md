---
title: "Rule 5.5"
rule: "5.5"
section: "Section 5 - Procedural writing"
topic: "Notes"
inherits: "../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-05.md"
status: adapted
mechanical-check: suggests
---

# Rule 5.5 – Notes

> **Rule 5.5** **Write notes only to give information, not instructions.**

Source: [Issue 9, Rule 5.5](../../../issue-9/part-1-writing-rules/section-5-procedural-writing/rule-5-05.md) gives the full text and the original examples.

## In software text

The profile adds one decision. Rule 5.5 is applicable to all text that has the function of a note, with all labels: “Note:”, “NB:”, “Tip:”, “Important:”, and the GitHub Markdown alerts `> [!NOTE]`, `> [!TIP]`, and `> [!IMPORTANT]`. If the text contains an instruction, write the instruction as a step. If the text tells the reader about a risk of injury or a risk of damage, write a safety instruction ([Section 7](../section-7-safety-instructions/README.md)). Use the alerts `> [!WARNING]` and `> [!CAUTION]` only for safety instructions ([Rule 7.1](../section-7-safety-instructions/rule-7-01.md)).

In [agent instructions](../../text-types/agent-instructions.md), an instruction in a note is a frequent problem. An agent can read a note as information only, and not do the instruction. A limit in a note, for example a maximum time or a maximum quantity, has the same problem. Put the limit directly after the related step.

A note is descriptive text. Each sentence in a note has a maximum of 25 words ([Rule 6.3](../section-6-descriptive-writing/rule-6-03.md)).

To find instructions in notes, do the test that Issue 9 gives. Read the procedure without the notes. Make sure that the reader can do the task correctly. If the task is not correct without a note, move the information from the note into a step.

## Examples

- [Non-STE] Note: Always run `make lint` before committing.
- [STE] Before you commit your changes, execute this command:

  ```sh
  make lint
  ```

- [Non-STE] Run the benchmark. Note: p95 latency must stay under 200 ms.
- [STE] Execute the benchmark. The p95 latency must be less than 200 ms.
  (The limit comes directly after the step.)
- [Non-STE] Note: This wipes your local DB, so back up anything you want to keep.
- [STE] CAUTION: Before you execute `make reset-db`, make a backup of the local database. This command deletes all data in the local database.
  (The Non-STE note tells the reader about a risk to data. Thus, it is a safety instruction.)
- [STE] NOTE: Approximately 10 minutes are necessary for the first build, because the build downloads all the dependencies.
  (This note gives information only.)

## Review notes

- The reviewer must do the Issue 9 test: read the procedure without the notes, and make sure that the reader can do the task. A mechanical check cannot do this test.
- A mechanical check can find notes that possibly contain instructions. It finds each text with a note label, and then it shows the notes that contain “must,” “do not,” “always,” “make sure,” or a verb at the start of a sentence. These results are areas to examine.
- Where the check gives incorrect results:
  - It does not find an instruction without the imperative, for example “It is mandatory to stop the service first” (Issue 9 gives the same case).
  - It does not find a limit without “must,” for example “The maximum is 100 requests in each minute.”
  - It does not find a note that has no label, for example a sentence in parentheses after a step.
  - It shows correct text as an area to examine when the first word of a sentence is a noun that is also a verb, for example “Build output is in `dist/`.”
- The reviewer must find each note that tells the reader about a risk. That note is a safety instruction. A check cannot find a risk.
