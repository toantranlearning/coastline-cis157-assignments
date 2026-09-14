# M03 Assignment - IOC Intake Form

## What you are doing, and why

You will complete a program that collects a suspicious-activity report from the keyboard and prints it back as a clean, standardized intake record. Everything in it is week-two Python: variables, `input()`, an `int()` cast, division, f-strings, and the `\n` and `\t` escape sequences. Every tool you build later in this course starts by turning messy typed input into tidy named variables, and this is where you drill that move.

## Scenario

At **Harborwatch Security**, hunts start with a phone call. A client notices something off (a strange IP hammering their firewall, a file hash their antivirus flagged) and phones it in. Whoever picks up writes down an indicator of compromise (IOC), and every analyst who works the case afterward works from that record. If the intake is sloppy, the hunt starts from garbage. Your lead wants intake off of sticky notes: a small program that prompts the analyst for the details of the report, scores how confident the caller sounded, and prints one standardized record, the same shape every time.

## What you are given

- [Starter file](m03_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.

If you have not set up Thonny yet, do that first: Course Materials, Software & Technology page in Canvas.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m03_jane_doe.py` for Jane Doe. Keep the `m03_` prefix.
2. **Read.** Part 1 is already complete: it prompts for the analyst's name with `input()` and echoes it back inside an f-string. Run the program, type your name, and confirm you see the `Intake started by` line.
3. **Modify.** Part 2 builds the intake banner from two pieces with string concatenation (`+`), but the last word is wrong. Change `TRIAGE` to `INTAKE` and run again.
4. **Create.** Part 3 has no code yet: only pseudocode, one line of code per step. Follow it to prompt for the remaining fields (the indicator value, indicator type, and source; then the confidence score cast with `int()`), compute the confidence as a fraction of 100 with division, and print the record as one multi-line f-string using the `\n` and `\t` escape sequences.
5. Run the program, type in a test report, and check that your record matches the expected output below.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. Every program you submit in this course carries this header; professionals sign their work, and so do you.

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

The values you type at the prompts may differ: different analyst, indicator, source, or score. The record layout must not: the prompts, the `Intake started by` echo from Part 1, the corrected banner from Part 2, the blank line, and the tab-indented `[IOC RECORD]` block must match exactly.

```text
Analyst name: dana_reyes
Intake started by dana_reyes
=== HARBORWATCH IOC INTAKE ===
Indicator value (IP or file hash): 203.0.113.44
Indicator type: IP address
Source of report: client phone call
Confidence score (0-100): 85

[IOC RECORD]
	Analyst:    dana_reyes
	Indicator:  203.0.113.44
	Type:       IP address
	Source:     client phone call
	Confidence: 85/100 (0.85)
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs in Thonny without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
