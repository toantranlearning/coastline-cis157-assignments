# M05 Assignment - Triage Queue

## What you are doing, and why

You will sort a list of alert severity scores with a **bubble sort you write yourself**: nested loops, comparing neighbors, swapping them when they are out of order. Python has `sorted()` and `.sort()`, and after this week you will use them; this week they are prohibited, because the point is to see what sorting *is* before you let the language do it for you. Along the way you will grow a list with `append()`, scan it with a loop to find its extremes, and walk it backward. These are the core list skills this module is about.

## Scenario

Overnight, Harborwatch's alert feed dumped a pile of severity scores (CVSS-style, 0.0 to 10.0) into the queue, and a few more came in by phone this morning. The morning threat hunter does not work the queue in arrival order; they work it **worst-first**, because a 9.8 waiting behind a 2.1 is how breaches happen. Your lead wants a small triage tool: take the overnight scores, add this morning's, put them in order, and print the queue the way a hunter should walk it.

## What you are given

- [Starter file](m05_firstname_lastname.py). A header docstring to complete and three parts: working code to read (the overnight scores, pre-loaded and printed by a loop), working code to modify (an `append()` for the morning's phoned-in scores), and pseudocode to turn into your own code (the bubble sort and the triage report).

If you have not set up Thonny yet, do that first: Course Materials, Software & Technology page in Canvas.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m05_jane_doe.py` for Jane Doe. Keep the `m05_` prefix.
2. **Read.** Part 1 is already complete: the overnight severity scores are pre-loaded as a list, and a loop prints each one. Run the program and watch the loop walk the list, one score per line.
3. **Modify.** Part 2 appends one phoned-in score, but the value is wrong. Change `0.5` to `4.7`, then add one more `append()` line for the second phoned-in score, `6.9`. Run again. The appends print nothing yet, but the list has grown.
4. **Create.** Part 3 has no code yet: only pseudocode, in five steps. Follow each step line by line: print the list **before** sorting; find the highest and lowest score by scanning with a loop (no `max()` or `min()`); sort **ascending** with a hand-written **bubble sort**: an outer loop for the passes, an inner loop that compares each pair of neighbors and swaps them when the left one is bigger, and no `sorted()` or `.sort()`, because writing the swap yourself is the point of this assignment; print the list **after** sorting; then print the triage order **worst-first** by walking the sorted list in reverse, one score per line with its priority number.
5. Run the program one last time and check your output against the expected output below: every line, in order.
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

The scores are fixed by the starter and your Part 2 change, so your output must match this exactly: every line, in order.

```text
Overnight scores in the queue:
7.8
2.1
9.6
5.0
9.8
3.3
6.4
8.2
All severities (unsorted): [7.8, 2.1, 9.6, 5.0, 9.8, 3.3, 6.4, 8.2, 4.7, 6.9]
Highest severity: 9.8
Lowest severity: 2.1
All severities (sorted): [2.1, 3.3, 4.7, 5.0, 6.4, 6.9, 7.8, 8.2, 9.6, 9.8]
Triage order (worst first):
1 - 9.8
2 - 9.6
3 - 8.2
4 - 7.8
5 - 6.9
6 - 6.4
7 - 5.0
8 - 4.7
9 - 3.3
10 - 2.1
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs in Thonny without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
