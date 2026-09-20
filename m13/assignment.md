# M13 Assignment - Platform Access Control

## What you are doing, and why

You will build the role-based access control for the Harborwatch SOC platform. The parent class `PlatformUser` and the custom exception `AccessDeniedError` are given to you complete. You read them, make one change to them, and then write three role classes that inherit from the parent. Each role keeps what the role below it can do and adds to it: every user can view the dashboard, a senior analyst can also close tickets and export reports, and an admin can also manage users. The program uses everything from this module together: inheritance, `super()`, method overriding, `__str__`, custom exceptions, `raise`, and the full `try`/`except`/`else`/`finally` structure.

## Scenario

On the Harborwatch platform today, every account can reach every tool. A junior analyst can run `manage_users`, so one stolen entry-level account would give an attacker control of user management. That breaks least privilege, the rule that each account gets only the tools its role needs, and it is the first thing auditors check: who can do what, and what stops them from doing more. Your lead has assigned you the permission layer. Every tool request is checked against the requester's role, and a request outside that role is refused with an error that shows up in the logs.

## What you are given

- [Starter file](m13_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and a create part with pseudocode for steps 3a to 3e and none for step 3f.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter. The last create step, 3f, has no pseudocode. You write your own pseudocode first, then turn it into Python.

1. Download the starter file and rename it with your own name, all lowercase: `m13_jane_doe.py` for Jane Doe. Keep the `m13_` prefix.
2. **Read.** Part 1 is already complete. Run the program first and read the output.
   - Part 1 holds the `AccessDeniedError` exception, the full `PlatformUser` parent class, and one demo user, Avery. The lines under the class use Avery to show each piece working.
   - `PlatformUser` has a class variable, `user_count`, and these methods: `__init__`, `__str__`, `login()`, `get_permissions()`, and `request_tool()`. `request_tool()` raises `AccessDeniedError` when a tool is outside the user's permissions.
   - Follow the comment near the end of Part 1. Uncomment the denied request, run once, and read the `AccessDeniedError` traceback. The program stops and names the error, which is what `raise` does. Then comment the line back out so the rest of the program can run.
3. **Modify.** An account with no role of its own should see the alert feed as well as the dashboard. The three role classes you write in Part 3 override `get_permissions()` with their own lists, so this change does not reach them. The change goes in Part 1, inside `get_permissions()`. There is nothing to write in the Part 2 section itself.
   - Change the default list `["view_dashboard"]` to `["view_dashboard", "view_alerts"]`.
   - Run again and compare Avery's permission line with what it printed before.
4. **Create.** Part 3 has no code yet. It has six steps. Steps 3a to 3e have pseudocode, so follow it line by line. Step 3f gives only the requirement.
   - **3a to 3c.** Define the three child classes `AdminUser`, `SeniorAnalyst`, and `JuniorAnalyst`. Each one calls `super().__init__()` and overrides `get_permissions()` to return its role's list.
   - **3d.** Create one object of each class. For each one, print it, log it in, and show its permissions.
   - **3e.** Write one `isinstance()` check and one `issubclass()` check. They prove the inheritance is real.
   - **3f, pseudocode first.** Before you write any code for this step, write your own pseudocode as comments. Use UPPERCASE verbs and one line per line of code, the same style as 3a to 3e. Your pseudocode stays in the file and is part of what you submit.
   - **3f, the escalation test.** Write a full `try`/`except`/`else`/`finally` block. In the `try`, Riley's allowed `run_scan` request prints, and then the `manage_users` request raises `AccessDeniedError`. The `except` catches that error and prints it, then prints its `args`. After the block, print the total user count, read from the class itself: `PlatformUser.user_count`.
   - **3f, which branches run.** The `except` branch runs because the second request raised an error. That is the privilege-escalation attempt, caught. The `else` branch runs only when nothing was raised, so it prints nothing here. The `finally` branch prints its closing line whether or not an error was raised.
5. Run the program one last time and check that every line matches the expected output below, in order.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain why request_tool() raises AccessDeniedError instead of just printing an error message.

Open notes and open book are both fine. Respond in your own words; do not copy from other sources.

**Acceptable AI use.** Itemized for this course; the syllabus policy governs.

> [!TIP]
> **These uses are permitted**
> - Asking an AI to explain a course concept or a Python error message, in general terms, while you study.
> - Grammar and spelling help on the written reflection in your header.
> - After your program works: asking an AI to show a different approach, described in your own words, to compare with what you wrote.

> [!CAUTION]
> **These uses are not permitted**
> - Generating any part of the code or reflection you submit.
> - Pasting the assignment page or the starter file into an AI tool.
> - Submitting or paraphrasing AI output as your own work.

You must be able to explain every line you submit, on request. Undisclosed AI use is handled as academic dishonesty under the syllabus.

## Expected output

This is the output after your Part 2 change, with the denied request in Part 1 commented back out. The last line shows `4` because `user_count` counts Avery, the Part 1 demo user, along with your three users.

```text
=== Part 1: One Platform User ===
Avery (Contractor)
Avery logged in to the Harborwatch platform.
Permissions: ['view_dashboard', 'view_alerts']
Access approved: Avery may use view_dashboard.

=== Part 3: Platform Users ===
Morgan (Admin)
Morgan logged in to the Harborwatch platform.
Permissions: ['view_dashboard', 'run_scan', 'close_ticket', 'export_report', 'manage_users']
Dana (Senior Analyst)
Dana logged in to the Harborwatch platform.
Permissions: ['view_dashboard', 'run_scan', 'close_ticket', 'export_report']
Riley (Junior Analyst)
Riley logged in to the Harborwatch platform.
Permissions: ['view_dashboard', 'run_scan']

=== Class Checks ===
Riley is a PlatformUser: True
JuniorAnalyst is a subclass of PlatformUser: True

=== Privilege Escalation Test ===
Access approved: Riley may use run_scan.
Access denied: Riley cannot use manage_users.
Exception args: ('Access denied: Riley cannot use manage_users.',)
Access control check complete.
Total platform users created: 4
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm four things: the file is renamed with your own name, it runs without errors and matches the expected output, every header field contains your text, not the placeholder text, and step 3f's pseudocode comments are your own writing.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
