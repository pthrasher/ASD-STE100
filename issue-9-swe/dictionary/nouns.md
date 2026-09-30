---
title: "Software technical nouns"
kind: dictionary-overlay
---

# Software technical nouns

Rule 1.5 lets you use technical nouns that you can put in a category. Rule 1.11 tells you to use one technical noun for one item. This file gives the technical nouns of this profile. For each item, it gives one term and the terms that you must not use for that item.

Rule 1.7 is applicable to each noun in this file: do not use a technical noun as a verb, unless [verbs.md](verbs.md) gives the verb.

Most nouns in this file are in Rule 1.5, category 19 (computer science, information and communication technology). The Basis field shows the category only when it is different.

## administrator (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 11 (professional roles, individuals, groups)
- Meaning: A person who controls the configuration of a system and the access of its users
  - STE: Only an administrator can delete a repository.
- Do not use: admin, sysadmin

## agent (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A program that uses a large language model to do tasks with tools
  - STE: The agent must not push to the `main` branch.
- Do not use: bot, assistant (for an agent that uses tools)

## alert (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [alert (v)](../../issue-9/part-2-dictionary/words/a.md#alert-v), not approved. Alternative: TELL (v)
- Meaning: A message that a monitoring system sends to persons when a metric is more than a specified limit
  - STE: If the error rate is more than 5% for 10 minutes, the monitoring system sends an alert to the on-call engineer.
