# M15 Assignment - Incident Timeline Builder

## What you are doing, and why

You will write a program that puts timestamped events in order and prints the timeline for an incident report. In M02 you found dwell time by subtracting one hour number from another, which worked only because that incident started and ended on the same day. This incident runs across several days, so you use the date tools from this module. You parse timestamp strings into `datetime` objects with `strptime`, sort them, measure the gaps as `timedelta` values, and format the output with `strftime`. You also use the `calendar` module to print the report's month grid and the `os` module to file the finished report in a folder under a dated name.

## Scenario

The hunt you ran in M14 for **Harborwatch Security** found six timestamped events on the client's network. The client wants to know **how long the intruders were inside, and what happened when**. The events are listed in the order the hunt found them, which is not the order they happened. Your lead wants a program that puts them in order, shows the gap between each event and the one before it, computes total dwell time, stamps the report with the time it was generated, and files a summary in the case folder under a dated name.

## What you are given

- [Starter file](m15_firstname_lastname.py). A header docstring to complete, the six recovered events already provided as a list of `(description, timestamp)` tuples, and three parts: working code to read, working code to modify, and seven requirements you design and build yourself.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own. Every starter before this one gave you the pseudocode for the create step. In this one, Part 3 has no pseudocode, so you write it yourself before you write the code.

Two functions do the string work in this module, and both use the same format codes. `datetime.strptime(text, format)` reads a string and returns a `datetime`. `some_datetime.strftime(format)` takes a `datetime` and returns a string. The codes you need:

| Code | Meaning | Example |
| --- | --- | --- |
| `%Y` | four-digit year | `2026` |
| `%m` | two-digit month | `07` |
| `%d` | two-digit day | `13` |
| `%H` | hour, 24-hour clock | `14` |
| `%M` | minute | `47` |
| `%a` | weekday name, short | `Mon` |
| `%b` | month name, short | `Jul` |

`%m` is **month** and `%M` is **minute**. If you swap them, Python raises no error. It reads the minutes as a month and returns a date that looks plausible and is wrong. If your gaps or your dwell time look wrong, check your format string first.

1. Download the starter file and rename it with your own name, all lowercase: `m15_jane_doe.py` for Jane Doe. Keep the `m15_` prefix.
2. **Read.** Part 1 is already complete. Run the program first.
   - Look at the `EVENTS` list and `TIMESTAMP_FORMAT` at the top of the starter. The six events are given. Do not edit them.
   - Part 1 takes one event's timestamp string and parses it into a `datetime` object with `datetime.strptime()`.
   - It then prints that moment twice: the raw string, then the same moment reformatted with `strftime()`. Compare the two lines in the output.
3. **Modify.** Part 2 prints that same moment in timeline style, but the format string is missing the weekday. Change `"%b %d, %H:%M"` to `"%a %b %d, %H:%M"` and run again. `%a` adds the short weekday name. Your timeline in Part 3 uses this same format.
4. **Create.** Part 3 lists seven requirements and no pseudocode. For each requirement, first write your own pseudocode as comments in the starter's usual style (UPPERCASE verbs, one line per line of code). Then translate it into Python beneath the comments. Your pseudocode stays in the file and is part of what you submit. The seven requirements:
   - Parse every event into a list of `(datetime, description)` tuples.
   - Sort the list with plain `.sort()`. The `datetime` comes first in each tuple, so no sort key is needed.
   - Print the timeline. Each event shows its gap since the previous event as a `timedelta`. The first event prints `(first event)` instead.
   - Compute dwell time: the `Detection` event's `datetime` minus the earliest one. Print it as a `timedelta` and as whole hours.
   - Stamp the report with `datetime.now()`.
   - Print the compromise month's grid with `calendar.month()`, then its caption line.
   - File the report with the `os` module, in this order:
      - Make a folder named `case_files` with `os.mkdir()`. Catch `FileExistsError` so a second run carries on.
      - Write a two-line summary to `case_files/draft.txt`.
      - Build the final file name: `timeline_` plus the earliest event's date.
      - Check `os.listdir()` for a file that already has the final name. If there is one, delete it with `os.remove()`.
      - Rename the draft to the final name with `os.rename()`. Remove first because `os.rename()` raises an error on Windows when the new name is taken, and on macOS and Linux it overwrites the file with no message. Removing the old file makes your program do the same thing on every computer and on every run.
      - Print the two filing lines.
5. Run the program twice. Check your timeline, gaps, dwell time, calendar grid, and the two filing lines against the expected output below. Confirm the second run ends the same way as the first. Open `case_files` and read the file your program made. Then complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain the difference between %m and %M in a format string.

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

One line depends on when you run the program: the `Report generated` stamp shows the time of your run. Everything else must match this sample exactly: the Part 1 and Part 2 lines, the event order, every gap, the dwell time, the calendar grid, the two filing lines, and the layout.

```text
Raw timestamp from the list: 2026-07-16 03:12
Reformatted with strftime:   Jul 16, 03:12
Timeline style: Thu Jul 16, 03:12

=== Harborwatch Security - Incident Timeline ===
Mon Jul 13, 09:47  Initial phishing link clicked (first event)
Mon Jul 13, 10:02  First C2 beacon observed (+0:15:00 after previous)
Thu Jul 16, 03:12  Lateral movement to file server (+2 days, 17:10:00 after previous)
Fri Jul 17, 22:41  Data staged for exfiltration (+1 day, 19:29:00 after previous)
Sat Jul 18, 14:30  Detection - EDR alert triaged (+15:49:00 after previous)
Sat Jul 18, 16:05  Containment - host isolated (+1:35:00 after previous)

Dwell time: 5 days, 4:43:00 (124 whole hours)

Report generated: 2026-08-15 03:56

     July 2026
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

Compromise began this month, on Mon Jul 13.

Report filed: case_files/timeline_2026-07-13.txt
Files in case_files: ['timeline_2026-07-13.txt']
```

The file your program writes, `case_files/timeline_2026-07-13.txt`, holds two lines:

```text
Incident timeline: 6 events
Dwell time: 5 days, 4:43:00 (124 whole hours)
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed. Do not upload the `case_files` folder. I run your program, and it makes the folder again.

Before you upload, confirm four things: the file is renamed with your own name, it runs without errors and matches the expected output, every header field contains your text and no placeholder text, and the Part 3 pseudocode comments are your own writing.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
