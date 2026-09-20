# M03 Assignment - IOC Intake Form

## What you are doing, and why

You will complete a program that asks for the details of a suspicious-activity report at the keyboard and prints them back as one intake record. The assignment practices what this module teaches: variables, `input()`, an `int()` cast, division, f-strings, and the `\n` and `\t` escape sequences.

## Scenario

At **Harborwatch Security**, a client who sees something suspicious, such as a strange IP address hitting their firewall or a file hash their antivirus flagged, reports it by phone. The analyst who takes the call writes down an indicator of compromise (IOC), and every analyst who works the case later starts from that record. Your lead wants a small program to replace handwritten notes. It prompts the analyst for the details of the report, takes a score for how confident the caller sounded, and prints one record in the same layout every time.

## What you are given

- [Starter file](m03_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m03_jane_doe.py` for Jane Doe. Keep the `m03_` prefix.
2. **Read.** Part 1 is already complete. It prompts for the analyst's name with `input()` and echoes the name back inside an f-string. Run the program, type your name, and confirm you see the `Intake started by` line.
3. **Modify.** Part 2 builds the intake banner from two pieces with string concatenation (`+`). The last word of the banner is wrong. Change `TRIAGE` to `INTAKE` and run again.
4. **Create.** Part 3 has no code yet, only pseudocode. Each pseudocode step becomes one line of code.
   - Prompt for the remaining text fields, in this order: the indicator value, the indicator type, and the source of the report. Store each reply in its own variable.
   - Prompt for the confidence score and cast the reply with `int()`. `input()` always gives you a string, and you cannot divide a string.
   - Compute the confidence as a fraction of 100 with division, and store the result in a new variable.
   - Print the record as one multi-line f-string. Use the `\n` escape sequence to start each new line and the `\t` escape sequence to indent the lines under the record heading.
5. Run the program, type in a test report, and check that your record matches the expected output below.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain why the confidence score is cast with int() before it is divided.

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

The values you type at the prompts may differ from this sample: a different analyst, indicator, source, or score. The layout must match exactly. That covers the prompts, the `Intake started by` echo from Part 1, the corrected banner from Part 2, the blank line, and the tab-indented `[IOC RECORD]` block.

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

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
