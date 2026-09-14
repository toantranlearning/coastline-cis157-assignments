# M14 Assignment - Server-Log Hunt

## What you are doing, and why

You will build the course's capstone file tool: a log hunter that reads a server log one line at a time, pulls out the lines that matter, and files a findings report. Every tool from this module does its part in one program: a `with` block to open the evidence, line-by-line reading to survive logs of any size, a generator with `yield` to filter without loading, and a second `with` block to write the report. The job is the one that makes file handling worth learning: turning a wall of log noise into a short report a human can act on.

## Scenario

A client's server had a rough day, and this morning the raw log landed on **Harborwatch Security**'s desk with the only question clients ever ask: what happened? This is the hunt the whole course has been building toward. Nobody at a SOC reads a log top to bottom. The log you are handed here is 119 lines, but the ones the shop sees daily run to millions. You will build the tool that does the reading: scan every line, hunt the `ERROR` and `WARNING` signal out of the routine noise, and produce a findings report your lead can skim in ten seconds.

## What you are given

- [Starter file](m14_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.
- [server.log](server.log). The evidence: one day of server activity, routine messages with errors and warnings buried in them. Save it in the same folder as your program.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m14_jane_doe.py` for Jane Doe. Keep the `m14_` prefix. Download `server.log` into the same folder. Your program looks for the evidence right next to it.
2. **Read.** Part 1 is already complete: it opens `server.log` with a `with` statement and reads it **line by line**: `for line in log_file`, not `read()` or `readlines()`. Read-everything loads the whole file into memory before you look at a single line; line-by-line holds one line at a time no matter how big the file grows. For a 119-line practice log the difference is invisible; for the million-line logs this tool is really for, it is the difference between a program that runs and one that dies. Run the program and confirm it counts 119 lines.
3. **Modify.** Part 2 counts every line containing the pattern in the `PATTERN` constant: right now, `"ERROR"`. Change `PATTERN` to `"WARNING"`, run again, and watch the count change from 18 to 14. One constant redirects the whole hunt; that is the idea your Part 3 tool is built on.
4. **Create.** Part 3 is the hunt, and it is all pseudocode: six steps, spelled out line by line. Follow them in order: define the generator function `def error_lines(path):` that opens the log and **yields** each line containing `ERROR` (a list of every error means holding every error in memory at once; a generator hands you one line, forgets it, and moves on: a million-line log never fits in RAM, and a generator never has to); scan the log in a reading loop that counts lines and collects the `WARNING` lines; consume the generator with a `for` loop to collect the `ERROR` lines; write every finding to `findings.txt`, header line first, with a `with` open in write mode (`"w"` truncates the file the moment it opens: write to `findings.txt` and nothing else); print the five-line summary; and wrap the file access in `try`/`except FileNotFoundError` with a friendly message saying what file is missing and what to do about it. A hunt tool that dies in a traceback when the evidence is missing helps nobody.
5. Run the program, check every line against the expected output below, then open `findings.txt` and confirm the report reads clean: the header line, then the findings.
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

The first two lines come from Parts 1 and 2 (after your Part 2 change), the last five from your Part 3 summary. Your wording may differ slightly; the numbers may not. They are computed from the `server.log` you downloaded, so 119, 18, 14, and 32 are exact.

```text
Lines in log: 119
Lines containing WARNING: 14
Lines scanned: 119
ERROR findings: 18
WARNING findings: 14
Total findings: 32
Findings report written to findings.txt
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed. Do not upload `findings.txt`: anyone who runs your program regenerates it, so the report is your program's output, not a separate deliverable.

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
