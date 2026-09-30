---
title: "Agent instructions"
kind: text-type
ste-text-type: procedural
---

# Agent instructions

Agent instructions are files that tell an AI agent how to do work in a repository, for example `CLAUDE.md`, `AGENTS.md`, or the instructions of a skill. The primary reader is a large language model agent. The agent frequently reads the file without the other files of the repository. It cannot get more information from the writer, and it obeys the words of the text. Developers also read these files, and tools load them before the agent starts its work. Agent instructions are procedural text (Section 5). [../SCOPE.md](../SCOPE.md) gives the types of text that are in the scope of this profile.

## Structure

An agent instruction file has these parts, in this sequence:

1. **The scope.** One short paragraph of descriptive text (Section 6). Tell the agent the repository, the work that the file is for, and the files to read first.
2. **Mandatory instructions.** A vertical list (Rule 4.3), with one instruction in each item (Rule 5.2). Put all safety instructions of the file in this part, because the agent reads it before the tasks (Rule 7.2).
3. **Permitted tasks.** The tasks that the agent can do without an instruction from a person.
4. **Procedures.** Numbered steps for each task (Section 5). Put each safety instruction again immediately before the step or the command that has the risk (Rule 7.2).
5. **Terms.** Give each item one name, and use only that name in the file (Rule 1.11). If a name is special to the repository, tell the agent the item that it identifies.

### Mandatory instructions and permitted tasks

