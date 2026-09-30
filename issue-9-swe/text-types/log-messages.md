---
title: "Log messages"
kind: text-type
ste-text-type: descriptive
---

# Log messages

A log message records one operation, one change of condition, or one error in a program. Operators and developers read log messages when they find the cause of an incident. Agents also read them, frequently many thousands of lines at one time. Tools parse them and count them. The text of a log message is descriptive text (Section 6). [../SCOPE.md](../SCOPE.md) gives the types of text that are in the scope of this profile.

## Structure

A log line has these parts. The program usually sets their sequence.

1. **The time and the level.** The level, for example `INFO`, `WARNING`, or `ERROR`, is a field for tools. It is not a safety word of Section 7. Do not write the level again in the text of the message.
2. **The text of the message.** STE is for this part only.
   - Record one operation, one change of condition, or one error in each message.
   - For an operation or an error that occurred, use the simple past tense: “The worker started the task.” For a condition that continues, use the simple present tense: “The queue contains 5000 tasks.” (Rule 3.2)
   - Write a full sentence (Rule 4.2). “Connection closed by peer” omits the article and the verb.
   - If the program knows the agent, use the active voice (Rule 3.6): “The database closed the connection.” If the program does not know the agent, the passive voice is permitted: “The connection was closed.”
   - Use the same term for the same item in all messages (Rule 1.11). If a message uses “job” and a different message uses “task” for the same item, a query for one term does not find the two messages.
   - The profile does not give a rule for the letter case of the first word or for a period at the end. Use the style of the project.
3. **The fields.** Put identifiers and values in `key=value` fields or in the fields of a structured log, not in the sentence. A tool can then find all messages about one item. Use one key for one item in all messages, for example `task_id`. Do not use `task_id`, `taskId`, and `tid` for the same item. The rules of STE are not for keys and values.

Do not record passwords, tokens, or other credentials in a log message.

## Rules that matter most

- [Rule 1.11](../rules/section-1-words/rule-1-11.md): One term and one key for one item. Operators use a query to find all messages about one item. A message with a different term or key is not in the result of that query.
- [Rule 3.2](../rules/section-3-verbs/rule-3-02.md): Use the simple past tense for an operation that occurred. Do not use the progressive form (“Processing job 8812…”). Refer also to [Rule 3.5](../rules/section-3-verbs/rule-3-05.md).
- [Rule 3.6](../rules/section-3-verbs/rule-3-06.md): Use the active voice when the program knows the agent.
- [Rule 4.2](../rules/section-4-sentences/rule-4-02.md): Do not omit articles and verbs to make the message shorter.
- [Rule 7.1](../rules/section-7-safety-instructions/rule-7-01.md): The log level `WARNING` is not the safety word WARNING. A log message is not a safety instruction.
- [Rule 10.1](../rules/section-10-code-in-text/rule-10-01.md): In documentation about log messages, put the level, the keys, and the values in code format.

## Examples

Messages about one task:

[Non-STE]

```text
INFO     Processing job 8812...
WARN     Job 8812 timed out, retrying
ERROR    task 8812 failed after 3 retries
```

[STE]

```text
INFO     The worker started the task. task_id=8812
WARNING  A timeout occurred. The worker will start the task again. task_id=8812 attempt=1
ERROR    The task stopped after three timeouts. task_id=8812 attempt=3
```

(The Non-STE messages use “job” and “task” for the same item. The STE messages use “task” and the key `task_id` in all lines.)

Other messages:

- [Non-STE] `User was deleted.`
- [STE] `The administrator deleted the user. admin_id=17 user_id=4410`
  (The program knows the agent. Thus, use the active voice.)
- [Non-STE] `Cache miss for user:4410`
- [STE] `The cache did not contain the key. key=user:4410`
- [Non-STE] `Unable to reach payment gateway (will retry)`
- [STE] `The payment service did not send a response in 10 seconds. The client will try the request again. timeout_s=10`

## Review questions

- Does each message record one operation, one change of condition, or one error?
- Do all messages about one item contain the same term and the same key? Can one query find all of them?
- Is the data in fields and the text in the sentence? If a tool must get a value from the sentence, put the value in a field.
- Is the log level correct? Does a message with the `ERROR` log level show a problem that a person must correct?
- Can an operator who does not know the code find the cause of an incident from the message?
- Does the message contain a credential, or the data of a user that must not be in the log?
