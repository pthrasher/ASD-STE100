---
title: "Commit messages"
kind: text-type
ste-text-type: descriptive
---

# Commit messages

A commit message records a change in the history of a repository. Developers read it during a code review and when they find the cause of a bug. Agents read it to find the commit that caused a regression. Tools parse the subject line: for example, `git log --oneline` shows only that line. A commit message is descriptive text (Section 6), with a subject line in the imperative. [../SCOPE.md](../SCOPE.md) gives the types of text that are in the scope of this profile.

## Structure

A commit message has these parts, in this sequence:

1. **The subject line.**
   - Write the subject line in the imperative, for example “Add,” “Remove,” or “Correct.” Git uses this form. Rule 3.2 lets you use the imperative, and an imperative sentence does not omit a word (Rule 4.2). Refer to [Rule 5.3](../rules/section-5-procedural-writing/rule-5-03.md).
   - Use a maximum of 50 characters. Do not put a period at the end.
   - Tell the change that the commit makes. Do not tell the work that you did.
   - Do not omit articles to make the line shorter (Rule 4.2). If the line is too long, use a different construction (Rule 9.1).
   - Do not use “fix.” Use CORRECT (v). Refer to [fix (v)](../dictionary/verbs.md#fix-v).
2. **An empty line.** Git uses the empty line to divide the subject line from the body.
3. **The body.** The body is descriptive text. Give the information gradually (Rule 6.1), in this sequence:
   1. The change. Use the active voice, with the commit or the code as the subject: “This commit adds …” (Rule 3.6).
   2. The cause of the change. Tell the problem that occurred before the change. Use the simple past tense for the condition before the change (Rule 3.2). Use the simple present tense for the code after the change.
   3. Other information that a reader must know. For example: a new default value, a change to the API, or a limit of the change.

   Use a maximum of 25 words in each sentence (Rule 6.3). Use one paragraph for each topic (Rule 6.5). Put identifiers, paths, and values in code format (Rule 10.1). Put a line break after a maximum of 72 characters. This limit comes from the style of git, not from a rule of STE.
4. **The trailers.** Put the issue number in a trailer at the end, for example `Refs: #412`. Trailers and the keywords that an issue tracker reads (for example `Fixes #412`) are data for tools. The rules of STE are for the text of the message, not for these keywords.

## Rules that matter most

- [Rule 5.3](../rules/section-5-procedural-writing/rule-5-03.md): The subject line is an imperative. The body is not a list of instructions.
- [Rule 3.6](../rules/section-3-verbs/rule-3-06.md): The writer knows the agent of the change. Write “This commit removes the cache,” not “The cache was removed.”
- [Rule 3.2](../rules/section-3-verbs/rule-3-02.md): Do not use the present perfect tense. Write “The client did not stop,” not “The client has been hanging.”
- [Rule 4.2](../rules/section-4-sentences/rule-4-02.md): A subject line with 50 characters frequently omits articles. Write a shorter sentence. Do not remove the articles.
- [Rule 6.1](../rules/section-6-descriptive-writing/rule-6-01.md): Give the change first, then its cause, then the other information.
- [Rule 1.11](../rules/section-1-words/rule-1-11.md): Use the same name for an item as the code and the issue use.
- [Rule 10.4](../rules/section-10-code-in-text/rule-10-04.md): Do not use a command, a product name, or an identifier as a verb, for example “Dockerize” or “grep.”

## Examples

A commit that adds a timeout:

[Non-STE]

```text
Fixed bug where uploads would hang forever

Uploads were getting stuck because we weren't setting a timeout on the
socket, so if S3 was slow the client would just wait. Added a 30s
timeout + retries w/ backoff.

Fixes #412
```

[STE]

```text
Add a timeout to requests in the storage client

This commit adds a timeout of 30 seconds to each request that the
storage client sends. After a timeout occurs, the client tries the
request again a maximum of three times. The client waits 1 second
before the second request, 2 seconds before the third request, and
4 seconds before the fourth request.

Before this change, the client did not set a timeout on the socket.
When the storage service was slow, the request continued without a
limit.

Refs: #412
```

A commit that refactors code:

[Non-STE]

```text
Refactored auth middleware, cleaned up some stuff

I've moved the token validation logic out of the handlers since it was
getting duplicated in a few places. Should be no functional change.
```

[STE]

```text
Validate API tokens in one middleware function

This commit refactors the code that validates API tokens. Before this
change, the handlers of `/orders`, `/users`, and `/invoices` each had a
copy of this code. After this change, only the `requireToken`
middleware function validates API tokens.

The API operates the same as before.
```

Subject lines:

- [Non-STE] Fix crash on empty config
- [STE] Return an error for an empty configuration file
- [Non-STE] Dockerize the API server
- [STE] Add a `Dockerfile` for the API server
  (Rule 10.4: do not use a product name as a verb.)
- [Non-STE] Bump lodash
- [STE] Update `lodash` to version 4.17.21

## Review questions

- Does the subject line tell the change that the commit makes, and not the work of the writer?
- Can a developer find this commit from only the subject line, for example in the output of `git log --oneline`?
- Does the body give the cause of the change? A developer who reads the commit in two years does not know the problem that occurred.
- Does the body tell the effects that the diff does not show, for example a change to a default value or to the API?
- Does the commit contain only one change? If the subject line must contain “and,” the commit possibly contains two changes.
- Do the names in the message agree with the names in the code and in the issue?
- Did the writer omit articles or verbs to make the subject line shorter? If yes, a different construction is necessary.
