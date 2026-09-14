# M04 Assignment - Brute-Force Alarm

## What you are doing, and why

You will write a monitoring program that watches a stream of login results and sounds the alarm when it sees a brute-force pattern. This is the week the course's two loop forms meet real state: a `while` loop that runs until a sentinel value ends the stream, a `for` loop with `range()` for a fixed count, and booleans with `if/elif/else` deciding what each new piece of input means for the counters you are tracking. The consecutive-failure counter at the heart of this program (reset on success, increment on failure, act at a threshold) is the same pattern behind account lockouts, rate limiters, and intrusion detection everywhere.

## Scenario

A **Harborwatch Security** client's VPN gateway is being hammered: someone is guessing passwords against it, mixed in with legitimate logins. Real detection systems read the gateway's log feed; until the pipeline team wires that up, your lead wants a working monitor she can drive by hand: an analyst reads login results off the gateway console and types them into your program one at a time. Three failed logins in a row is the shop's brute-force signature. Your monitor tracks the streak, raises an alert the moment the signature appears, keeps watching, and reports session totals when the analyst signs off.

## What you are given

- [Starter file](m04_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.

If you have not set up Thonny yet, do that first: Course Materials, Software & Technology page in Canvas.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m04_jane_doe.py` for Jane Doe. Keep the `m04_` prefix.
2. **Read.** Part 1 is already complete: a `for` loop with `range(3, 0, -1)` counts down the three arming lines, then a separator banner and the analyst's instructions print once. Run the program and watch the countdown; until you build Part 3, the program ends right after.
3. **Modify.** Part 2 sets `THRESHOLD`, the number of consecutive failures that fires the alarm. But it is set to 5, and the shop's brute-force signature is 3 in a row. Change it to 3. Nothing visible changes yet; once your monitor is running, this constant decides when the ALERT fires.
4. **Create.** Part 3 has no code yet: only pseudocode, one line of code per line. Follow it to build the monitor:
   - Create the tracking variables: total attempts, total failures, and the current failure streak (all starting at 0), plus an alarm boolean starting at `False`.
   - Write a `while` loop that reads one result per line with `input()`. The word `done` is the sentinel: when it arrives, leave the loop with `break` and go print the summary.
   - If the result is `ok`: count the attempt, reset the streak to 0, and print the status line: `Attempt 1: ok (failure streak: 0)`.
   - If the result is `fail`: count the attempt and the failure, add 1 to the streak, and print the status line: `Attempt 2: FAIL (failure streak: 1)`. When the streak reaches exactly `THRESHOLD`, print `ALERT: 3 consecutive failed logins - possible brute-force attack!` and set the alarm boolean to `True`. Do not stop; the monitor keeps watching until the sentinel.
   - Anything that is not `ok`, `fail`, or `done` is a typo: print `Unrecognized result - ignoring.` and use `continue` to skip back to the next read without counting an attempt.
   - After the loop, print the session summary: a `--- Session summary ---` line, then total attempts and failed attempts, then the alarm boolean reported meaningfully with `if/else`: `Alarm fired: YES - report this session to your lead.` when it fired, `Alarm fired: no - traffic looks normal.` when it did not.
5. Test with the attempt sequence under Expected output, then try your own: a session with no alarm, and a session where the streak passes 3 and keeps going.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. Every program you submit in this course carries this header; professionals sign their work, and so do you.

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

This run uses the attempt sequence `ok fail fail ok fail fail fail retry ok done`, one word per line. With that sequence, your output must match this transcript exactly: same lines, same order, same counts (your typed entries appear between the lines when you run it live). With a different sequence the counts and streaks will differ, but the line formats, the ALERT trigger at three consecutive failures, and the summary block must not.

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

Before you upload, confirm three things: the file is renamed with your own name, it runs in Thonny without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
