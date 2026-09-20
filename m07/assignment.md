# M07 Assignment - Threat-Intel Lookup

## What you are doing, and why

You will build a threat-intel lookup tool: a dictionary maps each indicator to a **tuple** of details, one function looks an indicator up, another prints the whole table, and `try`/`except` handles the indicator that is not there. That last part carries the real lesson of the module: a miss in an intel table means *unknown*, not *safe*, and your program has to say so instead of crashing. Along the way you will read why the records are tuples: intel entries are evidence, and evidence should not be editable in place. You will add one new entry to the table yourself, because the table can grow even though its records cannot change.

## Scenario

Mid-hunt at **Harborwatch Security**, the question is always the same: *have we seen this indicator before?* An IP address turns up in a firewall log, a file hash comes out of a malware scan, and the analyst needs an answer in seconds. Harborwatch keeps a small internal threat-intel table: indicators the team has already investigated, each with a threat name, a confidence level, and a current status. Your lead wants a lookup tool: type in an indicator, get the record if there is one, and get a clear warning (not a crash, and not false reassurance) if there is not.

## What you are given

- [Starter file](m07_firstname_lastname.py). A header docstring to complete and three parts: working lookup code to read (with the intel table below already typed in), one new record to add, and full line-by-line pseudocode to turn into your own code.

The intel table your tool searches (in Part 2 you add one more record to it):

| Indicator | Threat Name | Confidence | Status |
|---|---|---|---|
| 203.0.113.44 | Emotet C2 | High | Active |
| 198.51.100.7 | Cobalt Strike beacon | High | Active |
| 192.0.2.126 | Cryptomining pool | Medium | Contained |
| d41d8cd98f00 | AgentTesla dropper | High | Active |
| 9e107d9d372b | Mirai variant | Low | Retired |
| e99a18c428cb | Phishing kit payload | Medium | Active |
| 203.0.113.99 | TOR exit scanner | Low | Retired |

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m07_jane_doe.py` for Jane Doe. Keep the `m07_` prefix.
2. **Read.** Open the file and run it. Part 1 is already complete: the `INTEL` dictionary is the table above, and two working lines look up one indicator, first pulling out the whole record (a tuple, parentheses and all), then unpacking it into its three parts. Read the closing comment too: the records are tuples on purpose, because intel entries are evidence and should not be editable in place.
3. **Modify.** Part 2 gives you the pattern for a dictionary item assignment and one confirmed new record: indicator `198.51.100.23`, threat name `Qakbot loader`, confidence `High`, status `Active`. Add it to `INTEL` with one line of code.
4. **Create.** Part 3 has no code yet: only pseudocode. Follow it line by line to build:
   1. A function `lookup_ioc(intel, indicator)` that looks the indicator up and returns its details.
   2. A function `print_intel(intel)` that prints the whole table, one line per indicator, iterating with `.items()` and unpacking each tuple into its three parts.
   3. A prompt asking the user for an indicator.
   4. A `try`/`except` around the lookup: a hit prints the match line; a `KeyError` prints a message saying the indicator is **not in intel: treat it as unknown, not as safe** (that phrasing or similar; the point is that a miss is not a clean bill of health).
   5. A closing call to `print_intel` so every run ends with the full table, including your new entry from Part 2.
5. Run the program twice (once with an indicator from the table, once with one that is not) and check both runs against the expected output below.
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

Your wording and column spacing may differ; the pieces of each run (the Part 1 lines, the lookup result or miss message, and the full table ending with your new entry) must not. A run with an indicator that is in the table (the indicator you type appears after the prompt on your screen):

```text
d41d8cd98f00 -> ('AgentTesla dropper', 'High', 'Active')
Threat: AgentTesla dropper | Confidence: High | Status: Active

=== Harborwatch Threat-Intel Lookup ===
Enter an indicator (IP or hash): d41d8cd98f00

Match: d41d8cd98f00 | Threat: AgentTesla dropper | Confidence: High | Status: Active

--- Full Threat-Intel Table ---
203.0.113.44 | Emotet C2 | High | Active
198.51.100.7 | Cobalt Strike beacon | High | Active
192.0.2.126 | Cryptomining pool | Medium | Contained
d41d8cd98f00 | AgentTesla dropper | High | Active
9e107d9d372b | Mirai variant | Low | Retired
e99a18c428cb | Phishing kit payload | Medium | Active
203.0.113.99 | TOR exit scanner | Low | Retired
198.51.100.23 | Qakbot loader | High | Active
```

A run with an indicator that is not in the table (for example `10.9.9.9`) prints your unknown-not-safe message in place of the `Match:` line (`No record of 10.9.9.9 in intel -- treat it as UNKNOWN, not as safe.`), then the same table.

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
