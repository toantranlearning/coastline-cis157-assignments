# M02 Assignment - Dwell-Time Report

## What you are doing, and why

You will write a program that computes the numbers in an incident report and prints them in a fixed layout. It practices what this module teaches: `print()` with its `sep` and `end` arguments, the escape sequences `\n` and `\t`, Python's literals, the arithmetic operators, and the parentheses that decide what runs first. The program takes no input and stores nothing. The incident's numbers are given, and you write the arithmetic that turns them into the report.

## Scenario

At **Harborwatch Security**, every hunt report starts with **dwell time**: how long an attacker was inside a client's network before anyone noticed. For the Meridian Freight case, analysts have been working out the dwell time, a triage rate, and a risk score by hand and typing the results into the report. Your lead wants that arithmetic written once, as a program that prints the report block the same way every time.

## What you are given

- [Starter file](m02_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and line-by-line pseudocode to turn into your own code.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m02_jane_doe.py` for Jane Doe. Keep the `m02_` prefix.
2. **Read.** Part 1 is already complete. Its four `print()` calls print three lines. Look at the spacing in each line.
   - The first call passes three values and no `sep`. Python puts its default between them, which is a single space.
   - The second call replaces that default with `" | "`.
   - The third call sets `end=" "`. That replaces the newline `print()` normally adds at the end, so the next call prints `DRAFT` on the same line.
   - Run the program and match each printed line to the call that made it.
3. **Modify.** Part 2 uses two escape sequences: `\n` starts a new line, and `\t` jumps to the next tab stop.
   - Run the program. The banner is followed by one blank line.
   - That blank line comes from two newlines in a row. The `\n` at the end of the string makes one, and `print()` adds another.
   - The shop standard is **two** blank lines before a report body. Add one more `\n` to the end of the banner string.
   - Run again and count the blank lines after the banner.
4. **Create.** Part 3 has no code yet, only pseudocode, in four blocks.
   - The incident is already decided. The compromise began at hour 3, it was detected at hour 53, 24 alerts were raised, and 18 were triaged.
   - Write those numbers straight into your expressions and let Python do the arithmetic. Do not work an answer out yourself and type the result.
   - Slow down on the days-and-hours line, where `(53 - 3) // 24` needs its parentheses. Floor division is higher than subtraction in the priority table. Without the parentheses, Python divides 3 by 24 first, and the answer is wrong.
   - Once that line works, try it both ways to see the difference. Then put the parentheses back.
5. Run the program one last time and check it against the expected output below, line for line and blank line for blank line.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain why the parentheses in the days-and-hours line change the answer.

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

There are no input prompts in this assignment. The program prints the same report on every run, so your output must match this exactly. The blank lines count too, including the two after the banner that you created in Part 2.

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

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
