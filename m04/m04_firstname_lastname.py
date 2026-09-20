'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M04 Assignment - Brute-Force Alarm
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain why a while loop, not a for loop, fits the
monitoring stage of this program.]
'''

# ---- Part 1: READ -----------------------------------------------------
# The lines below are already complete. Run the program and watch the
# output. The for loop with range()
# counts 3, 2, 1 (range(3, 0, -1) starts at 3, stops before 0, and
# steps by -1), then a separator banner and the analyst's instructions
# print once. Until you build Part 3, the program ends right after.
for count in range(3, 0, -1):
    print(f"Arming brute-force monitor in {count}...")
print("=" * 40)
print("Monitoring gateway logins. Enter one result per line (ok, fail, or done).")

# ---- Part 2: MODIFY ---------------------------------------------------
# The line below sets the alarm threshold, but it is wrong: the shop's
# brute-force signature is 3 failed logins in a row, not 5. Change 5 to
# 3. Nothing visible changes yet, but once your Part 3 monitor is
# running, this is the number that decides when the ALERT fires.
THRESHOLD = 5

# ---- Part 3: CREATE ---------------------------------------------------
# The monitor: a while loop that reads one result per line until the
# sentinel word "done" arrives, tracking counters as it goes.
#
# Pseudocode (one line of code per line):
#   SET attempts to 0
#   SET failures to 0
#   SET streak to 0
#   SET alarm_fired to False
#   LOOP forever (while True):
#       READ the next result with input()
#       IF the result is "done":
#           STOP the loop (break)
#       IF the result is "ok":
#           ADD 1 to attempts
#           SET streak back to 0
#           PRINT the status line: Attempt <attempts>: ok (failure streak: 0)
#       ELSE IF the result is "fail":
#           ADD 1 to attempts
#           ADD 1 to failures
#           ADD 1 to streak
#           PRINT the status line: Attempt <attempts>: FAIL (failure streak: <streak>)
#           IF streak equals THRESHOLD:
#               PRINT: ALERT: <THRESHOLD> consecutive failed logins - possible brute-force attack!
#               SET alarm_fired to True
#       ELSE (anything else is a typo):
#           PRINT: Unrecognized result - ignoring.
#           SKIP back to the next read (continue)
#   PRINT the line: --- Session summary ---
#   PRINT the line: Total attempts: <attempts>
#   PRINT the line: Failed attempts: <failures>
#   IF alarm_fired is True:
#       PRINT: Alarm fired: YES - report this session to your lead.
#   ELSE:
#       PRINT: Alarm fired: no - traffic looks normal.
#
# TODO: write your code below this comment