- Use the imperative for a mandatory instruction (Rule 5.3). The imperative is usually sufficient.
- Use MUST when the subject of the sentence is not the agent, for example “Each commit must contain one change.” Do not put MUST before an imperative instruction. Rule 5.3 lets you do this only when the instruction is very important for safety (for example, in a safety instruction), or when you give an important condition.
- Use CAN for a permitted task: “You can change files in `docs/`.”
- Write “Do not” in place of “never.” “Never” is not an approved word, and “Do not” gives the same instruction.
- Do not use “should,” “may,” “prefer,” or “try to.” With these words, the agent cannot know if the instruction is mandatory. Refer to [should (v)](../dictionary/verbs.md#should-v) and [may (v)](../dictionary/verbs.md#may-v).

### Sentences

- Write one instruction in each sentence (Rule 5.2). If a sentence contains two instructions, the agent can do only one of them.
- If the agent must know a condition first, start the instruction with the condition (Rule 5.4): “If a test fails, do not commit.”
- Use the active voice (Rule 3.6). A passive instruction, for example “Files must not be edited,” does not tell the agent who must obey the instruction.
- Use a maximum of 20 words in each instruction (Rule 5.1).

### Causes and notes

- Give the cause of an instruction if the agent must use it in conditions that the file does not give. Write the cause as one short descriptive sentence after the instruction. With the cause, the agent can make the correct decision in a new condition.
- Do not give a cause for each instruction. A cause that the agent does not use makes the file longer.
- A note gives information only (Rule 5.5). Do not put an instruction in a note, in parentheses, or in an example. The agent can think that it is optional.

### Safety instructions

Write a safety instruction (Section 7) for each step that can:

- Delete data
- Change the history of a remote branch
- Change the production environment.

Put each safety instruction in two locations (Rule 7.2):

- In the mandatory instructions, which the agent reads before the tasks
- Immediately before the step or the command that has the risk.

Write the safety instruction in this sequence:

1. Start with the word for the level of risk (Rule 7.1). Issue 9 uses CAUTION for a risk of damage to objects, and WARNING for a risk of injury or death. In this profile, data, software, and computer systems are also objects. Thus, use CAUTION for a risk of damage to data or to systems.
2. Give a clear command or condition (Rule 7.2).
3. Tell the risk (Rule 7.3).

### Code in the text

- Put paths, commands, and identifiers in code format (Rule 10.1). The agent can then use them without a change.
- Put a command that the agent must execute in a code block, after the instruction (Rule 10.3).
- Use one style of placeholder in the file, for example `<version>` (Rule 10.5). Tell the agent the value of each placeholder.

## Rules that matter most

- [Rule 5.3](../rules/section-5-procedural-writing/rule-5-03.md): The imperative or MUST shows a mandatory instruction. CAN shows a permitted task. With “should,” the agent cannot know which of the two it is.
- [Rule 5.2](../rules/section-5-procedural-writing/rule-5-02.md): One instruction in each sentence. In a long sentence, an agent can do the first instruction and not the second.
- [Rule 5.4](../rules/section-5-procedural-writing/rule-5-04.md): The condition comes first. The agent must know the condition before it reads the instruction.
- [Rule 5.5](../rules/section-5-procedural-writing/rule-5-05.md): A note gives information only. An instruction in a note is not clearly mandatory.
- [Rule 3.6](../rules/section-3-verbs/rule-3-06.md): A passive instruction does not tell the agent who must obey the instruction.
- [Rule 7.1](../rules/section-7-safety-instructions/rule-7-01.md), [Rule 7.2](../rules/section-7-safety-instructions/rule-7-02.md), [Rule 7.3](../rules/section-7-safety-instructions/rule-7-03.md): A step that can delete data or change the production environment must have a safety instruction immediately before it. The mandatory instructions must also contain this safety instruction.
- [Rule 1.11](../rules/section-1-words/rule-1-11.md): If the file uses “the repo,” “the codebase,” and “the project” for one item, the agent can think that they are three items.
- [Rule 10.1](../rules/section-10-code-in-text/rule-10-01.md), [Rule 10.3](../rules/section-10-code-in-text/rule-10-03.md), [Rule 10.5](../rules/section-10-code-in-text/rule-10-05.md): Write paths, commands, and placeholders that the agent can use without a change.

## Examples

The first three Non-STE examples are lines from the [`CLAUDE.md`](../../CLAUDE.md) file of this repository.

- [Non-STE] **Never convert PDF to markdown with a script or tool.** That means no pdftotext, pandoc, pdfplumber or similar in the transcription path.
- [STE] Do not use a script or a tool to change a PDF into markdown. For example, do not use `pdftotext`, `pandoc`, or `pdfplumber`.
  (“Never” is not approved. “That means no …” is not an instruction in the imperative (Rule 5.3). “Or similar” does not tell the agent which tools are not permitted.)
- [Non-STE] Transcription is done by agents that read rendered page images. Text extraction may be used only for rough orientation during exploration, and it must not be trusted.
- [STE] Make each transcription from the page images only. You can use a tool that gets text from a PDF only to find a page. Do not put this text in a transcription, because it can be incorrect.
  (The Non-STE text uses the passive voice for instructions to the agent (Rule 3.6). “Must not be trusted” does not tell the agent how to use the text.)
- [Non-STE] Transcribe what is printed. Never correct the source: mark errors with `<!-- sic -->` and uncertain readings with `<!-- unclear: … -->`.
- [STE] Write only the text that is on the page. Do not correct errors in the source. If the source has an error, identify it with `<!-- sic -->`. If you are not sure about a word, identify it with `<!-- unclear: … -->`.
  (The Non-STE sentence after the colon contains two instructions (Rule 5.2).)

A line from the same file that gives a cause. Keep this structure:

- [Non-STE] **Do not use poppler** (`pdftoppm`/`pdftocairo`): the PDFs reference non-embedded fonts, and poppler renders bold as regular weight.
- [STE] Do not use Poppler (`pdftoppm` or `pdftocairo`) to make page images. The PDFs do not contain their fonts, and Poppler then shows bold text as text that is not bold.
  (The cause tells the agent the problem. If a different tool has the same problem, the agent knows that it must not use that tool.)

Words that do not tell the agent if an instruction is mandatory:

- [Non-STE] Prefer small, focused commits where possible.
- [STE] Each commit must contain only one change.
- [Non-STE] You may want to update the docs if you touch the API.
- [STE] If you change the API, update the API reference in `docs/api/` in the same commit.
- [Non-STE] Feel free to clean up old branches.
- [STE] You can delete the branches that you made.

A procedure with an instruction in a note, and a step that can cause damage to data:

[Non-STE]

```markdown
## Releasing

Bump the version, tag it and push. Note: don't forget to regenerate the
changelog first. If something goes wrong you can always force-push the tag.
```

[STE]

````markdown
## Release procedure

In these steps, replace `<version>` with the new version, for example `1.4.0`. Do not include the angle brackets.

1. Make the changelog:

   ```sh
   python3 tools/changelog.py
   ```

2. Set `version` in `pyproject.toml` to `<version>`.
3. Commit the two changed files.
4. Make a tag for the new version:

   ```sh
   git tag v<version>
   ```

CAUTION: If you push an incorrect tag, do not use `git push --force` to change the tag. Other developers and the release pipeline possibly have the previous tag. Two different commits then have the same version.

5. Push the tag:

   ```sh
   git push origin v<version>
   ```
````

(The Non-STE note contains an instruction. The STE procedure puts it in step 1. The first sentence of the Non-STE text contains three instructions. The CAUTION is immediately before the step that pushes the tag. The mandatory instructions of the same file must also contain this CAUTION (Rule 7.2).)

## Review questions

- If an agent obeys only the words of each sentence, is the result correct?
- For each instruction, can the agent know if it is mandatory or permitted?
- If a condition is not in the file, does the file give the causes that the agent must know to make a correct decision?
- Does a note, a parenthesis, or an example contain an instruction that the agent must obey?
- Is there a safety instruction immediately before each step that can delete data, change the history of a remote branch, or change the production environment? Do the mandatory instructions also contain it?
- Do two instructions tell the agent different things for the same condition?
- Does the file use one term for each item? Can the agent think that two terms are two different items?
- Can the agent use each path and each command without a change? Does the file tell the agent the value of each placeholder?
