---
title: "Rule 3.6"
rule: "3.6"
section: "Section 3 - Verbs"
topic: "Active voice"
inherits: "../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-06.md"
status: unchanged
mechanical-check: suggests
---

# Rule 3.6 – Active voice

> **Rule 3.6** **Use the active voice. In descriptive writing, you can use the passive voice only if the agent is unknown.**

Source: [Issue 9, Rule 3.6](../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-06.md) gives the full text and the original examples.

## In software text

In software text, the agent is usually known. It is the user, the client, the server, the service, the pipeline, or a script. Write the agent as the subject of the sentence.

Use this rule for these types of text:

- **Error messages.** The passive voice does not give the component that has the problem. “Your request could not be processed” does not tell the reader which component to examine. Write “The server cannot process your request,” and give the cause. Refer to [error messages](../../text-types/error-messages.md).
- **Log messages.** Give the component that did the operation: “The load balancer closed the connection.” Refer to [log messages](../../text-types/log-messages.md).
- **Procedures and agent instructions.** The passive voice is not permitted in procedural text. Write the imperative: “Add a unit test for each new function” (Method 3). Refer to [agent instructions](../../text-types/agent-instructions.md).
- **“You” and “we.”** If the reader is the agent, write “you.” If your team or your company is the agent, write “we” (Method 4).

“The agent is unknown” tells you that the writer does not know the agent. It does not tell you that the agent is not important. In software, the agent is frequently unknown in an incident note or in a log message about data that changed. For this condition, Issue 9 lets you use the passive voice. You can also write “something” as the agent. Do not write an agent that is only a possible cause.

## Examples

- [Non-STE] Request rejected: token could not be validated.
- [STE] The server rejected the request because it could not validate the token.
- [Non-STE] The configuration file is loaded at startup.
- [STE] The service loads the configuration file when it starts.
- [Non-STE] Tests must be added for each new function.
- [STE] Add a unit test for each new function.
- [Non-STE] Your password will be reset by an administrator.
- [STE] An administrator will set a new password for you.
- [STE] The row was deleted before the end of the transaction.
  (Correct. The writer does not know which process deleted the row. The agent is unknown.)
- [STE] Something deleted the row before the end of the transaction.
  (Correct. “Something” is the agent.)
- [Neutral] The cleanup script deleted the row before the end of the transaction.
  (Incorrect if the writer does not know that the cleanup script deleted the row.)

## Review notes

- The reviewer must find if the writer knows the agent. Only a person or an agent who knows the system can make this decision. If the agent is known, the passive voice is not correct.
- The reviewer must make sure that the text is descriptive. The passive voice is not permitted in procedural text, also when the agent is unknown.
- A mechanical check can find BE and a past participle, with or without “by.” It incorrectly shows a problem for a past participle as an adjective (“The flag is disabled,” [Rule 3.3](rule-3-03.md)) and for a correct passive with an unknown agent (“The row was deleted”).
- The check does not find a passive without BE, for example “Connection closed by peer” or “File not found.” These messages also have missing words ([Rule 4.2](../section-4-sentences/rule-4-02.md)).
- A check can cause a new error. To remove the passive, a writer can add an agent that is not correct, for example “The system rejected the request,” when the proxy rejected it. An incorrect agent sends the reader to the incorrect component.
