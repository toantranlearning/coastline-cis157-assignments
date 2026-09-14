# M15 Assignment - Incident Timeline Builder

## What you are doing, and why

You will turn a jumble of timestamped events into the chronological timeline that anchors an incident report. Back in M02 you computed dwell time by subtracting one bare hour number from another, which only worked because that incident conveniently started and ended on the same day. Real incidents span days, and this week you solve the same problem with the real tools: parsing timestamp strings into `datetime` objects with `strptime`, sorting them, measuring gaps as `timedelta`s, formatting output with `strftime`, and using the `calendar` module for the report's month grid.

## Scenario

The hunt you ran in M14 for **Harborwatch Security** turned up six timestamped events on the client's network, and now the client is asking the question every incident report must answer: **how long were they inside, and what happened when?** The events were recovered in the order the hunt found them, not the order they happened. Your lead wants a program that puts them in order, shows the gap between each step of the intrusion, computes total dwell time, and stamps the report with when it was generated.

## What you are given

- [Starter file](m15_firstname_lastname.py). A header docstring to complete, the six recovered events already provided as a list of `(description, timestamp)` tuples, and three parts: working code to read, working code to modify, and six requirements you design and build yourself.

If Thonny is not set up yet, do that first: Course Materials, Software & Technology page in Canvas.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own. This time the create step changes: every starter until now handed you the pseudocode, and from here the design step is yours, which is how the job works.

Two functions do all the string work this week, and both speak the same little format-code language: `datetime.strptime(text, format)` reads a string in and returns a `datetime`; `some_datetime.strftime(format)` writes a string out. The codes you need:

| Code | Meaning | Example |
| --- | --- | --- |
| `%Y` | four-digit year | `2026` |
| `%m` | two-digit month | `07` |
| `%d` | two-digit day | `13` |
| `%H` | hour, 24-hour clock | `14` |
| `%M` | minute | `47` |
| `%a` | weekday name, short | `Mon` |
| `%b` | month name, short | `Jul` |

One warning before you start: `%m` is **month** and `%M` is **minute**. Swap them and Python will not raise an error. It will cheerfully parse minutes as months and hand you dates that look plausible and are wrong. If your gaps or your dwell time look bizarre, check your format string first.

1. Download the starter file and rename it with your own name, all lowercase: `m15_jane_doe.py` for Jane Doe. Keep the `m15_` prefix.
2. **Read.** Look at the `EVENTS` list and `TIMESTAMP_FORMAT` at the top of the starter: the six events are given; do not edit them. Part 1 is already complete: it takes one event's timestamp string, parses it into a `datetime` object with `datetime.strptime()`, and prints it twice: the raw string, then the same moment reformatted with `strftime()`. Run the program and compare the two lines.
3. **Modify.** Part 2 prints that same moment in timeline style, but the format string is missing the weekday. Change `"%b %d, %H:%M"` to `"%a %b %d, %H:%M"` and run again. `%a` adds the short weekday name, and this is exactly the format your timeline will use.
4. **Create.** Part 3 lists six requirements and no pseudocode. For each requirement, first write your own pseudocode as comments in the starter's usual style (UPPERCASE verbs, one line per line of code), then translate it into Python beneath. Your pseudocode stays in the file and is part of what you submit. The six requirements: parse every event into a list of `(datetime, description)` tuples; sort the list with plain `.sort()` (the `datetime` comes first in each tuple, so no sort key is needed); print the timeline with each event's gap since the previous one as a `timedelta` (the first event prints `(first event)` instead); compute dwell time (the `Detection` event's `datetime` minus the earliest), printed as a `timedelta` and as whole hours; stamp the report with `datetime.now()`; and print the compromise month's grid with `calendar.month()` plus its caption line.
5. Run the program, check your timeline, gaps, dwell time, and calendar grid against the expected output below, then complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot.

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

One line in this sample depends on the moment you run it: the `Report generated` stamp will match your run, not this sample. Everything else (the Part 1 and Part 2 lines, the event order, every gap, the dwell time, the calendar grid, and the layout) must match exactly.

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
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm four things: the file is renamed with your own name, it runs in Thonny without errors and matches the expected output, every header field contains your text rather than the placeholder text, and the Part 3 pseudocode comments are your own writing.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
