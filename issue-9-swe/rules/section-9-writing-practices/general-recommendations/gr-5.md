---
title: "GR-5 False friends"
gr: "GR-5"
section: "Section 9 - Writing practices"
topic: "General recommendations"
inherits: "../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-5.md"
status: unchanged
mechanical-check: none
---

# GR-5 False friends

This recommendation tells you to make sure that a word has its English meaning, not the meaning of a word that looks the same in a different language.

Source: [Issue 9, GR-5](../../../../issue-9/part-1-writing-rules/section-9-writing-practices/general-recommendations/gr-5.md) gives the full text and the original examples.

## In software text

Many writers of software text do not have English as their first language. Some frequent false friends in software text are:

- “actual”: in German (“aktuell”) and French (“actuel”), the equivalent word gives the meaning “at this time.” In English, “actual” does not have that meaning.
- “eventually”: in German (“eventuell”), French (“éventuellement”), and Spanish (“eventualmente”), the equivalent word gives the meaning “possibly.” In English, “eventually” gives the meaning “after some time.”
- “control”: in French (“contrôler”), Italian (“controllare”), and Spanish (“controlar”), the equivalent word can give the meaning “examine.” In STE, CONTROL (v) is only for signals that adjust or operate something.
- “sensible”: in German (“sensibel”), the equivalent word gives the meaning “sensitive.”

“Actual” and “sensible” are not in the dictionary. “Eventually” is not approved, and its alternative is SOME TIME. “Control” is approved, but with a different meaning ([Rule 9.2](../rule-9-02.md)). If you use an approved word, read its approved meaning in the dictionary. Do not use the meaning of your first language.

## Examples

- [Non-STE] Print the actual config.
  (The writer wants the configuration that the service uses at this time.)
- [STE] Show the configuration that the service uses at this time.
- [Non-STE] If the queue is full, the job will eventually fail.
  (The writer wants “possibly.”)
- [STE] If the queue is full, it is possible that the task stops before its end.
- [Non-STE] Control the log file before you deploy the release.
- [STE] Examine the log file before you deploy the release.
- [Non-STE] Don't log sensible data.
- [STE] Do not record sensitive data in the log.

## Review notes

- A check cannot find a false friend. The word is correct English, and the check does not know the meaning that the writer wants.
- A check for words that are not approved finds “actual,” “eventually,” and “sensible.” It does not tell the reviewer that the writer possibly wanted a different meaning. It cannot find “control” with the meaning “examine,” because CONTROL (v) is approved.
- The reviewer must know the meaning that the text must give. If the reviewer is not sure, the reviewer must speak to the writer first.
