# M07 Assignment - Threat-Intel Lookup

## What you are doing, and why

You will build a threat-intel lookup tool. A dictionary maps each indicator to a **tuple** of details. One function looks up an indicator, another prints the whole table, and `try`/`except` handles an indicator that is not in the table. When a lookup misses, your program must keep running and tell the user to treat the indicator as unknown, not as safe. Part 1 explains why the records are tuples. In Part 2 you add one new entry yourself, because a dictionary can take new entries even though each tuple record cannot be changed.

## Scenario

At **Harborwatch Security**, analysts find indicators during a hunt, such as an IP address in a firewall log or a file hash from a malware scan. They need to know whether the team has seen that indicator before. Harborwatch keeps a small internal threat-intel table of indicators the team has already investigated, each with a threat name, a confidence level, and a current status. Your lead wants a lookup tool: the user types an indicator and gets the record if there is one, or a clear warning if there is not.

## What you are given

- [Starter file](m07_firstname_lastname.py). A header docstring to complete and three parts: working lookup code to read (with the intel table below already typed in), one new record to add, and full line-by-line pseudocode to turn into your own code.

This is the intel table your tool searches. In Part 2 you add one more record to it.

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

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m07_jane_doe.py` for Jane Doe. Keep the `m07_` prefix.
2. **Read.** Part 1 is already complete. Run the program first.
   - The `INTEL` dictionary is the table above. Each key is an indicator, and each value is a tuple of threat name, confidence, and status.
   - Two working lines look up one indicator. The first pulls out the whole record and prints it. The record is a tuple, so it prints with its parentheses. The second line unpacks the record into its three parts.
   - Read the closing comment. The records are tuples on purpose: intel entries are evidence, and evidence should not be editable in place.
3. **Modify.** Part 2 shows the pattern for a dictionary item assignment and gives you one confirmed new record.
   - The new record: indicator `198.51.100.23`, threat name `Qakbot loader`, confidence `High`, status `Active`.
   - Add it to `INTEL` with one line of code.
   - Run the program again. Nothing new prints yet. The new entry appears at the end of the full table once Part 3 works.
4. **Create.** Part 3 has no code yet, only pseudocode. Follow it line by line to build these pieces, in this order:
   1. A function `lookup_ioc(intel, indicator)` that looks the indicator up and returns its details.
   2. A function `print_intel(intel)` that prints the whole table, one line per indicator. Loop with `.items()` and unpack each tuple into its three parts.
   3. A prompt that asks the user for an indicator.
   4. A `try`/`except` around the lookup. A hit prints the match line. A `KeyError` prints a message that says the indicator is **not in intel: treat it as unknown, not as safe**. You may word it differently, but the message must say both things.
   5. A closing call to `print_intel`, so every run ends with the full table, including your new entry from Part 2.
5. Run the program twice: once with an indicator from the table, and once with one that is not in it. Check both runs against the expected output below.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain why a lookup miss is treated as unknown, not as safe.

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

Your wording and column spacing may differ. Every run must still have these pieces: the Part 1 lines, the lookup result or the miss message, and the full table ending with your new entry. This is a run with an indicator that is in the table. The indicator you type appears after the prompt on your screen.

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

A run with an indicator that is not in the table, for example `10.9.9.9`, prints your unknown-not-safe message in place of the `Match:` line. With the wording from the pseudocode, that line is `No record of 10.9.9.9 in intel -- treat it as UNKNOWN, not as safe.` The same table follows.

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
