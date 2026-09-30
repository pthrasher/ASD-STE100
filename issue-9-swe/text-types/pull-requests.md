---
title: "Pull requests"
kind: text-type
ste-text-type: descriptive and procedural
---

# Pull requests

A pull request description tells the reviewers the changes in a branch, the cause of the changes, and how to do a test of them. Reviewers read it before they read the diff. Agents read it when they do a code review, and when they find the cause of a regression. The summary and the list of changes are descriptive text (Section 6). The test procedure is procedural text (Section 5). [../SCOPE.md](../SCOPE.md) gives the types of text that are in the scope of this profile.

## Structure

A pull request description has these parts, in this sequence:

1. **The title.** The title obeys the rules for the subject line of a commit message: the imperative, no period at the end, and no omitted articles. Refer to [commit-messages.md](commit-messages.md#structure).
2. **Summary.** One paragraph of descriptive text. Tell the change, then its cause (Rule 6.1). Give the issue number. Use a maximum of 25 words in each sentence (Rule 6.3).
3. **Changes.** A vertical list (Rule 4.3). Each item tells one change. All items are descriptive. Do not put an instruction in this list, because a vertical list must not mix procedural text and descriptive text.
4. **Test procedure.** Numbered steps (Section 5):
   - Write one instruction in each step (Rule 5.2), in the imperative (Rule 5.3).
   - If the reader must know a condition first, start the step with the condition (Rule 5.4).
   - Put each command in a code block after the instruction (Rule 10.3).
   - If a step has a risk, put the safety instruction immediately before that step (Rule 7.2).
   - Tell the result that the reader must see in the same step, after the instruction (Rule 5.2).
5. **Risks.** Include this part only if the change has a risk, for example when you deploy it. This part is not for the risks of the test steps. If the change can cause damage to data or to the production environment, write a safety instruction (Section 7).

In a safety instruction, use the word for the level of risk (Rule 7.1). Issue 9 uses CAUTION for a risk of damage to objects. In this profile, data, software, and computer systems are also objects. Thus, use CAUTION for all risks of damage to data or to systems, small and large. Use WARNING only for a risk of injury or death, for example in software that controls machines. Start with a command or a condition (Rule 7.2), then tell the risk (Rule 7.3).

## Rules that matter most

- [Rule 4.3](../rules/section-4-sentences/rule-4-03.md): The list of changes and the test procedure are two different lists. Do not mix their items.
- [Rule 6.1](../rules/section-6-descriptive-writing/rule-6-01.md): The summary gives the change and its cause before the list of changes.
- [Rule 5.2](../rules/section-5-procedural-writing/rule-5-02.md): Each step of the test procedure has one instruction. A reviewer who did not write the change must know how to do each step.
- [Rule 10.3](../rules/section-10-code-in-text/rule-10-03.md): Put each command that the reviewer executes in a code block, after the instruction.
- [Rule 7.1](../rules/section-7-safety-instructions/rule-7-01.md), [Rule 7.2](../rules/section-7-safety-instructions/rule-7-02.md), [Rule 7.3](../rules/section-7-safety-instructions/rule-7-03.md): A migration that deletes data, or a change to the production environment, must have a safety instruction. A test step that has a risk must have a safety instruction immediately before it.
- [Rule 1.11](../rules/section-1-words/rule-1-11.md): Use the same term for an item in the title, the summary, the list, and the code.

## Examples

A full description:

[Non-STE]

```markdown
## What
Adds retry logic to the webhook sender + some cleanup.

## Why
Customers have been complaining that webhooks get dropped when their endpoint is flaky.

## Testing
Ran the unit tests. You can also spin up the sender, fire a test webhook and bring the mock endpoint up after a bit to see the retry happen.

## Risk
Should be low risk, but note that the migration drops the old attempts column so make sure you have a backup.
```

[STE]

````markdown
Try webhook requests again after an error

## Summary

After this change, the webhook sender tries a request again when the endpoint of the customer does not send a response. Before this change, the sender sent each webhook one time only. Refer to issue #871.

## Changes

- The sender tries each request again a maximum of five times.
- The time between two requests increases from 1 second to 16 seconds.
- The sender records each request and its result in the new `webhook_attempts` table.
- The migration removes the `attempts` column from the `webhooks` table.

## Test procedure

1. Start the webhook sender:

   ```sh
   make webhook-sender
   ```

2. In a different terminal, send a test webhook:

   ```sh
   make send-test-webhook
   ```

   The log of the sender shows `attempt=1 status=no_response`.

3. When the log shows `attempt=2`, start the mock endpoint:

   ```sh
   make mock-endpoint
   ```

4. Make sure that the log shows `status=delivered` for the test webhook.

## Risks

CAUTION: Before you deploy this change to the production environment, make a backup of the `webhooks` table. The migration deletes the `attempts` column and its data permanently.
````

Sentences that do not give sufficient information:

- [Non-STE] Should be safe to merge, just a refactor.
- [STE] This pull request refactors the code that sends webhooks. The webhook sender operates the same as before.
- [Non-STE] Tested locally, LGTM.
- [STE] All unit tests and integration tests pass on a local computer. Do the test procedure in the test environment before you merge the pull request.

## Review questions

- After a reviewer reads only the summary, does the reviewer know the change and its cause?
- Can a person who did not write the change do the test procedure without more information from the writer?
- Does each item in the list of changes tell one change? Does the list contain only descriptive text?
- Does the list agree with the diff? For example, does it include all changes to the API, the configuration, and the database schema?
- If the change can cause damage to data or stop a service in the production environment, is there a safety instruction? Does it tell the reader the risk?
- Is the level of the safety instruction correct for the risk?
- If a test step has a risk, is the safety instruction immediately before that step?
