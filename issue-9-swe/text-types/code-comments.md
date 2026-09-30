---
title: "Code comments"
kind: text-type
ste-text-type: descriptive
---

# Code comments

A code comment gives information about code that the code does not show: a cause, a limit, or a decision. Developers and agents read comments when they change the code. An agent can think that a comment is an instruction. Thus, an unclear comment can cause an incorrect change. Comments are descriptive text (Section 6). A comment that tells the reader to do something, for example a `TODO` comment, is an instruction (Section 5). [../SCOPE.md](../SCOPE.md) gives the types of text that are in the scope of this profile. For docstrings, refer to [api-reference.md](api-reference.md).

## Structure

A comment has these parts:

1. **The position.** Put the comment directly before the code that it is about. A comment at the end of a line is only for a short statement about that line.
2. **The information.** Tell the cause of the code, not the operation that the code shows. A developer can read `retries += 1`. The developer cannot read the limit of the payment API that is the cause of this line.
   - Use the simple present tense for the code and its conditions (Rule 3.2).
   - Use a maximum of 25 words in each sentence (Rule 6.3). Use one topic in each comment (Rule 6.5).
   - Do not use “should.” If a condition always occurs, tell the reader the condition and its cause. If a developer must make the condition occur, write MUST or an instruction. Refer to [should (v)](../dictionary/verbs.md#should-v).
   - Put identifiers in code format (Rule 10.1). If the project uses a different format for identifiers in comments, use that format.
3. **The instruction, if there is one.** A `TODO` comment, or a comment that tells a developer not to change something, is an instruction. Write it in the imperative (Rule 5.3). If there is a condition, give it first (Rule 5.4). Give the issue number, for example `TODO(#512):`.

Do not record the history of the code in a comment. Write the changes, their authors, and their causes in the commit message. Refer to [commit-messages.md](commit-messages.md).

## Rules that matter most

- [Rule 6.1](../rules/section-6-descriptive-writing/rule-6-01.md): Give the information that the reader does not have. Do not tell the reader the operation that the code shows.
- [Rule 3.2](../rules/section-3-verbs/rule-3-02.md): Use the simple present tense. “We changed this because …” is history. Write it in the commit message.
- [Rule 5.3](../rules/section-5-procedural-writing/rule-5-03.md): A `TODO` is an instruction. Write it in the imperative, with the step and its condition.
- [Rule 5.5](../rules/section-5-procedural-writing/rule-5-05.md): A comment that starts with `NOTE:` gives information only. If the developer must obey it, write an instruction.
- [Rule 1.11](../rules/section-1-words/rule-1-11.md): Use the names of the code. If the code uses `session`, do not write “the connection” in the comment.
- [Rule 4.2](../rules/section-4-sentences/rule-4-02.md): Do not omit articles and verbs. A comment of three words is frequently not clear.

## Examples

- [Non-STE] `i += 1  # increment i`
  (The comment tells the reader only the operation that the code shows. Remove the comment.)
- [Non-STE] `# sleep a bit so the API doesn't rate-limit us`
- [STE] `# The payment API rejects more than 10 requests each second from one client.`
- [Non-STE] `// This should never be null here`
- [STE] ``// The constructor sets `session`. Thus, `session` is not null here.``
- [Non-STE] `# TODO: fix this hack`
- [STE] `# TODO(#512): Remove this conversion after all clients use version 2 of the API.`

A comment that contains history and an unclear instruction:

[Non-STE]

```python
# Changed this to UTC because of the DST bug (see #301). Should probably
# be moved into utils at some point. Don't touch the offset!
offset = tz.utcoffset(now)
```

[STE]

```python
# The scheduler stores all times in UTC. Local times cause a bug when
# the clocks change for daylight saving time. Refer to issue #301.
# Do not change this offset. The billing reports use it.
offset = tz.utcoffset(now)
```

## Review questions

- Does the comment give information that the code cannot show, for example a cause, a limit, or a decision?
- Can an agent that reads only the comment make an incorrect change? For example, can the agent think that a statement is an instruction?
- Does the comment agree with the code after this change?
- Does each `TODO` give the step, the condition, and an issue number? Can a person find it and know when to do it?
- Does the comment contain history that the commit message must contain?
- Does a comment use “should” for a condition? Does the condition always occur, or must a developer make it occur?