- Do not use: alarm; notification, page (for an alert)
- Note: “alert (v)” is not approved. Write “send an alert,” or use TELL (v).
- Related: [metric (TN)](#metric-tn), [on-call engineer (TN)](#on-call-engineer-tn)

## API key (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [key (v)](../../issue-9/part-2-dictionary/words/k.md#key-v), not approved. Alternatives: REFER (v), KEY (TN)
- Meaning: A string that identifies a program to an API and gives the program access to the API
  - STE: Keep the API key in an environment variable. Do not write it in the code.
- Do not use: key (alone), app key, API secret
- Note: Issue 9 uses KEY (TN) for a mechanical key. Do not write “key” alone for an API key. A token (TN) also gives access to an API. Use the term that the documentation of the API uses. Do not use “API key” and “API token” for the same string (Rule 1.11).
- Related: [token (TN)](#token-tn), [credential (TN)](#credential-tn)

## API (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: Application programming interface. The functions, endpoints, and data formats that a program gives to other programs
  - STE: The API returns an error if the token is expired.
- Note: Rule 8.6 counts an abbreviation as one word.

## argument (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A value that you give to a function, a method, or a command when you call it
  - STE: Give the file path as the first argument.
- Do not use: arg; parameter (for the value). Refer to parameter (TN).

## array (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A data structure that contains values in a sequence, with a number for the position of each value
  - STE: The `tags` field contains an array of strings.
- Do not use: vector
- Note: Use the term of the programming language that the text is about, for example “list” in Python or “slice” in Go. Do not use two terms for the same item in one text (Rule 1.11).

## artifact (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A file that a build makes and that you keep for a subsequent step, for example a package, a container image, or an executable file
  - STE: The pipeline keeps the build artifacts for 30 days.
- Do not use: artefact, build output
- Related: [build (TN)](#build-tn), [registry (TN)](#registry-tn)

## authentication (TN)
- Profile status: technical noun
- Decision: standard
- Basis: Rule 1.5, category 19. Issue 9 gives this word in its list of examples.
- Meaning: The procedure that makes sure that a user or a program is the one that it identifies itself as
  - STE: Authentication is necessary for all endpoints. It is not necessary for `/health`.
- Do not use: auth, authn

## backup (TN)
- Profile status: technical noun
- Decision: standard
- Basis: Rule 1.5, category 19. Issue 9 gives “backup” and “backup file” in its list of examples.
- Issue 9: [backup (n)](../../issue-9/part-2-dictionary/words/b.md#backup-n), not approved in the meaning “a thing that you use in an emergency.” Alternatives: EMERGENCY (n), AUXILIARY (adj)
- Meaning: A copy of data that you keep. If the data is deleted or damaged, you can use the copy to replace it
  - STE: Make a backup of the database before you execute the migration.
- Note: “back up (v)” is a phrasal verb and is not approved (Rule 9.3). Write “make a backup of.”

## boolean (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A data type that has only two values, `true` and `false`
  - STE: The `enabled` field is a boolean. Its default value is `false`.
- Do not use: bool (except in code format)
- Note: “true (adj)” and “false (adj)” are not approved in Issue 9. Write the two values in code format.

## branch (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A line of development in a repository, with its own sequence of commits
  - STE: Make a branch for each change.
- Note: “branch (v)” is not approved (Issue 9 alternative: DIVIDE (v)).

## bucket (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A storage location in an object storage service. It has a name and contains files, for example an Amazon S3 bucket.
  - STE: Upload the backup file to the `db-backups` bucket.
- Do not use: container (for a bucket)
- Note: In “object storage,” an object is a file and its metadata. It is not an object of a class. Refer to [object (TN)](#object-tn).

## bug (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: An error in code that causes incorrect behavior
  - STE: This commit corrects a bug in the date parser.
- Do not use: defect, glitch, issue (for the error). Refer to issue (TN).
- Note: Issue 9 uses DEFECT (TN) for physical items. This profile uses “bug” for software, because it is the term of the industry (Rule 1.8). Do not use the two terms for the same item.

## build (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: 1. The procedure that makes executable files or packages from source code. 2. The result of that procedure
  - STE: The build takes four minutes.
- Do not use: compilation (for the full procedure)
- Note: “build (n)” is not approved in Issue 9 for structures. Use this technical noun only for software.

## cache (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A temporary store of data that makes subsequent access faster
  - STE: The service keeps the results in a cache for 60 seconds.
- Note: “cache (v)” is not approved. Write “keep in a cache.”

## callback (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A function that you give to a second function as an argument. The second function calls it at a subsequent time.
  - STE: The client calls the callback after it receives the response.
- Related: [function (TN)](#function-tn), [argument (TN)](#argument-tn)

## certificate (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A file that identifies a server or a client and contains its public key, with the approval of a certificate authority
  - STE: If the certificate is expired, clients cannot connect to the server.
- Do not use: cert, SSL certificate (write “TLS certificate” if the type is important)
- Note: Rule 1.5 gives certificates in category 15 and category 21 as documents and legal papers. Use this technical noun only for the software item. “certify (v)” is not approved in Issue 9.

## changelog (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A file that shows the changes in each release of a project
  - STE: Add an entry to the changelog for each change that users can see.
- Do not use: change log, history file, release notes (for the file in the repository)
- Related: [release (TN)](#release-tn)

## class (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A part of code that gives the fields and the methods of a type of object
  - STE: The `HttpClient` class keeps one connection for each server.
- Note: Rule 1.5 gives “Class” in category 15 with a different meaning. Issue 9 also gives CLASS (TN) as an alternative to “classification (n).” Use this technical noun only for code.
- Related: [object (TN)](#object-tn), [method (TN)](#method-tn), [interface (TN)](#interface-tn)

## client (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A program that sends requests to a server and receives the responses
  - STE: The client sends the API token in the `Authorization` header.
- Do not use: consumer (for a program that sends requests to an API)
- Note: A client is a program, not a person. For a person, use [user (TN)](#user-tn).
- Related: [server (TN)](#server-tn), [request (TN)](#request-tn), [response (TN)](#response-tn)

## cluster (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A group of nodes that operate together as one system
  - STE: If one node stops, the other nodes in the cluster continue to operate.
- Related: [node (TN)](#node-tn)

## code block (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: Code format on different lines, between two lines of three backticks in Markdown
  - STE: Put the command in a code block after the instruction.
- Do not use: code fence, fenced block, snippet (for the block)
- Note: In this technical noun, “code” is software code. CODE (n) is approved in Issue 9 with a different meaning: “A sequence of symbols, letters, and/or numbers used for identification.”
- Related: [code span (TN)](#code-span-tn), [Rule 10.1](../rules/section-10-code-in-text/rule-10-01.md), [Rule 10.2](../rules/section-10-code-in-text/rule-10-02.md), [Rule 10.3](../rules/section-10-code-in-text/rule-10-03.md)

## code review (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The procedure where a person or an agent examines a change before it is merged
  - STE: All changes must have a code review.
- Do not use: review (alone), CR
- Note: “review (n)” and “review (v)” are not approved in Issue 9. Use “code review” as the technical noun. For the action, use EXAMINE (v).

## code span (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: Code format in a sentence: text between two backticks in Markdown
  - STE: Put each file name in a code span.
- Do not use: inline code
- Note: In this technical noun, “code” is software code. CODE (n) is approved in Issue 9 with a different meaning: “A sequence of symbols, letters, and/or numbers used for identification.”
- Related: [code block (TN)](#code-block-tn), [Rule 10.1](../rules/section-10-code-in-text/rule-10-01.md), [Rule 10.2](../rules/section-10-code-in-text/rule-10-02.md), [Rule 10.3](../rules/section-10-code-in-text/rule-10-03.md)

## column (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A part of a database table that has a name and a data type. Each row has one value for each column.
  - STE: The `created_at` column contains the date of each change.
- Do not use: field, attribute (for a column of a table)
- Related: [table (TN)](#table-tn), [row (TN)](#row-tn), [index (TN)](#index-tn)

## command (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: An instruction that you execute in a terminal or give to a command-line program
  - STE: Execute this command:
- Do not use: cmd, invocation

## commit hash (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The string of characters that identifies one commit, for example `3de91f1`
  - STE: In the issue, give the commit hash of the commit that caused the regression.
- Do not use: SHA, commit SHA, commit ID, revision (for a Git commit)
- Related: [commit (TN)](#commit-tn)

## commit (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A recorded set of changes in the history of a repository
  - STE: Each commit must contain only one change.
- Related: commit (v) in [verbs.md](verbs.md#commit-v)

## compiler (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A program that compiles source code into machine code or bytecode
  - STE: Compile the code with the `-Wall` flag. The compiler then shows all its messages.
- Related: compile (v) in [verbs.md](verbs.md#compile-v), [build (TN)](#build-tn)

## configuration (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 7. Issue 9 gives “configuration” in its list of examples.
- Meaning: The values that control how a program or a system operates
  - STE: The configuration is in `config/app.yaml`.
- Do not use: config, settings
- Note: “setting (n)” is not approved in Issue 9. For one value, write “configuration value.”

## container image (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A file that contains a program, its dependencies, and its configuration. A container starts from a container image.
  - STE: Build the container image and upload it to the container registry.
- Do not use: image (alone), Docker image (unless the text is about Docker)
- Note: CONTAINER (n) is approved in Issue 9 with the meaning “Something that holds fluids, materials, or objects.” Use “container image” only for software.
- Related: [container (TN)](#container-tn), [registry (TN)](#registry-tn)

## container (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A process that is isolated from other processes. It operates from an image that contains its software
  - STE: Start the database container before you execute the tests.
- Note: CONTAINER (n) is approved in Issue 9 with the meaning “Something that holds fluids, materials, or objects.” Use this technical noun only for software.
- Related: [container image (TN)](#container-image-tn)

## contributor (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 11 (professional roles, individuals, groups)
- Meaning: A person who gives changes to a project, for example in pull requests
  - STE: Each contributor must write tests for the changes in the pull request.
- Related: [maintainer (TN)](#maintainer-tn), [reviewer (TN)](#reviewer-tn)

## credential (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: Data that proves the identity of a user or a program, for example a password, a token, or a key
  - STE: Do not write credentials in the repository.
- Do not use: secret (for a credential); creds

## dashboard (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A page that shows metrics and other data about a system in graphs and tables
  - STE: Examine the error rate on the dashboard after each deployment.
- Related: [metric (TN)](#metric-tn)

## database (TN)
- Profile status: technical noun
- Decision: standard
- Basis: Rule 1.5, category 19. Issue 9 gives this word in its list of examples.
- Meaning: A structured set of data that a program can search and change
  - STE: Make a backup of the database before you execute the migration.
- Do not use: DB (unless the text defines it)

## debugger (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A program that stops a second program at specified lines of code and lets you examine its values
  - STE: Start the service in the debugger. Then set a breakpoint in the `login` function.
- Related: debug (v) in [verbs.md](verbs.md#debug-v)

## default value (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The value that a program uses when you do not give a different value
  - STE: The default value of `--retries` is 3.
- Do not use: default (alone)

## dependency (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A package or a service that a program must have to operate
  - STE: Install the dependencies before you build the project.
- Do not use: dep, requirement (for a package)

## deployment (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: 1. The procedure that deploys software. 2. A version of software that is in operation in an environment
  - STE: The deployment starts after all checks pass.
- Do not use: deploy (as a noun), rollout
- Note: Issue 9 gives “deployment” in category 20 (civil and military operations). This profile uses the software meaning.

## diff (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The differences between two versions of a file or of a set of files, shown line by line
  - STE: Examine the diff before you commit the changes.
- Do not use: delta
- Note: “diff (v)” is not a verb in this profile. Use COMPARE (v).

## directory (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A location in a file system that contains files or other directories
  - STE: Put the test files in the `tests/` directory.
- Do not use: folder, dir

## docstring (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A comment at the start of a function, a class, or a module that tools can read as documentation
  - STE: Write a docstring for each function of the API.
- Note: Use the term of the programming language that the text is about: “docstring” for Python, “doc comment” for Rust. Do not use the two terms in the same text (Rule 1.11).
- Related: [API reference](../text-types/api-reference.md), [code comments](../text-types/code-comments.md)

## e-mail (TN)
- Profile status: technical noun
- Decision: standard
- Basis: Rule 1.5, category 19. Issue 9 gives this word in its list of examples.
- Meaning: A message that a person or a program sends to an e-mail address through the internet
  - STE: The service sends an e-mail to the user when the password changes.
- Do not use: email, mail (for an e-mail message)
- Note: “e-mail (v)” is not a verb in this profile (Rule 1.7). Write “send an e-mail.”

## endpoint (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A URL and an HTTP method that an API uses to receive requests
  - STE: The `/users` endpoint returns a maximum of 100 users in each response.
- Do not use: route (in API documentation); URL (for the endpoint)

## environment (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A set of computer systems and configuration where software operates, for example “test environment” or “production environment”
  - STE: Deploy to the test environment before the production environment.
- Do not use: env, prod, staging, dev (unless the text defines the term)

## environment variable (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A variable that the operating system gives to a process. It has a name and a string value.
  - STE: If the `DEBUG` environment variable is set, the service writes more data to the log.
- Do not use: env var, environment setting
- Related: [variable (TN)](#variable-tn), [environment (TN)](#environment-tn)

## error message (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The text that a program shows or records when an error occurs
  - STE: The error message must tell the user the next step.
- Note: ERROR (n) is approved in Issue 9.

## event (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [event (n)](../../issue-9/part-2-dictionary/words/e.md#event-n), not approved. Alternative: IF (conj)
- Meaning: A message that a system sends or records when something occurs, for example a `user.created` event or a webhook event
  - STE: The service sends a `user.created` event after it adds the user to the database.
- Note: Use this technical noun only for a message between programs. For a condition in text, use IF, as Issue 9 does.
  - STE: If the connection stops, the client tries the request again.
  - Non-STE: In the event of a lost connection, the client retries.
- Related: [webhook (TN)](#webhook-tn), [handler (TN)](#handler-tn)

## exception (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: An object that code raises or throws to show that an error occurred
  - STE: If the file is missing, the function raises an exception.
- Note: “exception (n)” is not approved in Issue 9 in the meaning “a thing that does not agree with the rule.” Use this technical noun only for code.

## feature flag (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A configuration value that enables or disables a function at runtime
  - STE: Enable the feature flag only in the test environment.
- Do not use: toggle, switch, feature gate

## field (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 19. Issue 9 gives this word in its list of examples.
- Meaning: 1. An area on a screen where the user enters data. 2. A value with a name in an object, a data structure, or a message
  - STE: Enter your user name in the “User name” field.
  - STE: The response contains a `status` field for each task.
- Do not use: attribute, property, member (for a value in an object, unless the text is about a language that uses that term)
- Note: Issue 9 gives “field” in category 19, but it does not give its meaning. Other examples in that list, for example “menu,” “toolbar,” and “dialog check box,” are items of a user interface. Meaning 1 agrees with them. Meaning 2 is a decision of this profile. For a database table, use [column (TN)](#column-tn).

## file (TN)
- Profile status: technical noun
- Decision: standard
- Basis: Rule 1.5, category 19. Issue 9 gives this word in its list of examples.
- Meaning: A named set of data in a file system
  - STE: Save the file before you close the editor.
- Note: “file (v)” is not approved in Issue 9.

## fixture (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: Data or a condition that the test code prepares before a test starts. With a fixture, each test starts from the same condition
  - STE: The `users` fixture adds three test users to the database before each test.
- Note: Use this technical noun only for software tests. For a tool that holds a part, “fixture” is a different technical noun, in Rule 1.5, category 3 (tools and support equipment).
- Related: [unit test (TN)](#unit-test-tn)

## flag (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A named value that you give to a command-line program, for example `--verbose`
  - STE: The `--dry-run` flag shows the changes but does not make them.
- Do not use: option, switch
- Note: “option (n)” is not approved in Issue 9.

## fork (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A copy of a repository in a different account. Changes to the copy do not change the source repository.
  - STE: Make a fork of the repository. Then push your branch to the fork.
- Note: “fork (v)” is not a verb in this profile. Write “make a fork of.” Do not use this technical noun for a copy of an operating-system process.
- Related: [remote repository (TN)](#remote-repository-tn), [repository (TN)](#repository-tn)

## formatter (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A program that changes the layout of code to agree with a specified style
  - STE: Execute the formatter before you commit your changes.
- Do not use: prettifier, beautifier
- Related: format (v) in [verbs.md](verbs.md#format-v), [linter (TN)](#linter-tn)

## framework (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A library that gives the structure of a program and calls the code that you write
  - STE: The web framework calls this function for each request to `/login`.
- Note: Your code calls a library. A framework calls your code. Refer to [library (TN)](#library-tn).

## function (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A named block of code that you can call
  - STE: The function returns `None` if the key is not in the cache.
- Note: FUNCTION (n) is approved in Issue 9 with the meaning “Action or activity that a person or thing does.” Make sure that the reader cannot mix the two meanings. “function (v)” is not approved.

## handler (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A function that a program calls when it receives a specified request or event
  - STE: The handler of the `/users` endpoint writes the new user to the database.
- Note: “handle (v)” is not approved. Refer to [verbs.md](verbs.md#handle-v).
- Related: [middleware (TN)](#middleware-tn), [event (TN)](#event-tn)

## header (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A name and a value in the first part of a request or a response. A header gives data about the message.
  - STE: Put the API token in the `Authorization` header.
- Related: [request (TN)](#request-tn), [response (TN)](#response-tn), [request body (TN)](#request-body-tn)

## host (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A computer or a virtual machine on a network, where programs and services operate
  - STE: Stop the service on one host at a time.
- Do not use: box, machine, node (unless the text is about a node of a cluster)
- Note: Use [server (TN)](#server-tn) only for a program or a computer that receives requests from clients. For a computer in general, use “host.”

## index (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A data structure that a database uses to find rows in a table quickly
  - STE: Add an index to the `email` column. Without an index, this query examines all rows.
- Do not use: key (for an index)
- Note: The plural is “indexes.” Use this technical noun only for databases.
- Related: [table (TN)](#table-tn), [column (TN)](#column-tn)

## integer (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A data type for numbers that are not fractions, for example `-3`, `0`, and `42`
  - STE: The `timeout` value must be an integer between 1 and 300.
- Do not use: int (except in code format)
- Note: “integer” is also a mathematical term (Rule 1.5, category 7). The meaning is the same.

## integration test (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A test of two or more components that operate together, for example a service and its database
  - STE: Start the database container before you execute the integration tests.
- Note: TEST (n) is approved in Issue 9. “test (v)” is not approved.
- Related: [unit test (TN)](#unit-test-tn), [test suite (TN)](#test-suite-tn)

## interface (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 19. Issue 9 gives this word in its list of examples.
- Issue 9: [INTERFACE (n)](../../issue-9/part-2-dictionary/words/i.md#interface-n), approved: “The connection between two systems or components”
- Meaning: A part of code that gives the methods that a class must have
  - STE: The `Storage` interface has two methods, `read()` and `write()`. Each storage class must have these methods.
- Note: For the connection between two systems or components, for example a user interface, use INTERFACE (n) with its Issue 9 meaning. Use this technical noun only for code. Make sure that the reader cannot mix the two meanings. Use the term of the language that the text is about, for example “protocol” in Swift or “trait” in Rust.
- Related: [class (TN)](#class-tn)

## issue (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: An item in an issue tracker that records a bug, a task, or a request for a change
  - STE: Refer to issue #123 for the data that shows the problem.
- Do not use: ticket, card, bug (for the tracker item)
- Note: Issue 9 gives “issue” as a technical noun in category 7 and category 15, with other meanings. This profile uses category 19 for the item in an issue tracker.

## job (TN)
- Profile status: technical noun
- Limit: only for a CI job or a scheduled job (for example a cron job)
- Decision: accepted
- Issue 9: [job (n)](../../issue-9/part-2-dictionary/words/j.md#job-n), not approved. Alternatives: WORK (n), TASK (n)
- Meaning: 1. A set of steps that a pipeline executes as one unit. 2. A program or a script that a scheduler executes at specified times
  - STE: The `test` job executes the unit tests on each commit.
  - STE: The backup job starts at 02:00 each day.
- Do not use: cron (for a scheduled job)
- Note: For other work, use TASK (n). For an item in a queue, use TASK (n). Refer to [queue (TN)](#queue-tn).
- Related: [pipeline (TN)](#pipeline-tn)

## library (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: Code that other programs can use to do specified operations
  - STE: This library parses JSON and YAML files.
- Do not use: lib
- Note: A library is code. A package is the unit that you install. Refer to [package (TN)](#package-tn). For a library that calls your code, use [framework (TN)](#framework-tn).

## linter (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A program that examines code for errors and style problems. The linter does not execute the code.
  - STE: The linter shows an error if a variable is not used.
- Do not use: lint (for the program), lint tool
- Note: “lint (v)” is not a verb in this profile. Write “execute the linter” or “examine the code with the linter.”
- Related: [formatter (TN)](#formatter-tn)

## load balancer (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A server or a device that sends each request to one server of a group. It gives each server approximately the same load.
  - STE: The load balancer sends no requests to a server that does not pass the health check.
- Do not use: LB, balancer
- Related: [proxy (TN)](#proxy-tn)

## lock file (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A file that records the version of each dependency that a project installs, for example `package-lock.json` or `uv.lock`
  - STE: Commit the lock file with each change to the dependencies.
- Do not use: lockfile
- Note: A lock file is not a lock. Do not use this term for a file that a program uses as a lock. Refer to [lock (TN)](#lock-tn).
- Related: [dependency (TN)](#dependency-tn)

## lock (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [LOCK (v)](../../issue-9/part-2-dictionary/words/l.md#lock-v), approved: “To attach something, or hold it in position with a locking device”
- Meaning: A control in code or in a database that lets only one thread or process at a time use specified data
  - STE: The worker gets a lock on the row before it changes the row. Then it releases the lock.
- Do not use: mutex, latch (unless the difference is important)
- Note: Do not use LOCK (v) for a software lock. Write “get a lock on.” RELEASE (v) has its Issue 9 meaning in “release the lock.” For a file that records the versions of dependencies, refer to [lock file (TN)](#lock-file-tn).
- Related: [thread (TN)](#thread-tn), [race condition (TN)](#race-condition-tn), [transaction (TN)](#transaction-tn)

## log level (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [LEVEL (n)](../../issue-9/part-2-dictionary/words/l.md#level-n), approved: “A horizontal line, plane, surface, or condition”
- Meaning: A value that shows how important a log message is, for example `debug`, `info`, `warning`, or `error`
  - STE: Set the log level to `debug` only in the test environment.
- Do not use: severity, log severity (unless the log system uses that term)
- Note: Use “log level” as one technical noun. Do not use LEVEL (n) alone in this meaning.
- Related: [log (TN)](#log-tn), [log message (TN)](#log-message-tn)

## log message (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: One record that a program writes to a log about one operation, one change of condition, or one error
  - STE: Each log message contains the time, the log level, and the ID of the request.
- Do not use: message (alone, for a log message), log entry, log record
- Note: An error message can also be a log message. Use “error message” when the text is about the error. Use “log message” when the text is about the log.
- Related: [log (TN)](#log-tn), [error message (TN)](#error-message-tn), [log messages](../text-types/log-messages.md)

## log (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The records that a program writes about its operation
  - STE: Examine the log for errors that occurred before the service stopped.
- Do not use: logs (for one log file), trace (for a log)
- Note: “log (v)” is not approved. Refer to [verbs.md](verbs.md#log-v).
- Related: log file, log message

## maintainer (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 11 (professional roles, individuals, groups)
- Meaning: A person who can merge pull requests in a project and who makes its releases
  - STE: A maintainer must examine all changes to the API.
- Note: “maintain (v)” is not approved in Issue 9 (alternatives: KEEP (v), HOLD (v), MAINTENANCE (n)). Use “maintainer” only as this technical noun.
- Related: [contributor (TN)](#contributor-tn), [reviewer (TN)](#reviewer-tn)

## merge conflict (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A condition where version control cannot merge two changes to the same lines
  - STE: If a merge conflict occurs, correct the conflict. Then execute `git rebase --continue`.

## method (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A function that is part of a class or an object
  - STE: The `close()` method releases the connection.
- Note: In this example, “releases” has its Issue 9 meaning: to let go.

## metric (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A value that a system measures and records at intervals, for example the number of requests in each second
  - STE: The service sends its metrics to the monitoring system at intervals of 15 seconds.
- Do not use: stat, measurement (for a metric)
- Related: [dashboard (TN)](#dashboard-tn), [alert (TN)](#alert-tn)

## middleware (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: Code that a server executes for each request, before or after the handler of the request
  - STE: The authentication middleware rejects requests that do not have a token.
- Note: Some frameworks use a different term for the same item, for example “filter” or “interceptor.” Use the term of the framework, and use only that term in the text (Rule 1.11).
- Related: [handler (TN)](#handler-tn), [request (TN)](#request-tn)

## migration (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A script that changes the schema or the data of a database from one version to the next version
  - STE: Do not change a migration after it is on the `main` branch. Add a new migration.
- Do not use: migration script, schema change (for the migration)
- Note: Use this technical noun only for a database. For a move of data or of a service to a different system, use MOVE (v). “migrate (v)” is not a verb in this profile. Write “execute the migrations.”
- Related: [schema (TN)](#schema-tn), [database (TN)](#database-tn)

## mock (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: An object in a test that replaces a dependency and records how the code uses it
  - STE: Replace the HTTP client with a mock in the unit tests.
- Do not use: fake, stub, test double (unless the difference is important)
- Note: “mock (v)” is not a verb in this profile. Write “replace … with a mock.”

## module (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A file or a directory of code that has a name and that other code can use
  - STE: Put the database functions in the `db` module.
- Note: A module is part of the code. A package is the unit that you install. Refer to [package (TN)](#package-tn).

## node (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A computer or a virtual machine that is part of a cluster
  - STE: If a node stops, the cluster moves the containers of that node to the other nodes.
- Note: In a text about a cluster, do not use [host (TN)](#host-tn) for a node (Rule 1.11). For a node of a tree or a graph in code, write the full term, for example “tree node.”
- Related: [cluster (TN)](#cluster-tn)

## null value (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A value that shows that a variable or a field contains no data
  - STE: If the user did not give a phone number, the `phone` field contains a null value.
- Do not use: null, nil, none (as words of the text)
- Note: VALUE (n) is approved in Issue 9. Write the value of the language in code format, for example `null`, `None`, or `nil`.

## object (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [OBJECT (n)](../../issue-9/part-2-dictionary/words/o.md#object-n), approved: “Something that you can see or touch”
- Meaning: An item in memory that a program makes from a class. It has values for the fields of the class.
  - STE: The `connect()` function returns a `Connection` object.
- Do not use: instance (for an object of a class)
- Note: Use this technical noun only for code. Make sure that the reader cannot mix it with OBJECT (n), which has its Issue 9 meaning. In “object storage,” an object is a file and its metadata. Refer to [bucket (TN)](#bucket-tn).
- Related: [class (TN)](#class-tn)

## on-call engineer (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 11 (professional roles, individuals, groups)
- Meaning: The person who must be available to correct problems in a service during a specified period
  - STE: If the error rate increases after the deployment, tell the on-call engineer.
- Do not use: on-call (as a noun), on-caller, responder
- Related: [alert (TN)](#alert-tn)

## package (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A unit of software that you can install with a package manager
  - STE: Install the package with `pip install`.
- Do not use: library (for the installable unit), module (for the installable unit)

## parameter (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A named variable in the definition of a function, a method, or an endpoint
  - STE: The `limit` parameter is not necessary. Its default value is 50.
- Do not use: param; argument (for the name in the definition). Refer to argument (TN).

## password (TN)
- Profile status: technical noun
- Decision: standard
- Basis: Rule 1.12 gives this word in its example “Enter your password.”
- Meaning: A string of characters that a user enters for authentication
  - STE: Do not record passwords in the log.

## path (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The location of a file or a directory in a file system
  - STE: Give the path of the configuration file as the first argument.

## pipeline (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The automatic sequence of builds, tests, and deployments that starts after a change
  - STE: The pipeline executes the unit tests on each commit.
- Do not use: CI (unless the text defines it), workflow (for the full pipeline)

## placeholder (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A part of a command, a path, or a code example that the reader must replace with a value, for example `<branch-name>`
  - STE: Replace each placeholder with its value. Do not include the angle brackets.
- Do not use: variable, token (for a placeholder)
- Note: A shell variable, for example `$USER`, is not a placeholder. Refer to [variable (TN)](#variable-tn).
- Related: [Rule 10.5](../rules/section-10-code-in-text/rule-10-05.md)

## port (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [port (adj)](../../issue-9/part-2-dictionary/words/p.md#port-adj), not approved. Alternative: LEFT (adj)
- Meaning: A number that identifies one network connection point on a host, for example `443` for HTTPS
  - STE: The service receives requests on port `8080`.
- Note: Rule 1.5 gives “port” in category 5 (facilities) for a location for ships. Use this technical noun only for networks.

## process (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 7. Issue 9 gives “process” in its list of examples.
- Meaning: A program that is in operation, with its own memory and identifier
  - STE: Stop the process.
- Note: “process (n)” is not approved in the Issue 9 dictionary (alternative: PROCEDURE), but Rule 1.5 gives it as a technical noun in category 7. Use this technical noun only for an operating-system process. For a sequence of steps, use PROCEDURE (n).

## product name (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 11 (organizations and companies). This is the best category for this noun. A product name is a proper noun, as the name of a company is.
- Issue 9: [product (n)](../../issue-9/part-2-dictionary/words/p.md#product-n), not approved. Issue 9 tells you to use the name of the product, if it is possible.
- Meaning: The name of a software product or service, for example GitHub or Slack
  - STE: Send a message to the on-call team in Slack.
- Do not use: short names, for example “GH” or “k8s” (unless the text defines them)
- Note: Write the name as its company writes it, for example “GitHub.” Do not use a product name as a verb. Do not put it in code format, unless it is also a command.
- Related: [Rule 10.4](../rules/section-10-code-in-text/rule-10-04.md)

## program (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A set of instructions that a computer can do, for example an application, a script, or a service
  - STE: The program records all errors in the log.
- Do not use: app, binary (for the program in general)
- Note: “program (n)” is not approved in Issue 9 in the meaning “sequence.” Use this technical noun only for software.

## project (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The files, the configuration, and the dependencies of one program or one package, usually in one repository
  - STE: Build the project before you execute the integration tests.
- Note: A repository can contain more than one project.
- Related: [repository (TN)](#repository-tn)

## proxy (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A server that receives requests from clients and sends them to other servers
  - STE: The proxy adds the `X-Request-ID` header to each request.
- Do not use: proxy server
- Related: [load balancer (TN)](#load-balancer-tn)

## pull request (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A request to merge the commits of a branch into a different branch, with its code review
  - STE: Open a pull request after you push the branch.
- Do not use: PR (unless the text defines it), merge request, MR

## query (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: An instruction to a database to find or change data
  - STE: This query gets all orders from the last 30 days.

## queue (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A list of tasks or messages that a program keeps in sequence until a worker gets them
  - STE: If the queue contains more than 1000 tasks, add more workers.
- Note: For an item in a queue, use TASK (n). Do not use “job” for it. Refer to [job (TN)](#job-tn). “queue (v)” is not a verb in this profile. Write “add to the queue.”
- Related: [worker (TN)](#worker-tn)

## race condition (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A bug that occurs when two threads or processes use the same data at the same time. The result changes with the sequence of their operations.
  - STE: The two workers can change the same row at the same time. This race condition can cause incorrect data.
- Do not use: race (alone), data race (unless the difference is important)
- Note: CONDITION (n) is approved in Issue 9. Use “race condition” as one technical noun.
- Related: [lock (TN)](#lock-tn), [thread (TN)](#thread-tn)

## rate limit (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The maximum number of requests that a client can send in a specified period
  - STE: The rate limit of the API is 100 requests in one minute for each API key.
- Do not use: throttle, quota (unless the difference is important)
- Note: RATE (n) and LIMIT (n) are approved in Issue 9 with meanings that agree with this term. The entry is here to give one term for the item (Rule 1.11). “rate-limit (v)” and “throttle (v)” are not verbs in this profile.

## reference (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 15. Issue 9 gives “reference” in its list of examples.
- Issue 9: [reference (n)](../../issue-9/part-2-dictionary/words/r.md#reference-n), not approved. Alternative: REFER (v)
- Meaning: A document that gives all of the information about an API, a command, or a format, for example an “API reference”
  - STE: The API reference gives the parameters of each endpoint.
- Do not use: API docs, reference docs (for this document)
- Note: The list of category 15 gives “reference” without a meaning. In technical documentation, the word usually identifies text that refers to a different document or to a different part of the same document. The software meaning is a type of document, not text that refers to a document. Thus, the decision is not `standard`. For the action, use REFER (v), as Issue 9 does: “Refer to Chapter 20.”
- Related: [API reference](../text-types/api-reference.md)

## registry (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A service that stores packages or container images and lets users download them
  - STE: The pipeline uploads each release to the package registry.
- Do not use: package index, feed, repository (for a registry)
- Note: A registry is not a repository. Refer to [repository (TN)](#repository-tn).
- Related: [container image (TN)](#container-image-tn), [package (TN)](#package-tn)

## regression (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A bug that causes a function to stop operating correctly after it operated correctly in a previous version
  - STE: Revert the commit that caused the regression.

## release (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A version of software that is available to its users
  - STE: This release removes the `v1` endpoints.
- Related: release (v) in [verbs.md](verbs.md#release-v)

## remote repository (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A repository on a server. You fetch commits from it and push commits to it.
  - STE: Push your branch to the remote repository. Then open a pull request.
- Do not use: remote (as a noun), upstream (for the remote repository)
- Note: Write the name of a remote repository in code format, for example `origin`.
- Related: [repository (TN)](#repository-tn), [fork (TN)](#fork-tn), fetch (v) in [verbs.md](verbs.md#fetch-v), push (v) in [verbs.md](verbs.md#push-v)

## replica (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A copy of a database that receives all changes from the primary database
  - STE: Send the queries that only read data to the replica.
- Do not use: slave, secondary, mirror (for a replica)
- Note: For the database that receives all write operations, write “primary database.” PRIMARY (adj) is approved in Issue 9. Do not use “master” or “main” for it. “main (adj)” is not approved in Issue 9 (alternative: PRIMARY).
- Related: primary database, [database (TN)](#database-tn)

## repository (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A storage location for the files of a project and the history of their changes
  - STE: Clone the repository.
- Do not use: repo, codebase (for the repository)

## request body (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The data that a request contains after its headers, for example JSON data
  - STE: The request body must contain the `name` field.
- Do not use: payload, request payload, body (alone)
- Related: [request (TN)](#request-tn), [header (TN)](#header-tn), [response body (TN)](#response-body-tn)

## request (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A message that a client sends to a server, for example an HTTP request
  - STE: The server rejects requests that do not have a token.
- Note: “request (n)” and “request (v)” are not approved in Issue 9 in their general meaning. Use this technical noun only for messages between programs.
- Related: response (TN)

## response body (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The data that a response contains after its headers
  - STE: If an error occurs, the response body contains an error message.
- Do not use: payload, response payload, body (alone)
- Related: [response (TN)](#response-tn), [request body (TN)](#request-body-tn)

## response (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The message that a server sends back to a client after a request
  - STE: The response contains the ID of the new user.

## reviewer (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 11 (professional roles, individuals, groups)
- Meaning: A person or an agent who examines a change in a code review
  - STE: Each reviewer examines the tests and the documentation of the change.
- Note: “review (n)” is not approved in Issue 9 (alternatives: INSPECTION (n), EXAMINE (v)). Use “reviewer” only as this technical noun. For the procedure, use [code review (TN)](#code-review-tn).
- Related: [maintainer (TN)](#maintainer-tn)

## row (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [ROW (n)](../../issue-9/part-2-dictionary/words/r.md#row-n), approved: “A number of objects in a line”
- Meaning: A set of values in a database table, with one value for each column
  - STE: The query returns one row for each user.
- Do not use: record, tuple (for a row of a database table)
- Note: ROW (n) is approved in Issue 9 for objects in a line. Use this technical noun for data in a table.
- Related: [table (TN)](#table-tn), [column (TN)](#column-tn)

## schema (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The structure that data must agree with, for example the tables and columns of a database, or the fields and types of a JSON document
  - STE: The migration adds a `created_at` column to the schema of the `users` table.
- Related: [migration (TN)](#migration-tn)

## script (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A short program in a text file that a shell or an interpreter executes, for example a shell script
  - STE: Execute `scripts/seed.sh` to add test data to the database.
- Related: [program (TN)](#program-tn), execute (v) in [verbs.md](verbs.md#execute-v)

## server (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A program or a computer that receives requests from clients and sends responses
  - STE: The server records each request in the access log.

## service (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A program that operates continuously and gives a function to other programs through an API
  - STE: Start the service again after you change the configuration.
- Do not use: microservice, daemon (unless the difference is important)

## session (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A period of time when a server keeps data about one user or one client between requests, usually after authentication
  - STE: The session stops after 30 minutes without a request.
- Related: [authentication (TN)](#authentication-tn), [token (TN)](#token-tn)

## stack trace (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The list of function calls that were active when an exception occurred
  - STE: Put the full stack trace in the issue.
- Do not use: traceback, backtrace (unless the text is about a language that uses that term)

## status code (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The number in an HTTP response that shows the result of the request, for example `200` or `404`
  - STE: If the token is expired, the API returns the status code `401`.
- Do not use: status (alone), HTTP code, response code
- Note: CODE (n) is approved in Issue 9: “A sequence of symbols, letters, and/or numbers used for identification.” A status code agrees with this meaning.
- Related: [response (TN)](#response-tn)

## string (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A sequence of characters that a program uses as a value, for example `"hello"`
  - STE: The function returns the date as a string in the format `YYYY-MM-DD`.
- Do not use: str (except in code format)

## table (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A set of data in a database, in rows and columns
  - STE: The `users` table has one row for each user.
- Note: Rule 1.5 gives “table” in category 15 (parts of documentation) for a table in a document. Use this technical noun for a database table. In a text that can have the two meanings, write “database table.”
- Related: [row (TN)](#row-tn), [column (TN)](#column-tn), [index (TN)](#index-tn)

## tag (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [TAG (v)](../../issue-9/part-2-dictionary/words/t.md#tag-v), approved: “To put a tag on”
- Meaning: A name that refers to one specified commit in a repository, usually a release, for example `v2.1.0`
  - STE: Push the tag `v2.1.0` to the remote repository after you merge the release branch.
- Note: Rule 1.5 gives “tag” in category 3 for a tag on equipment. For a Git tag, write “make a tag.” Do not use TAG (v) for software, because the reader can mix the two meanings.
- Related: [release (TN)](#release-tn), [commit (TN)](#commit-tn)

## tenant (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A customer or an organization that uses a service together with other customers. The service keeps the data of each tenant isolated.
  - STE: Each query must include the tenant ID. Users must not see the data of a different tenant.
- Do not use: org, workspace (for a tenant, unless the product uses that term)

## test case (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [case (n)](../../issue-9/part-2-dictionary/words/c.md#case-n), not approved. Alternative: CONDITION (n)
- Meaning: One test, with its input data and the result that the test must get
  - STE: Add a test case for an empty input.
- Do not use: case (alone), test scenario
- Note: Use “case” only in this technical noun.
- Related: [test suite (TN)](#test-suite-tn)

## test coverage (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The percentage of the code that the tests execute
  - STE: The test coverage of new code must be a minimum of 80%.
- Do not use: code coverage, coverage (alone)
- Note: “cover (v)” is not approved in Issue 9 (alternatives: INCLUDE (v), HAVE (v), COVER (TN)). Do not write “the tests cover this function.” Write “the tests execute this function.”

## test suite (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A set of tests that you execute together
  - STE: Execute the full test suite before you make a release.
- Do not use: suite (alone), test set
- Related: [test case (TN)](#test-case-tn), [unit test (TN)](#unit-test-tn), [integration test (TN)](#integration-test-tn)

## thread (TN)
- Profile status: technical noun
- Decision: accepted
- Issue 9: [thread (v)](../../issue-9/part-2-dictionary/words/t.md#thread-v), not approved. Alternatives: PUT (v), TURN (v)
- Meaning: A sequence of instructions in a process that can operate at the same time as other sequences in the same process
  - STE: The server uses one thread for each connection.
- Note: Rule 1.5 gives “thread” in category 7. Issue 9 uses THREAD (TN) for the thread on a rod or a fitting (the alternative for “threaded (adj)”). Use this technical noun only for software.
- Related: [process (TN)](#process-tn), [lock (TN)](#lock-tn)

## timeout (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: 1. The maximum time that an operation can continue. 2. The condition when an operation stops because it operated for the maximum time
  - STE: The default value of the timeout is 30 seconds.
  - STE: If a timeout occurs, the client tries the request again.
- Note: “time out (v)” is not a verb in this profile. Write “a timeout occurs.”

## token (TN)
- Profile status: technical noun
- Decision: standard
- Basis: Rule 1.5, category 19. Issue 9 gives this word in its list of examples.
- Meaning: 1. A string that gives access to an API. 2. A unit of text that a large language model reads or writes
  - STE: After one hour, the token is expired.
- Note: This word has two meanings in software. In a text that can have the two meanings, use “API token” or “model token.”

## transaction (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A set of database operations. The database does all the operations or none of them. If one operation stops with an error, the database cancels all the operations.
  - STE: Put the two `UPDATE` queries in one transaction.
- Note: To end a transaction, write the SQL command in code format, for example `COMMIT`. commit (v) in [verbs.md](verbs.md#commit-v) is only for version control. roll back (v) is applicable to a transaction.
- Related: [lock (TN)](#lock-tn), [query (TN)](#query-tn)

## unit test (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A test of one function or one small part of a program, without its dependencies
  - STE: Write a unit test for each new function.
- Note: TEST (n) is approved in Issue 9. “test (v)” is not approved.

## update (TN)
- Profile status: technical noun
- Decision: standard
- Basis: Rule 1.5, category 19. Issue 9 gives “update” in its list of examples.
- Meaning: A new version of software or data that replaces the version that you have
  - STE: Reboot the host after you install the kernel update.
- Related: update (v) in [verbs.md](verbs.md#update-v)

## URL (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: Uniform Resource Locator. The location of a page, a file, or an API on a network, for example `https://example.com/docs`
  - STE: Enter the URL of the dashboard in your browser.
- Do not use: link (for the URL), web address, URI (unless the difference is important)
- Related: [endpoint (TN)](#endpoint-tn)

## user (TN)
- Profile status: technical noun
- Decision: accepted
- Basis: Rule 1.5, category 11 (professional roles, individuals, groups)
- Meaning: A person who uses a program or a service
  - STE: The user must enter a password with a minimum of 12 characters.
- Do not use: end user, customer (unless the text is about a customer)
- Note: Issue 9 gives “end user” in category 20. This profile uses “user” for the same item (Rule 1.11).

## variable (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A name in code or in an environment that refers to a value
  - STE: Set the `DATABASE_URL` environment variable before you start the service.

## version (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A specified condition of software, identified by a number or a name
  - STE: Upgrade the database to version 16.

## webhook (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: An HTTP request that a service sends automatically to a URL that you give, when an event occurs
  - STE: When a user opens a pull request, GitHub sends a webhook to the `/hooks/github` endpoint.
- Do not use: hook (for a webhook), HTTP callback
- Related: [event (TN)](#event-tn), [endpoint (TN)](#endpoint-tn)

## worker (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: A process that gets tasks from a queue and does them
  - STE: The worker gets one task at a time from the queue.
- Do not use: consumer (for the process that does the tasks)
- Related: [queue (TN)](#queue-tn), [process (TN)](#process-tn)

## working tree (TN)
- Profile status: technical noun
- Decision: accepted
- Meaning: The files of a repository that you can see and change in your local directory
  - STE: Make sure that the working tree has no changes before you rebase your branch.
- Do not use: working directory, working copy, workspace, checkout
- Related: [repository (TN)](#repository-tn)
