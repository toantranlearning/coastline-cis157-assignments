# M12 Assignment - Sign-In Sentinel

## What you are doing, and why

You will build a class from scratch (class variables, a constructor, instance variables, and instance methods) and use it to catch a real attack pattern. Everything this module taught about the difference between what belongs to the class and what belongs to each object shows up here in working code: every sign-in is its own object with its own data, while the running totals live on the class and are shared by all of them. Keeping those two straight is the heart of this assignment, and it is exactly what the module quiz tests.

## Scenario

A Harborwatch client just called: one of their accounts signed in from Los Angeles, and ninety minutes later signed in again from Singapore. No airplane does that. Either the account is shared, or, far more likely, the credentials are stolen and being used from two places at once. The detection that catches this is called **impossible travel**: compute the speed a body would need to cover the distance between two sign-in locations in the time between them, and if it is faster than any airliner, raise an alert. Your lead wants a working prototype, and this is your first tool built with a class of your own.

## What you are given

- [Starter file](m12_firstname_lastname.py). A header docstring to complete and three parts: working code to read (a `CITY_COORDS` dictionary and a finished `distance_km()` helper), working code to modify (the alert threshold), and pseudocode to turn into the class and detection you write yourself.

If you have not set up Thonny yet, do that first: Course Materials, Software & Technology page in Canvas.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m12_jane_doe.py` for Jane Doe. Keep the `m12_` prefix.
2. **Read.** Part 1 is already complete: `CITY_COORDS` maps city names to `(latitude, longitude)` tuples, `distance_km(coord_a, coord_b)` returns the approximate distance in kilometers between two of those tuples (a flat-plane shortcut, not the haversine formula real systems use, but fine for this exercise), and one finished call prints the Los Angeles-to-Singapore distance. Run the program and look at that number: it is the trip the compromised account claims to have made in one hour. You call these in Part 3. You do not modify them.
3. **Modify.** Part 2 sets the alert threshold, `SPEED_LIMIT_KMH = 900`, and prints it. Your lead wants the detection tuned tighter: change `900` to `800`, run again, and confirm the threshold line changes.
4. **Create.** Part 3 has no code yet, only pseudocode. Follow it line by line to build a class `SignInEvent` with two **class variables** (`total_signins` and `flagged_count`, shared counters that live on the class, not on any one object), a constructor `__init__(self, username, city, hour)` that stores the parameters and the looked-up coordinates as instance variables and increments `SignInEvent.total_signins`, an instance method `summary(self)` that returns one f-string line, and an instance method `is_impossible_travel(self, other)` that computes distance and hour difference, guards a zero-hour difference with a conditional (an `if`, not exceptions), and returns `True`, incrementing `SignInEvent.flagged_count` first, when the implied speed exceeds `SPEED_LIMIT_KMH`.
5. The pseudocode then walks you through the detection run: create **four** events for **two users** (one user's pair is impossible travel, the other's is not), collect them in a list and loop over that list to print each event's `summary()` line, check one pair per user with `is_impossible_travel()` and print the `IMPOSSIBLE TRAVEL` alert when a pair is flagged, and finish by printing the fleet statistics **from the class**: `SignInEvent.total_signins` and `SignInEvent.flagged_count`, not from any individual object. That last distinction is the one the module quiz tests: the counts belong to all events collectively, so you ask the class, not an instance.
6. Run the program one last time, check your output against the expected output below, and complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot.

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

Your usernames, cities, and hours may differ, and your speeds will differ with them; the first two lines, the sections, the line shapes, and the alert must not. Whatever data you choose, exactly one user's pair must fire the alert, and the fleet stats must match your four events.

```text
Los Angeles to Singapore: 24914 km
Alert threshold: 800 km/h

=== Harborwatch Sign-In Sentinel ===

Sign-in log:
mchen signed in from Los Angeles at hour 8
mchen signed in from Singapore at hour 9
dokafor signed in from New York at hour 7
dokafor signed in from London at hour 19

Travel check:
IMPOSSIBLE TRAVEL: mchen -- Los Angeles (hour 8) -> Singapore (hour 9) implies 24914 km/h

Fleet stats (from the class):
Total sign-ins: 4
Flagged events: 1
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs in Thonny without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
