# M05 Assignment - Triage Queue

## What you are doing, and why

You will sort a list of alert severity scores with a **bubble sort you write yourself**. A bubble sort uses nested loops: it compares neighbors and swaps them when they are out of order. Python can sort a list for you, and after this module you will use that. For this assignment, step 4 names the built-in functions you may not use. You will also grow a list with `append()`, scan it with a loop to find its highest and lowest values, and walk it backward.

## Scenario

Harborwatch's alert feed added severity scores (CVSS-style, 0.0 to 10.0) to the queue overnight, and two more came in by phone this morning. The morning threat hunter works the queue **worst-first**, so a score of 9.8 is handled before a score of 2.1 that arrived earlier. Your lead wants a small triage tool that takes the overnight scores, adds this morning's, sorts them, and prints the queue in the order the hunter works it.

## What you are given

- [Starter file](m05_firstname_lastname.py). A header docstring to complete and three parts: working code to read (the overnight scores, pre-loaded and printed by a loop), working code to modify (an `append()` for the morning's phoned-in scores), and pseudocode to turn into your own code (the bubble sort and the triage report).

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m05_jane_doe.py` for Jane Doe. Keep the `m05_` prefix.
2. **Read.** Part 1 is already complete. The overnight severity scores are pre-loaded as a list, and a loop prints each one. Run the program and watch the loop walk the list, one score per line.
3. **Modify.** Part 2 appends one phoned-in score, but the value is wrong. Change `0.5` to `4.7`. Then add one more `append()` line for the second phoned-in score, `6.9`. Run again. The output does not change yet, because `append()` prints nothing. The list now holds two more scores.
4. **Create.** Part 3 has no code yet, only pseudocode, in five steps. Turn each step into Python, line by line, in order. Do not use `sorted()`, `.sort()`, `max()`, or `min()` anywhere in Part 3. Writing the loops yourself is the requirement.
   - Print the list **before** sorting.
   - Find the highest and the lowest score by scanning the list with a loop.
   - Sort the list **ascending** with a hand-written **bubble sort**. Use an outer loop for the passes and an inner loop that compares each pair of neighbors. Swap the pair when the left one is bigger.
   - Print the list **after** sorting.
   - Print the triage order **worst-first**. Walk the sorted list in reverse and print one score per line with its priority number.
5. Run the program one last time and check that every line matches the expected output below, in order.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain how bubble sort decides when to swap two neighbors.

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

The scores come from the starter and your Part 2 change, so the program prints the same report on every run. Your output must match this exactly, line for line.

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

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
