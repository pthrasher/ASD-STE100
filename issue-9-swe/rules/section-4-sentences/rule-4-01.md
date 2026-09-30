---
title: "Rule 4.1"
rule: "4.1"
section: "Section 4 – Sentences"
topic: "Short sentences and clear sentence structures"
inherits: "../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-01.md"
status: unchanged
mechanical-check: none
---

# Rule 4.1 – Short sentences and clear sentence structures

> **Rule 4.1** **Write short and clear sentences.**

Source: [Issue 9, Rule 4.1](../../../issue-9/part-1-writing-rules/section-4-sentences/rule-4-01.md) gives the full text and the original examples.

## In software text

- **Procedural text** (installation steps in a README, runbooks, agent instructions): write one short instruction in each step, in the imperative. Put the steps in a numbered list. Refer to [Rule 5.1](../section-5-procedural-writing/rule-5-01.md) and [Rule 5.2](../section-5-procedural-writing/rule-5-02.md).
- **Descriptive text** (commit bodies, pull request descriptions, docstrings, API reference): give one topic in each sentence. Refer to [Rule 6.3](../section-6-descriptive-writing/rule-6-03.md).
- **Accurate text.** Give values, units, and names. Write identifiers, commands, and paths in code format. “May impact performance” and “Improve error handling” do not tell the reader about the change.

An agent does each instruction as it reads it. The instruction “Keep the code clean” does not give the agent a step that it can do. Thus, the agent can do a step that the writer did not want. Write each instruction as a step that the agent can do and that a reviewer can examine.

## Examples

- [Non-STE] To set up the project, clone the repo, install deps with npm, copy .env.example to .env and fill in your keys, and then run the dev server.
- [STE] Prepare the project as follows:
  1. Clone the repository.
  2. Install the dependencies with `npm install`.
  3. Copy `.env.example` to `.env`.
  4. In `.env`, write your API keys.
  5. Start the development server with `npm run dev`.
- [Non-STE] The worker pulls jobs off the queue, retries failed ones with exponential backoff, and writes results to S3, where they're kept for 30 days.
- [STE] The worker gets tasks from the queue. If a task stops before its end, the worker tries it again after an interval. Each interval is longer than the interval before it. The worker writes the results to S3. S3 keeps the results for 30 days.
- [Non-STE] This change may impact performance.
- [STE] This change increases the response time of the `/search` endpoint by approximately 20 ms.
- [Non-STE] Keep PRs small and focused.
- [STE] Put only one change in each pull request.

## Review notes

- The reviewer must find if each sentence is clear and accurate for its reader. If the reader is an agent, the reviewer must read each instruction as the agent reads it. Then the reviewer must find each sentence that can have two meanings for the agent.
- The reviewer must find if each descriptive sentence has only one topic.
- A mechanical check can count the words in a sentence. That is a check for [Rule 5.1](../section-5-procedural-writing/rule-5-01.md) and [Rule 6.3](../section-6-descriptive-writing/rule-6-03.md). A short sentence can be not clear or not accurate, and a check cannot find this. Thus, this rule has no mechanical check.
- To make a sentence shorter, a writer can remove words that are necessary. [Rule 4.2](rule-4-02.md) does not let you do this.
