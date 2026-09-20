# M12 Assignment - Sign-In Sentinel

## What you are doing, and why

You will write a class of your own, `SignInEvent`, and use it to check pairs of sign-ins for travel that is too fast to be real. The assignment practices what this module teaches: class variables, a constructor, instance variables, and instance methods. Each sign-in is its own object with its own data. The running totals are class variables, which live on the class and are shared by every object. Keeping those two kinds of variable apart is what this assignment grades, and the module quiz tests it too.

## Scenario

A Harborwatch client reported an account that signed in from Los Angeles and, one hour later, signed in again from Singapore. No airplane covers that distance in that time, so either the account is shared or, more likely, the credentials are stolen and in use from two places. The detection for this is called **impossible travel**: compute the speed needed to cover the distance between two sign-in locations in the time between them, and raise an alert if it is faster than any airliner. Your lead wants a working prototype, and you build it with a class of your own.

## What you are given

- [Starter file](m12_firstname_lastname.py). A header docstring to complete and three parts: working code to read (a `CITY_COORDS` dictionary and a finished `distance_km()` helper), working code to modify (the alert threshold), and pseudocode to turn into the class and detection you write yourself.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m12_jane_doe.py` for Jane Doe. Keep the `m12_` prefix.
2. **Read.** Part 1 is already complete. Run the program first.
   - `CITY_COORDS` is a dictionary that maps city names to `(latitude, longitude)` tuples.
   - `distance_km(coord_a, coord_b)` returns the approximate distance in kilometers between two of those tuples. It uses a flat-plane shortcut. Real systems use the haversine formula, but the shortcut is fine for this exercise.
   - One finished call prints the Los Angeles-to-Singapore distance. Find that number in the output. It is the trip the compromised account claims to have made in one hour.
   - You call `CITY_COORDS` and `distance_km()` in Part 3. Do not modify them.
3. **Modify.** Part 2 sets the alert threshold, `SPEED_LIMIT_KMH = 900`, and prints it. Your lead wants a tighter threshold. Change `900` to `800`, run again, and confirm the threshold line changes.
4. **Create.** Part 3 has no code yet, only pseudocode. Follow it line by line to build a class named `SignInEvent`.
   - Give the class two **class variables**, `total_signins` and `flagged_count`. They are shared counters that live on the class, not on any one object.
   - Write the constructor `__init__(self, username, city, hour)`. It stores the parameters and the looked-up coordinates as **instance variables**, so each object keeps its own copy. It also increments `SignInEvent.total_signins`.
   - Read and change a class variable through the class name, as in `SignInEvent.total_signins`. If you assign to `self.total_signins` instead, Python creates a new instance variable on that one object and the shared counter does not change.
   - Write the instance method `summary(self)`. It returns one f-string line.
   - Write the instance method `is_impossible_travel(self, other)`. It computes the distance and the hour difference between the two events. Guard a zero-hour difference with a conditional: use an `if`, not exceptions. When the implied speed exceeds `SPEED_LIMIT_KMH`, the method increments `SignInEvent.flagged_count` first and then returns `True`.
5. The pseudocode then walks you through the detection run.
   - Create **four** events for **two users**. One user's pair is impossible travel. The other user's pair is not.
   - Collect the four events in a list. Loop over that list to print each event's `summary()` line.
   - Check one pair per user with `is_impossible_travel()`. Print the `IMPOSSIBLE TRAVEL` alert when a pair is flagged.
   - Before you compute the speed for the alert line, check the hour difference again. If it is 0, print the alert ending `in the same hour` and do not divide. Dividing by 0 raises `ZeroDivisionError`, and you are free to choose sign-in hours that are the same.
   - Finish by printing the fleet statistics **from the class**: `SignInEvent.total_signins` and `SignInEvent.flagged_count`. Do not print them from any individual object. The counts belong to all events together, so you ask the class and not an instance. The module quiz tests this distinction.
6. Run the program one last time and check your output against the expected output below. Then complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain the difference between a class variable and an instance variable, and why the fleet stats are read from the class.

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

Your usernames, cities, and hours may differ, and your speeds will differ with them. The first two lines, the sections, the line shapes, and the alert must stay the same. Whatever data you choose, exactly one user's pair must fire the alert, and the fleet stats must match your four events.

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

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
