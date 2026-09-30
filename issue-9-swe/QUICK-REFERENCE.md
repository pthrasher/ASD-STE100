---
title: "Quick reference"
kind: guidance
---

# Quick reference

This page gives the minimum that you must know to write software text in STE. Load it before you write. It does not replace the rule pages: each rule links to its page.

## Limits

| Item | Limit | Rule |
|---|---|---|
| Sentence in procedural text (an instruction) | 20 words maximum | [5.1](rules/section-5-procedural-writing/rule-5-01.md) |
| Sentence in descriptive text | 25 words maximum | [6.3](rules/section-6-descriptive-writing/rule-6-03.md) |
| Paragraph | 6 sentences maximum, one topic | [6.5](rules/section-6-descriptive-writing/rule-6-05.md), [6.6](rules/section-6-descriptive-writing/rule-6-06.md) |
| Instruction | one action, in the imperative | [5.2](rules/section-5-procedural-writing/rule-5-02.md), [5.3](rules/section-5-procedural-writing/rule-5-03.md) |
| Multi-word noun | 3 words maximum | [2.1](rules/section-2-multi-word-nouns/rule-2-01.md) |
| Semicolon | do not use | [8.1](rules/section-8-punctuation-and-word-count/rule-8-01.md) |
| Code span | counts as one word | [10.2](rules/section-10-code-in-text/rule-10-02.md) |

## Words that writers use incorrectly most frequently

These words are not approved. Use the alternative that keeps the meaning. If no alternative keeps the meaning, write a different sentence (Rule [9.1](rules/section-9-writing-practices/rule-9-01.md)).

| Do not write | Write | Example in STE |
|---|---|---|
| should | MUST, the imperative, or IF | Write tests for each new function. |
| may | CAN, POSSIBLY | This operation can continue for a maximum of 10 minutes. |
| need, require | NECESSARY, MUST | Python 3.12 or a subsequent version is necessary. |
| allow | LET | This flag lets the script continue after an error. |
| never | DO NOT | Do not push to the `main` branch. |
| run | execute (a program, a script, a command, or a test), START (a service), DO (a set of steps), OPERATE (a machine, or a system that continues to operate) | Execute the unit tests. Start the service. |
| create, generate | MAKE | Make a branch for each change. |
| check, verify | MAKE SURE, EXAMINE | Make sure that the tests pass. |
| fix | CORRECT, REPAIR | This commit corrects a bug in the parser. |
| fail (for a program) | DOES NOT … CORRECTLY, FAILURE | If the service does not start, examine the log. |
| restart, retry | START … AGAIN, TRY … AGAIN | Start the service again. |
| log (v) | RECORD | The service records each request in the log. |
| trigger | START, CAUSE | An empty input causes this error. |
| every, any | ALL, EACH | Each commit must contain only one change. |
| both, either | THE TWO, ONE OF THE TWO, OR | |
| however | BUT | |
| via | THROUGH | |
| so that | UNTIL, PREVENT, or a different sentence | |
| e.g., i.e., etc. | FOR EXAMPLE, THAT IS, OR OTHER …, or omit the abbreviation | |

The profile lets you use some software verbs as technical verbs, for example execute, commit, merge, deploy, build, call, return, parse, and (for tests only) pass and fail. [dictionary/verbs.md](dictionary/verbs.md) gives each verb and its limits. [dictionary/nouns.md](dictionary/nouns.md) gives one term for each item, for example “repository,” not “repo.”

## Code in text

- Put identifiers, commands, file paths, and values that the reader types in code format (Rule [10.1](rules/section-10-code-in-text/rule-10-01.md)).
- Put a command that the reader must execute in a code block after the instruction (Rule [10.3](rules/section-10-code-in-text/rule-10-03.md)).
- Do not use a command or a product name as a verb. Write “Use `grep` to find …,” not “grep for …” (Rule [10.4](rules/section-10-code-in-text/rule-10-04.md)).

## All rules

<!-- index:start -->
**Section 1 – Words**

