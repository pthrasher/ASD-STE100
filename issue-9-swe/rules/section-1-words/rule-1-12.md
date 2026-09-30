---
title: "Rule 1.12"
rule: "1.12"
section: "Section 1 – Words"
topic: "Technical verbs"
inherits: "../../../issue-9/part-1-writing-rules/section-1-words/rule-1-12.md"
status: adapted
mechanical-check: none
---

# Rule 1.12 – Technical verbs

> **Rule 1.12** **You can use verbs that you can include in a technical verb category.**

Source: [Issue 9, Rule 1.12](../../../issue-9/part-1-writing-rules/section-1-words/rule-1-12.md) gives the full text, the four categories, and the original examples.

## In software text

The profile adds [verbs.md](../../dictionary/verbs.md), a glossary of technical verbs for software. Each entry gives the category, the meaning, and a Limit field if you can use the verb only in some text. For example, [push (v)](../../dictionary/verbs.md#push-v) is only for version control. verbs.md also gives alternatives for frequent software verbs that are not approved.

Most software verbs are in **category 2, computer processes and applications**:

- 2 a, input and output processes: “enter,” “type,” “click.”
- 2 b, user interface and application processes: “delete,” “enable,” “save,” “validate.”
- 2 c, system operations: “install,” “boot,” and the software verbs of the profile, for example “deploy,” “commit,” and “merge.”

The other categories are usually not applicable to software text.

### The test for a technical verb

Before you use a technical verb, do this test: can an approved verb give the instruction or the information accurately? If it can, use the approved verb. Also, if an approved verb and a technical noun can give the same information, use them. For example, write “send a query to the database,” not “query the database.” The decisions in verbs.md use this test.

- **“Execute” is a technical verb, and “run” is not.** The software meaning is: to make a computer do the instructions of a program, a script, a command, or a test. The Issue 9 dictionary gives “execute” as not approved. But Rule 1.12 lets you use a word that is not approved as a technical verb, if you can put it in a category. The profile puts “execute” in category 2 c (system operations). No approved verb gives this meaning accurately:
  - DO has the meaning “To complete a procedure, task, or step.” With DO, the reader does the work. Use DO for a set of steps.
  - OPERATE has the meaning “To put, keep, or be in action.” Use it for a machine or a system that continues to operate. “Operate the unit tests” has no clear meaning ([Rule 9.1](../section-9-writing-practices/rule-9-01.md)).
  - START tells only the start of an operation. Use it for a service that continues to operate.

  Rule 1.12 also tells you: “Do not use technical verbs that are general or not clear.” “Run” has many meanings in general English. “Execute” has only one meaning in software. [Rule 1.10](rule-1-10.md) tells you to use words that are “well-known,” not slang or jargon. Its example “brick” is a verb. “Execute” is the usual term in software, not jargon. Refer to [execute (v)](../../dictionary/verbs.md#execute-v) and [run (v)](../../dictionary/verbs.md#run-v).
- **“Commit” is a technical verb.** No approved verb gives its meaning accurately: to record a set of changes in the history of a repository. RECORD (v) gives a part of the meaning, but “record the changes” does not tell the reader which operation to do. Refer to [commit (v)](../../dictionary/verbs.md#commit-v).

A word in a category is a technical verb only in the subject field of that category. “Fire” is in category 3 c (civil and military operations). “Land” is in category 3 d (navigation). “Spin” is in category 1 f (change the shape of a material). “Fire an event,” “land a change,” and “spin up a server” are not STE.

A technical verb obeys the rules of [Section 3](../section-3-verbs/README.md), the same as an approved verb.

## Examples

- [Non-STE] Run the unit tests before you push.
- [STE] Execute the unit tests before you push the branch.
- [Non-STE] Spin up the dev server.
- [STE] Start the development server.
- [Non-STE] Fire a `user.created` event after the insert.
- [STE] Send a `user.created` event after the function adds the row.
- [Non-STE] Land the change after the code review.
- [STE] Merge the pull request after the code review.

## Review notes

- The reviewer must make a decision for each technical verb: can an approved verb give the same instruction or information accurately? A mechanical check cannot make this decision.
- If a verb is not in verbs.md, the reviewer must find its category. If the verb has a category and no approved verb gives its meaning, tell the owner of the profile. The owner can add an entry to verbs.md.
- Examine the Limit field. “Pull the data from the API” is not permitted, because [pull (v)](../../dictionary/verbs.md#pull-v) is only for version control. [fail (v)](../../dictionary/verbs.md#fail-v) is only for tests and checks.
- A mechanical check cannot help. A check can find verbs that are not in the dictionaries ([Rule 1.1](rule-1-01.md)). It cannot tell if an approved verb gives the same meaning. It accepts “fire” and “land” because they are in the category lists of Issue 9.
