# M06 Assignment - Hunt Utilities

## What you are doing, and why

You will write two functions of your own and call them. The assignment practices what this module teaches: defining a function with `def`, parameters and arguments (including a default value and a keyword argument), and `return`. Two guided experiments in Part 1 show what a function hands back when it has no `return` (the value `None`) and why a variable created inside a function cannot be used outside it (scope). Part 1 also gives you a recursive function to read and trace.

## Scenario

At **Harborwatch Security**, the dwell-time subtraction, the severity check, and the IOC formatting have each been written three times, in three different files, and the copies no longer match. The shop is moving that repeated work into a shared set of functions that are written once and called wherever they are needed. You complete the first four utilities and show that they work.

## What you are given

- [Starter file](m06_firstname_lastname.py). A header docstring to complete and three parts: a working function to read, a working function to modify, and two functions to create from line-by-line pseudocode.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m06_jane_doe.py` for Jane Doe. Keep the `m06_` prefix.
2. **Read.** Part 1 is already complete. Run the program first.
   - `dwell_time(start_hour, end_hour)` **returns** the hours elapsed: the hour detected minus the hour the compromise began. The call below it stores that value, then prints it. Find the dwell-time line in the output.
   - Try the two experiments in the observation comments. The first shows what `print()` hands back: `None`, the value of any function with no `return`. The second shows why `hours` raises a `NameError` outside the function, which is scope.
   - `alerts_through(tier)` is a function that calls **itself**. It totals the alerts reviewed by a tier and every tier beneath it. Find its base case, the `if tier == 0` line, which answers without calling again. Trace the calls on paper the way the observation comment describes, innermost call first. You are not asked to write recursion in this module. You are expected to read one and say what it prints.
3. **Modify.** `alert_banner(text, width=40)` in Part 2 has a **default value** for its second parameter. The shop's standard banner is 30 characters wide, so change the default from `40` to `30` and run again. The two calls already in the starter show both ways to call it: one leaves `width` at its default, and the other overrides it with the **keyword argument** `width=20`.
4. **Create.** Part 3 has no code yet, only pseudocode, in three numbered steps.
   - Define `severity_label(score)`. Use `if`/`elif`/`else` to **return** `"LOW"` for a score below 25, `"MEDIUM"` for 25-49, `"HIGH"` for 50-74, and `"CRITICAL"` for 75 and above. Return the label. Do not print inside the function.
   - Define `format_ioc(indicator, kind, confidence)`. It **returns** one record string built with an f-string, in exactly this shape: `[IP] 203.0.113.7 (confidence 85%)`.
   - Write the short main section that calls both functions and prints the results.
5. Run the program one last time and check that every line matches the expected output below, in order.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain the difference between print() and return.

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

There are no input prompts in this assignment. The program prints the same report on every run, so your output must match this exactly, line for line.

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

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
