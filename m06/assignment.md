# M06 Assignment - Hunt Utilities

## What you are doing, and why

You will package code you have already written into **functions** (named, reusable blocks defined with `def`) and then call them the way real tools do. Along the way you will use what this module covers: parameters and arguments (including a default value and a keyword argument), `return`, and, in guided observations along the way, what a function hands back when it has no `return` (the value `None`) and why a variable created inside a function is invisible outside it (scope). Nothing here is new math; what is new is that you write each piece once and call it as many times as you need.

## Scenario

Back at **Harborwatch Security**, your lead has been reading your last few hunts and noticed something: you have now written the dwell-time subtraction, the severity check, and the IOC formatting three different times, in three different files, with three slightly different sets of bugs. A hunter who copies code between hunts is a hunter who ships stale bugs: fix it in one place and the other two copies stay broken. This week the shop is standing up a shared toolkit: the repeated work becomes functions, written once, called everywhere. Your job is to stock the first four utilities and prove they work.

## What you are given

- [Starter file](m06_firstname_lastname.py). A header docstring to complete and three parts: a working function to read, a working function to modify, and two functions to create from line-by-line pseudocode.

If Thonny is not set up yet, do that first: Course Materials, Software & Technology page in Canvas.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m06_jane_doe.py` for Jane Doe. Keep the `m06_` prefix.
2. **Read.** Part 1 is already complete: `dwell_time(start_hour, end_hour)` **returns** the hours elapsed (the hour detected minus the hour the compromise began), and the call below it stores that value before printing it. Run the program and find the dwell-time line in the Shell. Then try the two Shell experiments in the observation comments: what `print()` hands back (`None`, the value of any function with no `return`), and why `hours` raises a `NameError` outside the function (scope). Part 1 then shows a function that calls **itself**: `alerts_through(tier)` totals the alerts reviewed by a tier and every tier beneath it. Read its base case, the `if tier == 0` line that answers without calling again, and trace the chain on paper the way the observation comment describes, innermost call first. You are not asked to write recursion this week, but you are expected to read one and say what it prints.
3. **Modify.** Part 2 gives you `alert_banner(text, width=40)`, whose second parameter has a **default value**, but the shop standard banner is 30 characters wide. Change the default from `40` to `30` and run again. The two calls already in the starter show both ways to call it: one leaves `width` at its default, the other overrides it with the **keyword argument** `width=20`.
4. **Create.** Part 3 has no code yet: only pseudocode, in three numbered steps. Define `severity_label(score)`, which uses `if`/`elif`/`else` to **return** `"LOW"` for a score below 25, `"MEDIUM"` for 25-49, `"HIGH"` for 50-74, and `"CRITICAL"` for 75 and above. Return the label, do not print inside the function. Define `format_ioc(indicator, kind, confidence)`, which **returns** one record string built with an f-string, in exactly this shape: `[IP] 203.0.113.7 (confidence 85%)`. Then write the short main section that calls both functions and prints the results.
5. Run the program one last time and check that every line matches the expected output below, in order.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot.

Open notes and open book are both fine. Respond in your own words; do not copy from other sources.

**Acceptable AI use.** Itemized for this course; the syllabus policy governs.

> [!TIP] These uses are permitted
> - Asking an AI to explain a course concept or a Python error message, in general terms, while you study.
> - Grammar and spelling help on the written reflection in your header.
> - After your program works: asking an AI to show a different approach, described in your own words, to compare with what you wrote.

> [!CAUTION] These uses are not permitted
> - Generating any part of the code or reflection you submit.
> - Pasting the assignment page or the starter file into an AI tool.
> - Submitting or paraphrasing AI output as your own work.

You must be able to explain every line you submit, on request. Undisclosed AI use is handled as academic dishonesty under the syllabus.

## Expected output

There are no input prompts this week: the program computes the same report every run, so your output must match this exactly, line for line.

```text
Dwell time, Meridian Freight: 14 hours
Alerts reviewed through tier 3: 6
==============================
HARBORWATCH HUNT UTILITIES
==============================
====================
SHIFT CHANGE
====================
Score 18 is LOW
Score 42 is MEDIUM
Score 67 is HIGH
Score 91 is CRITICAL
[IP] 203.0.113.7 (confidence 85%)
[DOMAIN] update-cdn.example.net (confidence 60%)
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs in Thonny without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
