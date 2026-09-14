# M11 Assignment - Dirty-Log Field Extractor

## What you are doing, and why

You will write a parser that pulls fields out of a pipe-delimited log dump, and survives the records that are broken. The Python is this module's string and exception toolkit: `.strip()`, `.split()`, and a `try`/`except`/`else` around the risky work. The point underneath is exception specificity: your `except ValueError` catches exactly the one failure you expect (a cast that could not produce a number) instead of a bare `except` that would silently swallow every bug you have not met yet. Catch what you expect, let the rest crash loudly: that discipline is what separates a parser from a program that merely has not crashed today. A tool that dies on line 3 of a 10,000-line export hunts nothing.

## Scenario

A Harborwatch client exported their gateway log to a pipe-delimited text dump and sent it over for review. Like every real export, it is dirty: somewhere in the batch a record lost a field, one has letters where the hour should be, one is padded with stray whitespace, and one line is simply blank. Your lead wants a field extractor that parses every record it can, rejects the ones it cannot (with a reason), and reports the hunt totals: how many parsed, how many rejected and why, and how many failed logins. In the real world this dump would arrive as a file; file reading comes in M14, so this week the records are handed to you as an in-code list and your whole job is the parsing.

## What you are given

- [Starter file](m11_firstname_lastname.py). A header docstring to complete, the `records` list already loaded with the client's ten raw records (dirt included: do not edit the list), and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.

If you have not set up Thonny yet, do that first: Course Materials, Software & Technology page in Canvas.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m11_jane_doe.py` for Jane Doe. Keep the `m11_` prefix.
2. **Read.** Part 1 is already complete: it takes one clean record from the `records` list, `.split()`s it on `"|"`, and prints each field. Run the program and match each printed field back to the record it came from: hour, username, source IP, status. That is the whole parsing move; Part 3 just repeats it inside a loop, on records that fight back.
3. **Modify.** Part 2 cleans a record with `.strip()`, but it cleans `records[0]`, which was never dirty. Change it to clean `records[2]`, the whitespace-padded record, and run again. Notice what `.strip()` removed (the outer spaces) and what it did not (the spaces around the inner fields). That is why your parser will strip every field, not just the record.
4. **Create.** Part 3 is the parser itself, laid out as line-by-line pseudocode. Loop over the records: `.strip()` each one and skip blanks with `continue`; `.split("|")` and reject any record that does not have exactly 4 fields, recording the reason in an `errors` list; `.strip()` each field; then cast the hour with `int()` inside a `try`, catching `ValueError` for hours that are not numbers. Put the success path in the `else` clause: print the parsed record and tally your counters there.
5. After the loop, print the hunt summary shown in the expected output: records parsed, records rejected with their reasons, and failed logins.
6. Run the program and check that your output matches the expected output below, line for line. Parts 1 and 2 print too.
7. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. Every program you submit in this course carries this header; professionals sign their work, and so do you.

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

The data is fixed and the program takes no input, so your output must match exactly: every line, in this order. The first six lines come from Parts 1 and 2; the rest is your parser.

```text
record: 14|jdoe|203.0.113.44|fail
hour: 14
user: jdoe
ip: 203.0.113.44
status: fail
cleaned: 14 | jdoe | 203.0.113.44 | fail
parsed: 14 jdoe 203.0.113.44 fail
parsed: 02 asmith 198.51.100.23 ok
parsed: 14 jdoe 203.0.113.44 fail
parsed: 15 jdoe 203.0.113.44 ok
parsed: 03 asmith 198.51.100.23 fail
parsed: 23 jdoe 203.0.113.44 fail
parsed: 04 asmith 192.0.2.150 ok

=== Hunt summary ===
Records parsed: 7
Records rejected: 2
  xx|npatel|192.0.2.150|ok  [hour is not a number]
  22|mallory|203.0.113.99  [wrong field count]
Failed logins: 4
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs in Thonny without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