- [1.1](rules/section-1-words/rule-1-01.md) Use words that are: Approved in the dictionary; Technical nouns; Technical verbs.
- [1.2](rules/section-1-words/rule-1-02.md) Use approved words from the dictionary only as the specified part of speech.
- [1.3](rules/section-1-words/rule-1-03.md) Use approved words only with their approved meanings.
- [1.4](rules/section-1-words/rule-1-04.md) Use only the approved forms of verbs and adjectives.
- [1.5](rules/section-1-words/rule-1-05.md) You can use words that you can include in a technical noun category.
- [1.6](rules/section-1-words/rule-1-06.md) Use a word that is not approved in the dictionary, only when it is a technical noun or part of a technical noun.
- [1.7](rules/section-1-words/rule-1-07.md) Do not use words that are technical nouns as verbs.
- [1.8](rules/section-1-words/rule-1-08.md) Use technical nouns that are approved in your company, industry, or subject field.
- [1.9](rules/section-1-words/rule-1-09.md) When you must select a technical noun, use one which is short and easy to understand.
- [1.10](rules/section-1-words/rule-1-10.md) Do not use regional, slang, or jargon words as technical nouns.
- [1.11](rules/section-1-words/rule-1-11.md) Do not use different technical nouns for the same item.
- [1.12](rules/section-1-words/rule-1-12.md) You can use verbs that you can include in a technical verb category.
- [1.13](rules/section-1-words/rule-1-13.md) Do not use technical verbs as nouns.
- [1.14](rules/section-1-words/rule-1-14.md) Use American English spelling unless other official directives tell you differently.

**Section 2 – Multi-word nouns**

- [2.1](rules/section-2-multi-word-nouns/rule-2-01.md) Write multi-word nouns of no more than three words.
- [2.2](rules/section-2-multi-word-nouns/rule-2-02.md) When a technical noun has more than three words, write it in full. Then, you can use one of these methods to make the technical noun clear: Give a shorter form of the technical noun.; Use hyphens (-) between words that you use as one unit.

**Section 3 - Verbs**

- [3.1](rules/section-3-verbs/rule-3-01.md) Use only the verb forms that are given in the dictionary.
- [3.2](rules/section-3-verbs/rule-3-02.md) Use only these verb forms and tenses of verbs: The infinitive form; The imperative form (command form); The simple present tense; The simple past tense; The simple future tense; The past participle form (as an adjective).
- [3.3](rules/section-3-verbs/rule-3-03.md) Use the past participle form as an adjective.
- [3.4](rules/section-3-verbs/rule-3-04.md) Do not use auxiliary verbs to make complex verb constructions.
- [3.5](rules/section-3-verbs/rule-3-05.md) Use the “-ing” form of a verb only as a technical noun or as a modifier in a technical noun.
- [3.6](rules/section-3-verbs/rule-3-06.md) Use the active voice. In descriptive writing, you can use the passive voice only if the agent is unknown.
- [3.7](rules/section-3-verbs/rule-3-07.md) Use an approved verb to describe an action, not a noun or other parts of speech.

**Section 4 – Sentences**

- [4.1](rules/section-4-sentences/rule-4-01.md) Write short and clear sentences.
- [4.2](rules/section-4-sentences/rule-4-02.md) Do not omit words or use contractions to make your sentences shorter.
- [4.3](rules/section-4-sentences/rule-4-03.md) Use a vertical list for complex text.
- [4.4](rules/section-4-sentences/rule-4-04.md) Use connecting words and connecting phrases to connect sentences that contain related topics.
- [4.5](rules/section-4-sentences/rule-4-05.md) When applicable, use an article (the, a, an) or a demonstrative adjective (this, these) before a noun or a multi-word noun.

**Section 5 - Procedural writing**

- [5.1](rules/section-5-procedural-writing/rule-5-01.md) Write short sentences. Use a maximum of 20 words in each sentence.
- [5.2](rules/section-5-procedural-writing/rule-5-02.md) Write only one instruction in each sentence unless two or more actions occur at the same time.
- [5.3](rules/section-5-procedural-writing/rule-5-03.md) Write instructions in the imperative (command) form.
- [5.4](rules/section-5-procedural-writing/rule-5-04.md) When there is a condition that the reader must know about first, start the instruction with a descriptive statement. Then, divide that descriptive statement from the command with a comma.
- [5.5](rules/section-5-procedural-writing/rule-5-05.md) Write notes only to give information, not instructions.

**Section 6 - Descriptive writing**

