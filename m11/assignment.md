# M11 Assignment - Dirty-Log Field Extractor

## What you are doing, and why

You will write a parser that pulls the fields out of pipe-delimited log records and keeps running when a record is broken. It practices this module's string methods and exception handling: `.strip()`, `.split()`, and a `try`/`except`/`else` around the code that can fail. Your `except` names one exception, `ValueError`, which is what a cast raises when the text is not a number. A log export can have 10,000 lines. If the program crashes on a bad record at line 3, none of the lines after it get parsed.

## Scenario

A Harborwatch client exported a gateway log as pipe-delimited text and sent it in for review. Some records are damaged: one is missing a field, one has letters where the hour should be, one is padded with extra spaces, and one line is blank. Your program parses every record it can, rejects the ones it cannot and gives a reason, and prints the hunt totals: records parsed, records rejected with their reasons, and failed logins. Reading files comes in M14, so in this module the records are already in the starter as a list, and your work is the parsing.

## What you are given

- [Starter file](m11_firstname_lastname.py). A header docstring to complete, the `records` list holding the client's ten raw records, and three parts: working code to read, working code to modify, and pseudocode to turn into your own code. Do not edit the `records` list. The damaged records are there on purpose.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m11_jane_doe.py` for Jane Doe. Keep the `m11_` prefix.
2. **Read.** Part 1 is already complete. It takes one clean record from the `records` list, splits it on `"|"` with `.split()`, and prints each field. Run the program and match each printed field to the record it came from: hour, username, source IP, status. Part 3 does the same split inside a loop, on records that may be damaged.
3. **Modify.** Part 2 cleans a record with `.strip()`, but it cleans `records[0]`, which has no extra spaces, so nothing changes. Change it to clean `records[2]`, the record padded with spaces, and run again. Look at what `.strip()` removed (the spaces at the two ends) and what it left (the spaces around the inner fields). That is why your parser strips every field and not only the whole record.
4. **Create.** Part 3 is the parser. The starter lays it out as line-by-line pseudocode. Loop over the records, and for each one:
   - `.strip()` the record. If nothing is left, it was a blank line, so skip it with `continue`. A blank line is not an error and does not go in the `errors` list.
   - `.split("|")` the record. If it does not have exactly 4 fields, reject it: add the record and the reason to an `errors` list, then go on to the next record.
   - `.strip()` each field.
   - Cast the hour with `int()` inside a `try`. When the hour is not a number, `int()` raises `ValueError`. Catch it and add the record and the reason to `errors`.
   - Write `except ValueError`, not a bare `except`. A bare `except` would catch every error, so it would also hide bugs you have not found yet.
   - Put the success path in the `else` clause. Print the parsed record and add to your counters there.
5. After the loop, print the hunt summary shown in the expected output: records parsed, records rejected with their reasons, and failed logins.
6. Run the program and check that your output matches the expected output below, line for line. Parts 1 and 2 print too.
7. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain why catching ValueError specifically is better here than a bare except.

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

The data is fixed and the program takes no input, so your output must match this exactly, line for line and in this order. The first six lines come from Parts 1 and 2. The rest comes from your parser.

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

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
