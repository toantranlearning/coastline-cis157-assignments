# M14 Assignment - Server-Log Hunt

## What you are doing, and why

You will write a program that reads a server log one line at a time, collects the `ERROR` and `WARNING` lines, and writes them to a report file. It practices the file handling from this module: a `with` block to open a file, reading line by line, a generator function that uses `yield`, and a second `with` block that writes a file. You will also handle the case where the log file is missing.

## Scenario

A client sent **Harborwatch Security** one day of raw server log and asked what happened. The log you are given is 119 lines. The logs the shop handles daily run to millions of lines, so the program must never load a whole file at once. Your program scans every line, pulls out the `ERROR` and `WARNING` lines, and writes a findings report your lead can skim.

## What you are given

- [Starter file](m14_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.
- [server.log](server.log). One day of server activity: routine messages with errors and warnings mixed in. Save it in the same folder as your program.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m14_jane_doe.py` for Jane Doe. Keep the `m14_` prefix. Download `server.log` into the same folder. Your program looks for the log in its own folder.
2. **Read.** Part 1 is already complete. Run the program and confirm it counts 119 lines.
   - Part 1 opens `server.log` with a `with` statement and reads it **line by line** with `for line in log_file`. It does not use `read()` or `readlines()`.
   - `read()` and `readlines()` load the whole file into memory before you look at a single line. Reading line by line holds one line in memory at a time, however big the file is.
   - With a 119-line log you will not notice the difference. With a million-line log, loading the whole file can use up memory and crash the program.
3. **Modify.** Part 2 counts every line that contains the text stored in the `PATTERN` constant. Right now that is `"ERROR"`. Change `PATTERN` to `"WARNING"` and run again. The count changes from 18 to 14. Changing one constant changes what the whole program searches for. Your Part 3 code searches lines the same way.
4. **Create.** Part 3 is all pseudocode: six steps, written out line by line. Follow them in order.
   - Define the generator function `def error_lines(path):`. It opens the log and **yields** each line that contains `ERROR`. A list would hold every matching line in memory at once. A generator hands over one line at a time, so it works on a log of any size.
   - Scan the log in a reading loop that counts the lines and collects the `WARNING` lines.
   - Consume the generator with a `for` loop to collect the `ERROR` lines.
   - Write every finding to `findings.txt`, header line first, using a `with` block that opens the file in write mode. Opening a file in `"w"` mode empties it the moment it opens, so write to `findings.txt` and nothing else.
   - Print the five-line summary.
   - Wrap the file access in `try`/`except FileNotFoundError`. When `server.log` is missing, the program must print a friendly message that says which file is missing and what to do about it. It must not end in a traceback.
5. Run the program and check every line against the expected output below. Then open `findings.txt` and confirm it has the header line first, then the findings.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain why a generator with yield can handle a log file too large to fit in memory.

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

The first two lines come from Parts 1 and 2, after your Part 2 change. The last five come from your Part 3 summary. Your wording may differ slightly, but the numbers must match. They are computed from the `server.log` you downloaded, so 119, 18, 14, and 32 are exact.

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

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed. Do not upload `findings.txt`. Anyone who runs your program creates it again, so I do not need a copy.

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
