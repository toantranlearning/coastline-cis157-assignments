'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M15 Assignment - Incident Timeline Builder
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain the difference between %m and %M in a format string.]
'''

import calendar
import os
from datetime import datetime

# Given: the six events recovered by the M14 hunt, in the order they were
# found, NOT the order they happened. Do not edit this list.
EVENTS = [
    ("Lateral movement to file server", "2026-07-16 03:12"),
    ("Initial phishing link clicked", "2026-07-13 09:47"),
    ("Containment - host isolated", "2026-07-18 16:05"),
    ("First C2 beacon observed", "2026-07-13 10:02"),
    ("Data staged for exfiltration", "2026-07-17 22:41"),
    ("Detection - EDR alert triaged", "2026-07-18 14:30"),
]

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M"

# ---- Part 1: READ -----------------------------------------------------
# The lines below are already complete. They take ONE event's timestamp
# string, parse it into a real datetime object with strptime(), and print
# it twice: once raw, once reformatted with strftime(). Run the program
# and compare the two lines: same moment, two different strings.
first_description, first_timestamp = EVENTS[0]
first_moment = datetime.strptime(first_timestamp, TIMESTAMP_FORMAT)
print("Raw timestamp from the list:", first_timestamp)
print("Reformatted with strftime:  ", first_moment.strftime("%b %d, %H:%M"))

# ---- Part 2: MODIFY ---------------------------------------------------
# The line below prints the same moment in the style the timeline will
# use, but the weekday is missing. Change "%b %d, %H:%M" to
# "%a %b %d, %H:%M" and run again: %a adds the short weekday name.
print("Timeline style:", first_moment.strftime("%b %d, %H:%M"))

# ---- Part 3: CREATE ---------------------------------------------------
# The design step is yours this time. Every starter until now handed you
# the pseudocode; from here you write it, which is how the job works.
# For each requirement below, FIRST write your own pseudocode as comments
# (UPPERCASE verbs, one line per line of code, the same style you have
# been translating all course), THEN write the Python beneath it. Your
# pseudocode stays in the file: it is part of what you submit.

# 1. Parse every event. Build a list named timeline holding one
#    (parsed datetime, description) tuple per EVENTS entry, parsing each
#    timestamp with datetime.strptime and TIMESTAMP_FORMAT. Put the
#    datetime FIRST in the tuple.
# YOUR PSEUDOCODE:
# TODO: your code here

# 2. Sort the timeline with plain .sort(). Each tuple starts with its
#    datetime, so no key is needed.
# YOUR PSEUDOCODE:
# TODO: your code here

# 3. Print the timeline. A blank line, then the header
#    === Harborwatch Security - Incident Timeline ===
#    then one line per event: the moment formatted with
#    strftime("%a %b %d, %H:%M"), the description, and either
#    (first event) for the first line or (+<gap> after previous) for the
#    rest, where <gap> is this moment minus the previous one (printing a
#    timedelta directly produces text like 2 days, 17:10:00).
# YOUR PSEUDOCODE:
# TODO: your code here

# 4. Compute and print dwell time. Find the event whose description
#    starts with "Detection"; dwell is that moment minus the earliest
#    moment (timeline[0] after sorting). Print a blank line, then:
#    Dwell time: <dwell> (<hours> whole hours)
#    where <hours> comes from int() on dwell.total_seconds() / 3600.
# YOUR PSEUDOCODE:
# TODO: your code here

# 5. Stamp the report. Capture datetime.now() once, then print a blank
#    line and: Report generated: <stamp formatted with "%Y-%m-%d %H:%M">
# YOUR PSEUDOCODE:
# TODO: your code here

# 6. Print the compromise month. A blank line, then the month grid from
#    calendar.month() for the earliest event's .year and .month, then the
#    caption: Compromise began this month, on <earliest moment formatted
#    with "%a %b %d">.
# YOUR PSEUDOCODE:
# TODO: your code here

# 7. File the report. In order:
#    - Make a folder named case_files with os.mkdir(). If it is already
#      there from an earlier run, carry on: catch FileExistsError.
#    - Write two lines to the file case_files/draft.txt:
#          Incident timeline: <number of events> events
#          the same Dwell time line you printed in step 4
#    - Build the final name: timeline_<earliest moment formatted with
#      "%Y-%m-%d">.txt
#    - If os.listdir("case_files") already holds a file with the final
#      name, delete it with os.remove(), so that os.rename() does the
#      same thing on every computer and on every run.
#    - Rename draft.txt to the final name with os.rename().
#    - Print a blank line, then:
#          Report filed: case_files/<final name>
#          Files in case_files: <the sorted os.listdir of the folder>
# YOUR PSEUDOCODE:
# TODO: your code here
