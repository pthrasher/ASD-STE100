---
title: "Software verbs"
kind: dictionary-overlay
---

# Software verbs

This file gives the profile status of verbs that occur frequently in software text. Each entry tells you if you can use the verb and in which meaning. If you cannot use the verb, the entry gives a different word.

Look here first. If a verb is not in this file, use the [Issue 9 dictionary](../../issue-9/part-2-dictionary/index.md). [README.md](README.md) gives the full lookup procedure and the meaning of each field.

## abort (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To stop a process or an operation before the process or the operation is completed
  - STE: If the migration shows an error, abort the migration.
  - Non-STE: If the migration errors out, bail.

## allow (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [allow (v)](../../issue-9/part-2-dictionary/words/a.md#allow-v), not approved
- Alternative: LET (v)
  - STE: This flag lets the script continue after an error.
  - Non-STE: This flag allows the script to continue after an error.

## approve (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [approve (v)](../../issue-9/part-2-dictionary/words/a.md#approve-v), not approved
- Alternative: APPROVAL (n)
  - STE: Two reviewers must give their approval before you merge the pull request.
  - Non-STE: The pull request needs to be approved by two reviewers before merging.
- Note: The label of a user-interface control is quoted text (Rule 8.6). You can write: Click “Approve.”

## boot (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To start a computer or a virtual machine and load its operating system
  - STE: Boot the virtual machine from the recovery image.
- Related: reboot (v)

## build (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [build (v)](../../issue-9/part-2-dictionary/words/b.md#build-v), not approved. Alternative: ASSEMBLE (v)
- Meaning: To make the executable files or packages of a project from its source code
  - STE: Build the project before you execute the integration tests.
  - Non-STE: Build and run the integration tests.
- Note: Use this verb only for software. For physical items, use ASSEMBLE (v).

## call (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [call (v)](../../issue-9/part-2-dictionary/words/c.md#call-v), not approved. Alternative: TELL (v)
- Meaning: To start the operation of a function, a method, or an endpoint from code
  - STE: The handler calls `validate()` before it writes to the database.
  - Non-STE: The handler invokes `validate()` prior to writing to the database.
- Note: Do not use this verb for people or for telephones.

## catch (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [CATCH (v)](../../issue-9/part-2-dictionary/words/c.md#catch-v), approved with a different meaning: “To stop or prevent the movement of something.” For other meanings, Issue 9 gives COLLECT (v).
- Meaning: To receive an exception in code and stop it before it goes to the caller
  - STE: The client catches `TimeoutError` and tries the request again.
  - Non-STE: Timeouts are handled by the client, which retries.
- Note: This is a software meaning. Rule 1.3 is also applicable to the Issue 9 meanings.

## check (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [check (v)](../../issue-9/part-2-dictionary/words/c.md#check-v), not approved
- Alternative: MAKE SURE (v)
  - STE: Make sure that the tests pass before you push the branch.
  - Non-STE: Check that the tests pass before pushing.
- Alternative: EXAMINE (v)
  - STE: Examine the log file for errors.
  - Non-STE: Check the logs for errors.
- Alternative: CHECK (n)
  - STE: The pipeline does a lint check on each commit.