- [6.1](rules/section-6-descriptive-writing/rule-6-01.md) Give information gradually.
- [6.2](rules/section-6-descriptive-writing/rule-6-02.md) Use key words and key phrases to give your text a logical structure.
- [6.3](rules/section-6-descriptive-writing/rule-6-03.md) Write short sentences. Use a maximum of 25 words in each sentence.
- [6.4](rules/section-6-descriptive-writing/rule-6-04.md) Use paragraphs to show related information.
- [6.5](rules/section-6-descriptive-writing/rule-6-05.md) Make sure that each paragraph has only one topic.
- [6.6](rules/section-6-descriptive-writing/rule-6-06.md) Make sure that no paragraph has more than six sentences.

**Section 7 - Safety instructions**

- [7.1](rules/section-7-safety-instructions/rule-7-01.md) Use an applicable word (for example, “warning” or “caution”) to identify the level of risk.
- [7.2](rules/section-7-safety-instructions/rule-7-02.md) Start a safety instruction with a clear and accurate command or condition.
- [7.3](rules/section-7-safety-instructions/rule-7-03.md) Give an explanation to show the risk or possible result.

**Section 8 - Punctuation and word count**

- [8.1](rules/section-8-punctuation-and-word-count/rule-8-01.md) You can use all standard English punctuation marks but not the semicolon (;).
- [8.2](rules/section-8-punctuation-and-word-count/rule-8-02.md) Use hyphens (-) to connect words that are directly related.
- [8.3](rules/section-8-punctuation-and-word-count/rule-8-03.md) You can use parentheses: To make references to illustrations or text; To include letters or numbers that identify items on an illustration or in a text; To identify the work steps in a procedure; To include abbreviations; To give the singular and plural forms of a noun at the same time; To explain words or a part of a sentence; To include an alternative.
- [8.4](rules/section-8-punctuation-and-word-count/rule-8-04.md) In a vertical list, a colon (:) has the same effect on word count as a period and shows the end of a sentence.
- [8.5](rules/section-8-punctuation-and-word-count/rule-8-05.md) When you put text in parentheses, it counts as one word in that sentence.
- [8.6](rules/section-8-punctuation-and-word-count/rule-8-06.md) Count each of these elements as one word: Numbers; Numbers together with units of measurement; Abbreviations; Alphanumeric identifiers; Quoted text; Titles, headings, and text on placards and labels; Proper nouns of individuals, groups, organizations, and geopolitical entities.
- [8.7](rules/section-8-punctuation-and-word-count/rule-8-07.md) Hyphenated words count as one word.

**Section 9 - Writing practices**

- [9.1](rules/section-9-writing-practices/rule-9-01.md) Use a different sentence construction to write a sentence when a word-for-word replacement is not sufficient.
- [9.2](rules/section-9-writing-practices/rule-9-02.md) Use each approved word correctly.
- [9.3](rules/section-9-writing-practices/rule-9-03.md) When you use two words together, do not make phrasal verbs.
- [9.4](rules/section-9-writing-practices/rule-9-04.md) When you select terminology or wording, always use a consistent style.
- [GR-1](rules/section-9-writing-practices/general-recommendations/gr-1.md) The conjunction “that”
- [GR-2](rules/section-9-writing-practices/general-recommendations/gr-2.md) The preposition “with”
- [GR-3](rules/section-9-writing-practices/general-recommendations/gr-3.md) How to use pronouns
- [GR-4](rules/section-9-writing-practices/general-recommendations/gr-4.md) The pronoun “this”
- [GR-5](rules/section-9-writing-practices/general-recommendations/gr-5.md) False friends
- [GR-6](rules/section-9-writing-practices/general-recommendations/gr-6.md) Latin abbreviations
- [GR-7](rules/section-9-writing-practices/general-recommendations/gr-7.md) Inclusive language
- [GR-8](rules/section-9-writing-practices/general-recommendations/gr-8.md) Possessive form

**Section 10 – Code in text**

- [10.1](rules/section-10-code-in-text/rule-10-01.md) Use code format for identifiers, commands, file paths, and values that the reader types or sees on the screen.
- [10.2](rules/section-10-code-in-text/rule-10-02.md) Count each code span as one word. Do not count the text in a code block.
- [10.3](rules/section-10-code-in-text/rule-10-03.md) When the reader must execute a command, put the command in a code block after the instruction.
- [10.4](rules/section-10-code-in-text/rule-10-04.md) Do not use a command, a product name, or an identifier as a verb.
- [10.5](rules/section-10-code-in-text/rule-10-05.md) Write placeholders in one format in all of the text. Tell the reader which value to put in each placeholder.
<!-- index:end -->
