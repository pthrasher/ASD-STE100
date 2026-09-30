---
title: "Error messages"
kind: text-type
ste-text-type: descriptive and procedural
---

# Error messages

An error message tells a user, an operator, or a developer that an operation did not operate correctly. It also tells the reader the step that corrects the problem. Persons frequently read an error message when they must correct a problem quickly. Agents read it to select their next step. Scripts and tools parse it, for example to find an error code. An error message is descriptive text (Section 6), then procedural text (Section 5). [../SCOPE.md](../SCOPE.md) gives the types of text that are in the scope of this profile. An error dialog in a user interface is also an error message.

## Structure

An error message has these parts, in this sequence:

1. **The problem.** One descriptive sentence. Tell the operation that stopped before its end, and the item. The program usually knows the agent. Thus, use the active voice (Rule 3.6): “The server rejected the request,” not “The request was rejected.” Do not use “failed” for a program or an operation. Refer to [fail (v)](../dictionary/verbs.md#fail-v).
2. **The cause, if the program knows it.** Give the values that are necessary to find the cause: the value that the program received, and the limit. Use BECAUSE, or write a second sentence.
3. **The correction.** An instruction in the imperative (Rule 5.3). If there is a condition, start the instruction with it (Rule 5.4). Write one instruction in each sentence (Rule 5.2). If the reader cannot correct the problem, tell the reader who can correct it. Tell the reader the data to give to that person.
4. **Data for tools.** An error code, a request ID, or other fields. Put this data after the text. The rules of STE are for the text, not for the data.

Put identifiers, paths, and values in code format (Rule 10.1). If the output cannot show code format, for example in a terminal, use the format of the program. A code span counts as one word (Rule 10.2).

Tell the problem and the correction. Do not tell the reader that they caused the problem. The reader must know how to correct the problem, not who caused it. The words “invalid” and “illegal” are not in the dictionary. BAD (adj) is approved, but “bad,” “invalid,” and “illegal” do not tell the reader the problem.

Do not show a password, a token, or other credentials in an error message.

## Rules that matter most

- [Rule 3.6](../rules/section-3-verbs/rule-3-06.md): The program usually knows the agent. Rule 3.6 lets you use the passive voice only when the agent is unknown.
- [Rule 5.3](../rules/section-5-procedural-writing/rule-5-03.md): The correction is an instruction in the imperative. “Please try again” is not an instruction that the reader can do correctly without more information.
- [Rule 5.4](../rules/section-5-procedural-writing/rule-5-04.md): If the correction has a condition, give the condition first.
- [Rule 4.2](../rules/section-4-sentences/rule-4-02.md): Do not omit words. “Config not found” omits the article and the verb.
- [Rule 9.4](../rules/section-9-writing-practices/rule-9-04.md): Use the same text each time that the same problem occurs. A person or a tool can then find all these messages in the log and in the documentation.
- [Rule 10.1](../rules/section-10-code-in-text/rule-10-01.md): Put the identifiers and the values in code format. The reader can then see which part of the text is a value from the program.

## Examples

Messages for a command-line program or an API:

- [Non-STE] Invalid port.
- [STE] The value `abc` for `--port` is not a number. Enter a number from 1 to 65535.
- [Non-STE] Error: config file could not be loaded.
- [STE] The service cannot load `/etc/app/config.yaml` because there is no file at this path. Make a configuration file at `/etc/app/config.yaml`. You can also give a different path with the `--config` flag.
- [Non-STE] You forgot to set DATABASE_URL!
- [STE] The `DATABASE_URL` environment variable is not set. Set `DATABASE_URL` to the URL of the database. Then start the service again.
- [Non-STE] Request failed: 403 Forbidden
- [STE] The server rejected the request with status `403` because the API token does not have the `write` scope. Use an API token that has the `write` scope.

A message that gives no cause and no correction:

[Non-STE]

```text
Error: Oops! Something went wrong while processing your request. Please try again later.
```

[STE]

```text
error: The backup stopped because the disk of "/var/data" is full.
Remove files from "/var/data". Then execute "app backup" again.
code=E_DISK_FULL
```

## Review questions

- Can the reader correct the problem with only the information in the message?
- Does the message give the cause, when the program knows it? Or does it give only a general statement, for example “An error occurred”?
- Does the message tell the reader that they caused the problem? Is that information necessary to correct the problem?
- If the reader cannot correct the problem, does the message tell the reader who can correct it?
- Does the message show a credential, or the data of a different user?
- Is the text the same each time that the same problem occurs? Can a person find the message in the log and in the documentation?