## clear (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 b (user interface and application processes)
- Issue 9: [clear (v)](../../issue-9/part-2-dictionary/words/c.md#clear-v), not approved in general text. Alternative: CLEAN (v)
- Meaning: To remove all data from a cache, a field, a buffer, or a screen
  - STE: Clear the cache, then start the service again.
- Note: For physical items, use CLEAN (v).

## clone (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To make a local copy of a repository and its history
  - STE: Clone the repository, then install the dependencies.
- Note: Use this verb only for repositories. For other data, use COPY (n) or the technical verb “copy.”

## commit (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To record a set of changes in the history of a repository
  - STE: Commit your changes before you rebase your branch.
  - Non-STE: Check in your changes before kicking off the rebase.
- Related: commit (TN) in [nouns.md](nouns.md#commit-tn)

## compile (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [compile (v)](../../issue-9/part-2-dictionary/words/c.md#compile-v), not approved, in the meaning “to make a list”
- Meaning: To change source code into machine code or bytecode
  - STE: The compiler shows an error if a type is incorrect.
  - STE: Compile the module without optimization.
- Note: For the full sequence that makes a package, use build (v).

## configure (v)
- Profile status: not approved
- Decision: accepted
- Issue 9: not in the dictionary
- Alternative: SET (v)
  - STE: Set the timeout to 30 seconds.
  - Non-STE: Configure the timeout to be 30 seconds.
- Alternative: CHANGE (v) … CONFIGURATION (TN)
  - STE: Change the configuration of the load balancer.
  - Non-STE: Reconfigure the load balancer.

## copy (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 b (user interface and application processes)
- Issue 9: [copy (v)](../../issue-9/part-2-dictionary/words/c.md#copy-v), not approved in general text. Alternatives: WRITE (v), COPY (n), RECORD (v)
- Meaning: To make a second instance of data, a file, or text in a computer system
  - STE: Copy `.env.example` to `.env`.
- Note: For a repository, use clone (v).

## create (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [create (v)](../../issue-9/part-2-dictionary/words/c.md#create-v), not approved
- Alternative: MAKE (v)
  - STE: Make a branch for each change.
  - Non-STE: Create a branch for each change.

## debug (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To find and correct the cause of incorrect operation in software
  - STE: To debug the service, set the log level to `debug`.

## delete (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 b (user interface and application processes)
- Issue 9: [delete (v)](../../issue-9/part-2-dictionary/words/d.md#delete-v), not approved in general text. Alternatives: ERASE (v), REMOVE (v)
- Meaning: To remove data, a file, or a resource from a computer system
  - STE: Delete the branch after you merge the pull request.
  - STE: This command deletes all data in the table permanently.

## deploy (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [DEPLOY (v)](../../issue-9/part-2-dictionary/words/d.md#deploy-v), approved with a different meaning: “To move or cause to move from a specified position of storage and into operation”
- Meaning: To install a version of software in an environment and put it into operation
  - STE: Deploy the release to the test environment first.
  - Non-STE: Ship it to staging first.
- Note: This is a software meaning. Rule 1.3 is also applicable to the Issue 9 meanings.

## disable (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 b (user interface and application processes)
- Meaning: To stop the operation of a function or a setting until someone enables it again
  - STE: Disable the cache when you do the performance test.
- Related: enable (v)

## download (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To copy data from a remote computer system to a local one
  - STE: Download the installer from the release page.
- Related: upload (v)

## enable (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 b (user interface and application processes)
- Issue 9: [enable (v)](../../issue-9/part-2-dictionary/words/e.md#enable-v), not approved in general text. Alternative: LET (v)
- Meaning: To start the operation of a function or a setting
  - STE: Enable the feature flag only in the test environment.
  - Non-STE: This setting enables users to export data. (Use LET: This setting lets users export data.)
- Related: disable (v)

## enter (v)
- Profile status: technical verb
- Limit: only for data that the reader types
- Decision: standard
- Basis: Rule 1.12, category 2 a (input and output processes)
- Issue 9: [enter (v)](../../issue-9/part-2-dictionary/words/e.md#enter-v), not approved in general text. Alternatives: GO INTO, RECORD (v), ENTRY (n)
- Meaning: To type data into a computer system, for example a value or a password
  - STE: Enter your API token when the CLI shows the prompt.
- Note: Rule 1.12 uses this word as its own example (“Enter your password”).
- Note: Do not use this verb for a command, a script, a program, or a test. Use execute (v).
  - STE: Execute this command:
  - Non-STE: Enter the following command:

## execute (v)
- Profile status: technical verb
- Limit: only for software
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [execute (v)](../../issue-9/part-2-dictionary/words/e.md#execute-v), not approved. Alternative: DO (v)
- Meaning: To make a computer do the instructions of a program, a script, a command, or a test
  - STE: Execute the unit tests before you push the branch.
  - STE: Execute this command:
  - STE: The pipeline executes the migrations after each deployment.
- Note: Rule 1.12 lets you use a word that is not approved as a technical verb, if it is in a category. No approved verb gives this meaning accurately:
  - DO (v) has the meaning “To complete a procedure, task, or step.” The reader does the work. With execute (v), the computer does the instructions.
  - OPERATE (v) has the meaning “To put, keep, or be in action.” “Operate the unit tests” has no clear meaning.
  - START (v) tells only the start of an operation.
- Note: For a set of steps that a person or an agent does, use DO (v), as the Issue 9 entry for “execute” does: “Do these steps.” For a service that continues to operate, use START (v) and STOP (v). For a machine or a system that continues to operate, use OPERATE (v). For data that the reader types, use enter (v).
- Note: Tests have two forms. For test code, use execute (v): “Execute the unit tests.” For a test procedure that a person or an agent does, use DO (v) and TEST (n): “Do a test of the migration on a copy of the production data.”
- Related: [run (v)](#run-v), [enter (v)](#enter-v)

## fail (v)
- Profile status: technical verb
- Limit: only for tests and checks
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [fail (v)](../../issue-9/part-2-dictionary/words/f.md#fail-v), not approved. Alternatives: IF … NOT, FAILURE (TN), UNSATISFACTORY (adj)
- Meaning: To give a result that shows that a test or a check is not satisfactory
  - STE: If a unit test fails, do not merge the pull request.
  - STE: The lint check fails when a line has more than 100 characters.
- Note: For programs, services, and components, use the Issue 9 alternatives.
  - STE: If the service does not start, examine the log file.
  - Non-STE: If the service fails to start, check the logs.
- Related: pass (v)

## fetch (v)
- Profile status: technical verb
- Limit: only for version control
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To download commits and branches from a remote repository without a change to your local branches
  - STE: Fetch the remote branches before you rebase your branch.
- Note: For data from an API, use GET (v).
  - STE: The client gets the configuration from the server when it starts.
  - Non-STE: The client fetches the config on startup.

## fix (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [fix (v)](../../issue-9/part-2-dictionary/words/f.md#fix-v), not approved
- Alternative: CORRECT (v)
  - STE: This commit corrects the bug in the date parser.
  - Non-STE: Fix date parser bug.
- Alternative: REPAIR (v)
  - STE: Repair the corrupted index with this command:

## format (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To change the layout of code or data to agree with a specified style
  - STE: Format the code with the project formatter before you commit it.

## generate (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [generate (v)](../../issue-9/part-2-dictionary/words/g.md#generate-v), not approved
- Alternative: MAKE (v)
  - STE: This script makes the client code from the API schema.
  - Non-STE: This script generates the client from the schema.

## handle (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [handle (v)](../../issue-9/part-2-dictionary/words/h.md#handle-v), not approved
- Alternative: catch (v), for exceptions
  - STE: The worker catches connection errors and records them.
  - Non-STE: The worker handles connection errors gracefully.
- Alternative: process (v), a technical verb
  - STE: The queue processes one task at a time.
  - Non-STE: The queue handles one job at a time.

## install (v)
- Profile status: approved
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations), and the Issue 9 dictionary
- Issue 9: [INSTALL (v)](../../issue-9/part-2-dictionary/words/i.md#install-v), approved: “To attach an item in or to a second item”
- Meaning: To put software on a computer system so that it is ready for use
  - STE: Install the dependencies before you build the project.

## kill (v)
- Profile status: not approved
- Limit: for software processes
- Decision: accepted
- Issue 9: [KILL (v)](../../issue-9/part-2-dictionary/words/k.md#kill-v), approved only with the meaning “To cause death”
- Alternative: STOP (v)
  - STE: Stop the process.
  - Non-STE: Kill the process.
- Alternative: STOP (v) … IMMEDIATELY (adv)
  - STE: If the process does not stop after 30 seconds, stop it immediately with `kill -9`.
- Note: Rule 1.3 forbids other meanings of an approved word. A command name in code format is not a word of the text (Rule 10.4).

## load (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [load (v)](../../issue-9/part-2-dictionary/words/l.md#load-v), not approved in general text
- Meaning: To read data or code into memory for use
  - STE: The service loads the configuration file when it starts.

## log (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [log (v)](../../issue-9/part-2-dictionary/words/l.md#log-v), not approved. Alternative: RECORD (v)
- Alternative: RECORD (v)
  - STE: The service records each failed request in the log.
  - Non-STE: Failed requests get logged.
- Related: log (TN) in [nouns.md](nouns.md#log-tn)

## may (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [may (v)](../../issue-9/part-2-dictionary/words/m.md#may-v), not approved. Alternatives: CAN (v), POSSIBLY (adv)
- Alternative: CAN (v)
  - STE: This operation can continue for a maximum of 10 minutes.
  - Non-STE: This operation may take up to 10 minutes.
- Note: In agent instructions, “may” is frequently a permission. Write the permission clearly: “You can change files in `docs/`.”

## merge (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To combine the changes of one branch with a second branch
  - STE: Merge the pull request only after all pipeline checks pass.
- Related: merge conflict (TN) in [nouns.md](nouns.md#merge-conflict-tn)

## need (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [need (v)](../../issue-9/part-2-dictionary/words/n.md#need-v), not approved. Alternative: NECESSARY (adj)
- Alternative: NECESSARY (adj)
  - STE: Python 3.12 or a subsequent version is necessary.
  - Non-STE: You need Python 3.12+.
- Alternative: MUST (v)
  - STE: You must have write access to the repository.
  - Non-STE: You'll need write access to the repo.

## parse (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To read text or data and change it into a structure that a program can use
  - STE: The function parses the date string and returns a `datetime` object.

## pass (v)
- Profile status: technical verb
- Limit: only for tests and checks
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [pass (v)](../../issue-9/part-2-dictionary/words/p.md#pass-v), not approved
- Meaning: To give a result that shows that a test or a check is satisfactory
  - STE: All tests pass on the `main` branch.
- Note: Do not use this verb to mean “give” or “send.” For arguments, write: “Give the path as the first argument.”
  - Non-STE: Pass the path as the first argument.
- Related: fail (v)

## process (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [process (v)](../../issue-9/part-2-dictionary/words/p.md#process-v), not approved in general text. Alternative: DO (v) THE … PROCEDURE (n)
- Meaning: To do operations on data in a computer system
  - STE: The worker processes one task at a time.
- Note: For a procedure that a person does, use the Issue 9 alternative.

## pull (v)
- Profile status: technical verb
- Limit: only for version control
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [PULL (v)](../../issue-9/part-2-dictionary/words/p.md#pull-v), approved with a different meaning: “To use a force on something to move it toward the source of the force”
- Meaning: To fetch the changes from a remote repository and merge them into the local branch
  - STE: Pull the `main` branch before you make a new branch.
- Note: This is a software meaning. Rule 1.3 is also applicable to the Issue 9 meanings.
- Related: push (v)

## push (v)
- Profile status: technical verb
- Limit: only for version control
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [PUSH (v)](../../issue-9/part-2-dictionary/words/p.md#push-v), approved with meanings that are not software meanings: “1. To apply a force to something to move it away from the source of the force. 2. To move with a force against something”
- Meaning: To send local commits to a remote repository
  - STE: Push your branch, then open a pull request.
  - STE: Do not push to the `main` branch.
- Note: This is a software meaning. Rule 1.3 is also applicable to the Issue 9 meanings.
- Related: pull (v)

## query (v)
- Profile status: not approved
- Decision: accepted
- Issue 9: not in the dictionary
- Alternative: SEND (v) … QUERY (TN)
  - STE: The report sends one query to the database for each customer.
  - Non-STE: The report queries the database per customer.
- Alternative: GET (v)
  - STE: Get the row count from the `orders` table.
  - Non-STE: Query the orders table for the row count.
- Note: Rule 1.12 prefers an approved verb and a technical noun to a technical verb.

## raise (v)
- Profile status: technical verb
- Limit: only for exceptions
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [raise (v)](../../issue-9/part-2-dictionary/words/r.md#raise-v), not approved
- Meaning: To cause an exception in code
  - STE: The parser raises `ValueError` if the input is empty.
- Note: Use the verb of the programming language that the text is about: “raise” for Python and Ruby, “throw” for Java, JavaScript, and C++. Do not use the two verbs in the same text (Rule 1.11).
- Related: throw (v)

## rebase (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To move a set of commits so that they start from a different commit
  - STE: Rebase your branch on the `main` branch before you open the pull request.

## reboot (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To stop a computer and boot it again
  - STE: Reboot the host after you install the kernel update.
- Related: boot (v), restart (v)

## refactor (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To change the structure of code without a change to its behavior
  - STE: This commit refactors the retry code. The code operates the same as before.

## release (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [RELEASE (v)](../../issue-9/part-2-dictionary/words/r.md#release-v), approved with a different meaning: “To make free, to let go”
- Meaning: To make a version of software available to its users
  - STE: We release a new minor version each month.
- Note: This is a software meaning. Rule 1.3 is also applicable to the Issue 9 meaning, for example “release the lock.”

## render (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [render (v)](../../issue-9/part-2-dictionary/words/r.md#render-v), not approved. Alternative: MAKE (v)
- Alternative: SHOW (v)
  - STE: The browser shows the page after the scripts load.
  - Non-STE: The page renders after the scripts load.
- Alternative: MAKE (v)
  - STE: The function makes HTML from the template.
  - Non-STE: The function renders the template to HTML.

## require (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [require (v)](../../issue-9/part-2-dictionary/words/r.md#require-v), not approved. Alternative: NECESSARY (adj)
- Alternative: NECESSARY (adj)
  - STE: An API token is necessary for all write operations.
  - Non-STE: All write operations require an API token.
- Alternative: MUST (v)
  - STE: The `--output` flag must have a value.
  - Non-STE: The `--output` flag requires a value.

## restart (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [restart (v)](../../issue-9/part-2-dictionary/words/r.md#restart-v), not approved. Alternative: START (v)
- Alternative: START (v) … AGAIN (adv)
  - STE: Start the service again after you change the configuration.
  - Non-STE: Restart the service after changing the config.
- Note: For a computer or a virtual machine, you can use reboot (v).

## retry (v)
- Profile status: not approved
- Decision: standard
- Issue 9: not in the dictionary
- Alternative: TRY (v) … AGAIN (adv)
  - STE: The client tries the request again three times.
  - Non-STE: The client retries up to three times.

## return (v)
- Profile status: technical verb
- Limit: only for code
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Issue 9: [return (v)](../../issue-9/part-2-dictionary/words/r.md#return-v), not approved. Alternative: GO (v)
- Meaning: To give a value back to the caller when a function or a method stops
  - STE: The function returns `None` if the key is not in the cache.
- Note: For people and physical items, use the Issue 9 alternatives.

## revert (v)
- Profile status: technical verb
- Limit: only for version control
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To make a new commit that removes the changes of a previous commit
  - STE: Revert the commit that caused the regression.
- Related: roll back (v)

## roll back (v)
- Profile status: technical verb
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To put an environment or a database back into the condition of a previous version
  - STE: If the error rate increases after the deployment, roll back the deployment.
- Note: This is a technical verb, not a phrasal verb. Do not make other phrasal verbs from “roll” (Rule 9.3).

## run (v)
- Profile status: not approved
- Decision: accepted
- Issue 9: [run (v)](../../issue-9/part-2-dictionary/words/r.md#run-v), not approved. Alternative: OPERATE (v)
- Alternative: execute (v), for a program, a script, a command, or a test
  - STE: Execute the unit tests before you push the branch.
  - Non-STE: Run the unit tests before pushing.
  - STE: Execute this command:
  - Non-STE: Run the following:
- Alternative: START (v), for a service or a server that continues to operate
  - STE: Start the development server.
  - Non-STE: Spin up the dev server.
- Alternative: DO (v), for a set of steps
  - STE: Do the steps in the release procedure.
  - Non-STE: Run through the release checklist.
- Alternative: OPERATE (v), for a system that continues to operate
  - STE: The service operates in three regions.
  - Non-STE: The service runs in three regions.
- Note: Rule 1.12 tells you: “Do not use technical verbs that are general or not clear.” “Run” has many meanings in general English. Thus, the profile does not use “run” as a technical verb. “Execute” has only one meaning in software, and it is not slang or jargon (Rule 1.10). Refer to [execute (v)](#execute-v).

## save (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 b (user interface and application processes)
- Issue 9: [save (v)](../../issue-9/part-2-dictionary/words/s.md#save-v), not approved in general text. Alternative: KEEP (v)
- Meaning: To write data from memory to a file or to storage
  - STE: Save the file before you close the editor.

## should (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [should (v)](../../issue-9/part-2-dictionary/words/s.md#should-v), not approved. Alternatives: MUST (v), IF (conj)
- Alternative: MUST (v), for an instruction
  - STE: The commit subject must have a maximum of 50 characters.
  - Non-STE: The commit subject should be 50 characters or less.
- Alternative: an imperative, for an instruction to the reader
  - STE: Write tests for each new function.
  - Non-STE: You should write tests for each new function.
- Alternative: IF (conj), for a condition
  - STE: If the build fails, examine the log.
  - Non-STE: Should the build fail, check the log.
- Note: In agent instructions, “should” is not clear. The agent cannot know if the instruction is mandatory. Use MUST or the imperative for a mandatory instruction. Use CAN for a permission.

## store (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 b (user interface and application processes)
- Issue 9: [store (v)](../../issue-9/part-2-dictionary/words/s.md#store-v), not approved in general text
- Meaning: To keep data in memory, in a file, or in a database
  - STE: The service stores session tokens in memory only.

## test (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [test (v)](../../issue-9/part-2-dictionary/words/t.md#test-v), not approved. Alternative: TEST (n)
- Alternative: DO (v) … TEST (n)
  - STE: Do a test of the migration on a copy of the production data.
  - Non-STE: Test the migration against a prod snapshot.
- Related: unit test (TN) in [nouns.md](nouns.md#unit-test-tn)

## throw (v)
- Profile status: technical verb
- Limit: only for exceptions
- Decision: accepted
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To cause an exception in code
  - STE: The constructor throws `IllegalArgumentException` if the name is empty.
- Note: Use the verb of the programming language that the text is about. Refer to raise (v).
- Related: raise (v)

## trigger (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [trigger (v)](../../issue-9/part-2-dictionary/words/t.md#trigger-v), not approved. Alternatives: CAUSE (v), START (v)
- Alternative: START (v)
  - STE: When you push to the `main` branch, the deployment pipeline starts.
  - Non-STE: Pushing to main triggers the deploy pipeline.
- Alternative: CAUSE (v)
  - STE: An empty input causes this error.
  - Non-STE: This error is triggered by empty input.

## update (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To change software or data so that it agrees with a newer version
  - STE: Update the lock file after you add a dependency.
- Related: upgrade (v)

## upgrade (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To replace software with a newer version
  - STE: Upgrade the database to version 16 before you deploy this release.

## upload (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 c (system operations)
- Meaning: To copy data from a local computer system to a remote one
  - STE: Upload the build artifacts to the package registry.
- Related: download (v)

## validate (v)
- Profile status: technical verb
- Decision: standard
- Basis: Rule 1.12, category 2 b (user interface and application processes)
- Meaning: To make sure that data agrees with a specified format or with specified limits
  - STE: The API validates the request body before it writes to the database.
- Note: For a person who examines a result, use MAKE SURE (v). Refer to verify (v).

## verify (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [verify (v)](../../issue-9/part-2-dictionary/words/v.md#verify-v), not approved. Alternative: MAKE SURE (v)
- Alternative: MAKE SURE (v)
  - STE: Make sure that the service is available after the deployment.
  - Non-STE: Verify the service is up post-deploy.

## work (v)
- Profile status: not approved
- Decision: standard
- Issue 9: [work (v)](../../issue-9/part-2-dictionary/words/w.md#work-v), not approved. Alternative: WORK (n)
- Alternative: OPERATE (v)
  - STE: If the script does not operate correctly, examine its output.
  - Non-STE: If the script doesn't work, look at its output.
