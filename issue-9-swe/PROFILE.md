---
title: "How this profile relates to Issue 9"
kind: specification
---

# How this profile relates to Issue 9

This file is the specification for the software profile. It tells you how the profile uses Issue 9, which decisions the profile makes, and how each page is written. Writers and reviewers of this profile must obey it.

## 1. Issue 9 is the base

The profile does not replace ASD-STE100 Issue 9. It adds decisions for software text to Issue 9.

- The transcription of Issue 9 is in [../issue-9/](../issue-9/README.md). It is the source for all rules and all dictionary entries.
- If the profile gives a decision about a rule or a word, use the decision of the profile.
- If the profile does not give a decision, Issue 9 is applicable without a change.
- The profile does not change the text of `issue-9/`. That folder is a transcription of the printed standard.

This profile is not an ASD publication. ASD did not examine it or give its approval.

## 2. What the profile adds

The profile adds four types of content:

1. **Rule pages.** Each rule of Issue 9 has a page in [rules/](rules/README.md). The page gives the rule statement, tells you how to use the rule for software text, and gives software examples. Section 10 contains new rules for code in text.
2. **Dictionary decisions.** [dictionary/](dictionary/README.md) gives technical verbs and technical nouns for software. It also gives software alternatives for words that are not approved.
3. **Text-type guides.** [text-types/](text-types/README.md) tells you how to use the rules for commit messages, error messages, agent instructions, and other types of text in [SCOPE.md](SCOPE.md).
4. **Review guidance.** [review/](review/README.md) tells you how to examine a text. It also tells you the problems that a mechanical check can find and the problems that it cannot find.

## 3. Decisions

Each dictionary entry has a Decision field. The field has one of these values:

| Value | Meaning |
|---|---|
| `standard` | Issue 9 gives this status. For example, Rule 1.12 gives “delete” as a technical verb in category 2 b. |
| `proposed` | The profile gives this status. The owner of the profile did not examine it yet. |
| `accepted` | The owner of the profile examined a `proposed` decision and accepted it. |

Rule 1.12 controls all verb decisions. Use a technical verb only if no approved verb gives the instruction or the information accurately. If an approved verb and a technical noun can give the same information, use them.

A word can be approved in Issue 9 with a meaning that is not a software meaning, for example DEPLOY, PUSH, and RELEASE. The profile can give a software meaning of that word as a technical verb. Rule 1.3 is also applicable to the Issue 9 meaning.

## 4. Links to Issue 9

- Each rule page links to its source rule in Issue 9. Use a relative path, for example `../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-06.md`.
- Each dictionary entry that has an Issue 9 entry links to it, for example `../../issue-9/part-2-dictionary/words/r.md#run-v`.
- Do not copy the text of Issue 9 into the profile. Quote the rule statement only. The Issue 9 page gives the full text and the original examples.
- The rule statement in a rule page must be the same as the statement in Issue 9, word for word.

## 5. Rule pages

A rule page has this front matter:

```yaml
---
title: "Rule 3.6"
rule: "3.6"                 # for a general recommendation: gr: "GR-1"
section: "Section 3 - Verbs"
topic: "Active voice"
inherits: "../../../issue-9/part-1-writing-rules/section-3-verbs/rule-3-06.md"   # new rules: none
status: adapted              # unchanged | adapted | new
mechanical-check: suggests   # detects | suggests | none
---
```

The values of `status` are:

- `unchanged`: The rule is applicable to software text as Issue 9 writes it. The page adds software examples only.
- `adapted`: The rule is applicable, and the profile adds a decision or an interpretation for software text. The page gives the addition.
- `new`: The rule is not in Issue 9. Only Section 10 has new rules.

The values of `mechanical-check` are:

- `detects`: A mechanical check can find all text that has the pattern of this rule. A person must also find if each result is an error.
- `suggests`: A mechanical check can show possible problems. It does not find all of them, and it shows some text that is correct.
- `none`: A mechanical check cannot help. Only a person or an agent who reads the text can use the rule.

No value shows that a mechanical check can prove compliance. [review/LIMITS.md](review/LIMITS.md) gives the causes.

A rule page has these parts, in this sequence:

1. The heading: `# Rule 3.6 – Active voice`.
2. The rule statement as a block quote, the same as in Issue 9: `> **Rule 3.6** **Use the active voice. …**`
3. A source line, for example: `Source: [Issue 9, Rule 3.6](<path>) gives the full text and the original examples.` The path is the same as the `inherits` path.
4. `## In software text`: How to use the rule for software text. If the status is `adapted`, the first paragraph tells you what the profile adds.
5. `## Examples`: Pairs of software examples. Refer to [Examples](#6-examples).
6. `## Review notes`: The items that a reviewer must find by judgment. The items that a mechanical check can find, and the conditions where it fails.

## 6. Examples

Write each example as a list item with a tag, as in Issue 9:

```markdown
- [Non-STE] Pushing to main triggers the deploy pipeline.
- [STE] When you push to the `main` branch, the deployment pipeline starts.
```

- Put the Non-STE example first, then the STE example.
- To give an explanation, add a line in parentheses under the example, with an indent of two spaces.
- A `[Neutral]` example is an example that is not STE and is not an error. Use it only when the rule page must show a construction without a judgment.
- An `[STE]` example must contain only:
  - approved words of Issue 9, in their approved meaning and part of speech
  - technical nouns and technical verbs that the profile gives in [dictionary/](dictionary/README.md), or that you can put in a category of Rule 1.5 or Rule 1.12
  - text in code format
- Use realistic software text for the Non-STE examples: text that a developer or an agent can possibly write.

## 7. Dictionary entries

A dictionary entry uses the heading format of Issue 9, `## word (part of speech)`, so that one search finds entries in the two dictionaries. The part of speech of a technical noun is `TN`.

| Field | Meaning |
|---|---|
| `Profile status` | `approved`, `technical verb`, `technical noun`, or `not approved` |
| `Limit` | The contexts where you can use the word, if they are fewer than all software text |
| `Decision` | `standard`, `proposed`, or `accepted`. Refer to [Decisions](#3-decisions). |
| `Basis` | The rule and the category that let you use the word |
| `Issue 9` | The Issue 9 entry and its status. “Not in the dictionary” if there is no entry. |
| `Meaning` | The meaning that you can use. An `STE:` example follows. |
| `Alternative` | For a word that is not approved: a word to use. `STE:` and `Non-STE:` examples follow. |
| `Do not use` | For a technical noun: other terms for the same item (Rule 1.11) |
| `Note`, `Related` | Other information and links |

## 8. The language of this profile

Write the pages of this profile in STE, as the profile defines it. The rule statements, the explanations, and the review notes must obey the rules. The Non-STE examples are the only text that does not obey them.

This is a target, not a claim. [review/LIMITS.md](review/LIMITS.md) gives the causes: no page can prove its own compliance.
