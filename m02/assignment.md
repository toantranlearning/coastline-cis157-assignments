# M02 Assignment - Dwell-Time Report

## What you are doing, and why

You will write a program that computes the numbers in an incident report and prints them in a fixed layout. Everything it needs is this module's material and nothing more: `print()` with its `sep` and `end` arguments, the escape sequences `\n` and `\t`, Python's literals, the arithmetic operators, and the parentheses that decide what runs first. There is nothing to type in and nothing to store: the incident's numbers are known, and your job is the arithmetic that turns them into a report.

## Scenario

Back at **Harborwatch Security**, your lead has real work for you this week. The first number in every hunt report the shop sends out is **dwell time**: how long an attacker sat inside a client's network before anyone noticed. Analysts have been working it out by hand for the Meridian Freight case, along with a triage rate and a risk score, and typing the results into the report. Your lead wants that arithmetic written down once, as a program that prints the report block the same way every time.

## What you are given

- [Starter file](m02_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and line-by-line pseudocode to turn into your own code.

## Instructions

Same three-step rhythm as every assignment in this course: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m02_jane_doe.py` for Jane Doe. Keep the `m02_` prefix.
2. **Read.** Part 1 is already complete. It prints four values in three calls, and the interesting part is the spacing. The first call passes three values with no `sep`, so Python uses its default of a single space. The second replaces that default with `" | "`. The third sets `end=" "`, which replaces the newline print normally adds, so `DRAFT` lands on the same line. Run it and match each printed line to the call that made it.
3. **Modify.** Part 2 uses the escape sequences `\n`, which starts a new line, and `\t`, which jumps to the next tab stop. The banner is followed by one blank line, because the `\n` at the end of the string makes one and `print()` adds another. The shop standard is **two** blank lines before a report body. Add one more `\n` to the end of the banner string, run again, and count.
4. **Create.** Part 3 has no code yet, only pseudocode, in four blocks. The incident is already decided: the compromise began at hour 3, it was detected at hour 53, 24 alerts were raised, and 18 were triaged. Write those numbers straight into your expressions and let Python do the arithmetic; do not work an answer out yourself and type the result. The one line to slow down on is the days-and-hours line, where `(53 - 3) // 24` needs its parentheses. Floor division sits higher than subtraction in the priority table, so without them Python divides 3 by 24 first and the answer is wrong. Try it both ways once it works, then put them back.
5. Run the program one last time and check it against the expected output below, line for line and blank line for blank line.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot.

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

The whole program is fixed: there is nothing to type in, so every run prints exactly this. The blank lines are part of it, including the two after the banner that you created in Part 2.

```text
Harborwatch Security dwell-time report
Hours | Alerts | Risk
Report status: DRAFT

=== Harborwatch Security - Dwell-Time Report ===


Client:	Meridian Freight
Analyst:	J. Okafor

Timeline
  Began at hour 3
  Detected at hour 53
  Dwell time: 50 hours
  That is 2 days and 2 hours

Alerts
  Raised: 24
  Triaged: 18
  Untriaged: 6
  Triage rate: 0.75

Risk
  Score: 130
  A beacon doubling hourly for 5 hours reaches 32
  Escalation required: True

Prepared by / Harborwatch Security / Tier 1
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
