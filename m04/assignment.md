# M04 Assignment - Brute-Force Alarm

## What you are doing, and why

You will write a program that reads login results one at a time and prints an alert when it sees three failed logins in a row. It practices both loops from this module: a `for` loop with `range()` for a fixed count, and a `while` loop that runs until a sentinel value ends the input. Inside the `while` loop, booleans and `if/elif/else` decide what each result does to the counters you are tracking. The main counter is the failure streak: add 1 on a failure, reset it to 0 on a success, and act when it reaches a threshold.

## Scenario

Someone is guessing passwords against the VPN gateway of a **Harborwatch Security** client, and the guesses are mixed in with legitimate logins. The gateway's log feed is not connected to a detection system yet, so your lead wants a monitor that can be run by hand: an analyst reads login results off the gateway console and types them into your program one at a time. Three failed logins in a row is the shop's brute-force signature. Your monitor tracks the streak, prints an alert as soon as the signature appears, keeps watching, and reports session totals when the analyst signs off.

## What you are given

- [Starter file](m04_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m04_jane_doe.py` for Jane Doe. Keep the `m04_` prefix.
2. **Read.** Part 1 is already complete. Run the program and watch the countdown.
   - A `for` loop with `range(3, 0, -1)` counts down the three arming lines.
   - After the countdown, a separator banner and the analyst's instructions print once.
   - Until you build Part 3, the program ends right after that.
3. **Modify.** Part 2 sets `THRESHOLD`, the number of failures in a row that fires the alarm. It is set to 5, but the shop's brute-force signature is 3 in a row. Change it to 3. You will not see a difference yet. Once your monitor runs, this constant decides when the ALERT fires.
4. **Create.** Part 3 has no code yet, only pseudocode. Each line of pseudocode becomes one line of code. Follow it to build the monitor.
   - Create the tracking variables: total attempts, total failures, and the current failure streak, all starting at 0. Add an alarm boolean that starts at `False`.
   - Write a `while` loop that reads one result per line with `input()`.
   - The word `done` is the sentinel. When it arrives, leave the loop with `break` and go print the summary.
   - If the result is `ok`: count the attempt, reset the streak to 0, and print the status line in this format: `Attempt 1: ok (failure streak: 0)`.
   - If the result is `fail`: count the attempt and the failure, add 1 to the streak, and print the status line in this format: `Attempt 2: FAIL (failure streak: 1)`.
   - Also for `fail`: when the streak reaches exactly `THRESHOLD`, print `ALERT: 3 consecutive failed logins - possible brute-force attack!` and set the alarm boolean to `True`. Do not stop the loop. The monitor keeps watching until the sentinel.
   - Anything that is not `ok`, `fail`, or `done` is a typo. Print `Unrecognized result - ignoring.` and use `continue` to go back to the next read without counting an attempt.
   - After the loop, print the session summary: a `--- Session summary ---` line, then total attempts, then failed attempts.
   - End the summary by reporting the alarm boolean in words, using `if/else`. Print `Alarm fired: YES - report this session to your lead.` if it fired, or `Alarm fired: no - traffic looks normal.` if it did not.
5. Test with the attempt sequence under Expected output. Then try two sequences of your own: a session with no alarm, and a session where the streak passes 3 and keeps going.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain why a while loop, not a for loop, fits the monitoring stage of this program.

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

This run uses the attempt sequence `ok fail fail ok fail fail fail retry ok done`, typed one word per line. With that sequence, your output must match this transcript exactly: same lines, same order, same counts. When you run it live, the words you type appear between the output lines. With a different sequence, the counts and streaks will differ. The line formats, the ALERT at three consecutive failures, and the summary block must stay the same.

```text
Arming brute-force monitor in 3...
Arming brute-force monitor in 2...
Arming brute-force monitor in 1...
========================================
Monitoring gateway logins. Enter one result per line (ok, fail, or done).
Attempt 1: ok (failure streak: 0)
Attempt 2: FAIL (failure streak: 1)
Attempt 3: FAIL (failure streak: 2)
Attempt 4: ok (failure streak: 0)
Attempt 5: FAIL (failure streak: 1)
Attempt 6: FAIL (failure streak: 2)
Attempt 7: FAIL (failure streak: 3)
ALERT: 3 consecutive failed logins - possible brute-force attack!
Unrecognized result - ignoring.
Attempt 8: ok (failure streak: 0)
--- Session summary ---
Total attempts: 8
Failed attempts: 5
Alarm fired: YES - report this session to your lead.
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
