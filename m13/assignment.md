# M13 Assignment - Platform Access Control

## What you are doing, and why

You will build the role-based access control layer for Harborwatch's own SOC platform. The parent class that defines what every user can do, and the custom exception that fires when someone asks for a tool their role does not grant, are given to you complete; your job is to read them, make one change to them, and then build the three role classes that extend them. Role hierarchies map to class inheritance because that is literally what inheritance models: shared capability with specialized extension. Every user can view the dashboard; a senior analyst can do that plus close tickets and export reports; an admin can do all of that plus manage users. This is the densest weekly assignment in the course (inheritance, `super()`, method overriding, `__str__`, custom exceptions, `raise`, and the full `try`/`except`/`else`/`finally` shape all land in one program), and that is intentional: they are one system, and access control is where they meet.

## Scenario

Least privilege is the control every audit checks first. When the auditors come through Harborwatch, the opening question is always the same: who can do what, and what stops them from doing more? Right now the platform has no answer: every account can reach every tool, which means a junior analyst who can run `manage_users` is a privilege-escalation incident waiting for a phish. One compromised entry-level account and the attacker owns user management. Your lead has assigned you the fix: build the permission layer, so that every tool request is checked against the requester's role, and every request outside that role is refused loudly enough to show up in the logs.

## What you are given

- [Starter file](m13_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and a create part where the final step's design is yours to write.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. New this module: the final create step (3f) ships with no pseudocode. You write your own first, then translate it, which is the design habit the last stretch of this course builds.

1. Download the starter file and rename it with your own name, all lowercase: `m13_jane_doe.py` for Jane Doe. Keep the `m13_` prefix.
2. **Read.** Part 1 is already complete: the `AccessDeniedError` exception, the full `PlatformUser` parent class (`user_count`, `__init__`, `__str__`, `login()`, `get_permissions()`, and `request_tool()`, which raises `AccessDeniedError` when a tool is outside the user's permissions), and one demo user, Avery, exercised so you can watch each piece work. Run the program and read the output. Then follow the comment near the end of Part 1: uncomment the denied request, run once, read the `AccessDeniedError` traceback (that crash-with-a-name is what `raise` does), and comment it back out.
3. **Modify.** Every user should also see the alert feed. In `get_permissions()` in Part 1, change the default list `["view_dashboard"]` to `["view_dashboard", "view_alerts"]`, run again, and compare Avery's permission line with what it printed before.
4. **Create.** Part 3 has no code yet. Steps 3a–3e carry pseudocode as usual; follow it line by line. Step 3f carries only the requirement, and you write your own pseudocode as comments before coding it (UPPERCASE verbs, one line per line of code, the same style as 3a–3e; your pseudocode stays in the file and is part of what you submit). Together the six steps build: the three child classes `AdminUser`, `SeniorAnalyst`, and `JuniorAnalyst`, each calling `super().__init__()` and overriding `get_permissions()` with its role's list (3a–3c); one object of each, printed, logged in, and its permissions shown (3d); one `isinstance()` check and one `issubclass()` check proving the inheritance is real (3e); and the escalation test, a full `try`/`except`/`else`/`finally` block in which Riley's allowed `run_scan` request prints and the `manage_users` request raises `AccessDeniedError`, caught and printed with its `args`, followed by the total user count read from the class itself, `PlatformUser.user_count` (3f). The `except` block is your caught privilege-escalation attempt: the exact moment the permission layer earns its keep; the `else` block only runs when nothing was raised, so it stays silent here, and `finally` prints its closing line no matter what.
5. Run the program one last time and check that your output matches the expected output below.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. Every program you submit in this course carries this header; professionals sign their work, and so do you.

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

This is the output after your Part 2 change, with the denied request in Part 1 commented back out. The count is `4` because Avery, the Part 1 demo user, counts too.

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

Before you upload, confirm four things: the file is renamed with your own name, it runs in Thonny without errors and matches the expected output, every header field contains your text rather than the placeholder text, and step 3f's pseudocode comments are your own writing.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
