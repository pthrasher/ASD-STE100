---
title: "API reference"
kind: text-type
ste-text-type: descriptive and procedural
---

# API reference

API reference documentation tells developers and agents how to call a function, a method, or an endpoint. It is in the docstrings of the code, and in the pages that tools make from the docstrings. Developers read it in their editor. Agents read it to select a function and to write a correct call. Tools parse its sections to make pages. Editors also show these sections. The reference is descriptive text (Section 6). Its examples and its procedures are procedural text (Section 5). [../SCOPE.md](../SCOPE.md) gives the types of text that are in the scope of this profile.

## Structure

A docstring or a reference page has these parts, in this sequence:

1. **The first line.** One sentence in the imperative, with a period at the end: “Return the user that has the given ID.” Many tools show only this line in a list of functions. Thus, it must identify the function without the other lines. This form agrees with Rule 3.2 and Rule 4.2. It is a decision of the profile, not an instruction to the reader (Rule 5.3).
2. **The description.** Descriptive text (Section 6). Tell how the function operates, and give its limits. Tell the effects that are not in the return value, for example a write to the database. Use the simple present tense. Use the function, the method, or the endpoint as the subject of the sentence (Rule 3.6).
3. **The parameters.** One item for each parameter (Rule 4.3). Give the name in code format (Rule 10.1), the value that the function accepts, and the default value. Use “parameter” for the name in the definition, and “argument” for the value in a call. Refer to [parameter (TN)](../dictionary/nouns.md#parameter-tn).
4. **The return value.** Give the value, and each condition that gives a different value.
5. **The exceptions.** Give each exception and the condition that causes it. Use the verb of the programming language: “raise” for Python and Ruby, “throw” for Java, JavaScript, and C++. Do not use the two verbs in the same text. Refer to [raise (v)](../dictionary/verbs.md#raise-v).
6. **The examples.** Put each example in a code block. Before the code block, write one sentence that tells the result of the example. If the example is a procedure, write the instructions in the imperative (Rule 5.3). Put each command after its instruction (Rule 10.3).

The keywords of the docstring format (for example `Args:`, `@param`, or `@throws`) are data for tools. The rules of STE are for the text after the keywords.

## Rules that matter most

- [Rule 3.2](../rules/section-3-verbs/rule-3-02.md): The first line uses the imperative. The description uses the simple present tense, not “will attempt to.”
- [Rule 3.6](../rules/section-3-verbs/rule-3-06.md): The function is the agent. Write “The function deletes the file,” not “The file is deleted.”
- [Rule 1.11](../rules/section-1-words/rule-1-11.md): Use the names of the code. If the code uses `user_id`, do not write “the account number” in the text.
- [Rule 1.12](../rules/section-1-words/rule-1-12.md): The profile gives “call,” “return,” “raise,” and “throw” as technical verbs. Refer to [verbs.md](../dictionary/verbs.md).
- [Rule 4.3](../rules/section-4-sentences/rule-4-03.md): Parameters, return values, and exceptions are vertical lists. An item that is not a full sentence has no period.
- [Rule 10.1](../rules/section-10-code-in-text/rule-10-01.md) and [Rule 10.4](../rules/section-10-code-in-text/rule-10-04.md): Put identifiers in code format. Do not use an identifier as a verb, for example “`await` the result.”
- [Rule 7.1](../rules/section-7-safety-instructions/rule-7-01.md): If a call can delete data permanently, give a safety instruction before the example.

## Examples

A Python docstring:

[Non-STE]

```python
def get_user(user_id, include_deleted=False):
    """Gets a user.

    This function will attempt to fetch the user from the cache first, and if it
    isn't there it queries the DB. Deleted users are excluded unless
    include_deleted is set.

    Args:
        user_id: the id
        include_deleted: whether to include deleted users

    Returns:
        User object or None

    Raises:
        ValueError: bad id
    """
```

[STE]

```python
def get_user(user_id, include_deleted=False):
    """Return the user that has the given ID.

    First, the function gets the user from the cache. If the cache does not
    contain the user, the function gets the user from the database.

    Args:
        user_id: The ID of the user. It must be more than 0.
        include_deleted: If this value is `True`, the function also
            returns a deleted user. The default value is `False`.

    Returns:
        The user. If no user has this ID, the function returns `None`.

    Raises:
        ValueError: `user_id` is less than 1.
    """
```

An endpoint:

[Non-STE]

```markdown
### DELETE /projects/{id}

Deletes the project. Note: this can't be undone, so be careful! Requires admin scope.
```

[STE]

```markdown
### DELETE /projects/{project_id}

Delete the project and all of its files.

An API token with the `admin` scope is necessary.

CAUTION: Before you send this request, make a backup of the project. The server deletes the project and its files permanently.

Responses:

- `204 No Content`: The server deleted the project.
- `404 Not Found`: No project has this ID.
```

JavaScript tags:

- [Non-STE] `@returns {boolean} true if successful`
- [STE] `@returns {boolean}` The function returns `true` if it saved the file. It returns `false` if it did not save the file.
- [Non-STE] `@throws {TypeError} Should throw if name is empty.`
- [STE] `@throws {TypeError}` The name is an empty string.

## Review questions

- Can an agent select the correct function from only the first line?
- Does the text give each condition that causes an exception, and the exception for each condition?
- Does the text tell the effects that are not in the return value, for example a write to the database or a network request?
- Do the names in the text agree with the names in the code after this change?
- Can a developer use the example without changes? Does the example show a result that the developer can compare with their result?
- If a call can delete data or change the production environment, is there a safety instruction?
