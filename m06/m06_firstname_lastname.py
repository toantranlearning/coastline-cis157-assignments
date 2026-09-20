'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M06 Assignment - Hunt Utilities
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain the difference between print() and return.]
'''

# ---- Part 1: READ -----------------------------------------------------
# The function below is already complete. Run the program and find its
# line in the output. Notice the shape: def names the function and
# its parameters, return hands a value back, and the call below stores
# that value in a variable before printing it.

def dwell_time(start_hour, end_hour):
    hours = end_hour - start_hour
    return hours

elapsed = dwell_time(3, 17)
print(f"Dwell time, Meridian Freight: {elapsed} hours")

# Observe (nothing to change here):
# - dwell_time RETURNS a number; that is why we could store it in elapsed.
# - print() returns nothing. Try these two lines: x = print("hi") and then
#   print(x). You get None, the value a function hands back when it has
#   no return statement.
# - The variable hours exists only while the function runs. Try
#   print(hours) outside the function: the NameError means hours is
#   out of scope out here.
# (The setup page for your editor says how to try one line after a run.)

# A function can also call ITSELF. This one totals the alerts reviewed by
# a tier and every tier beneath it. Run it and read the trace below.

def alerts_through(tier):
    if tier == 0:
        return 0
    return tier + alerts_through(tier - 1)

print(f"Alerts reviewed through tier 3: {alerts_through(3)}")

# Observe (nothing to change here):
# - The if tier == 0 line is the BASE CASE: the one input this function
#   can answer without calling itself again. Without it the calls would
#   never stop and Python would raise RecursionError.
# - Trace it on paper, innermost call first: alerts_through(3) waits on
#   alerts_through(2), which waits on alerts_through(1), which waits on
#   alerts_through(0). That one returns 0, and the answers unwind back
#   up the chain: 1, then 3, then 6.

# ---- Part 2: MODIFY ---------------------------------------------------
# The function below is complete, but its default width is wrong: the
# shop standard banner is 30 characters wide, not 40. Change the default
# value 40 to 30, then run again and watch the first banner shrink.
# The first call below leaves width at its default; the second overrides
# it with a keyword argument. Most calls leave a default alone, and a call
# that needs something different names the parameter it changes.

def alert_banner(text, width=40):
    rule = "=" * width
    return rule + "\n" + text + "\n" + rule

print(alert_banner("HARBORWATCH HUNT UTILITIES"))
print(alert_banner("SHIFT CHANGE", width=20))

# ---- Part 3: CREATE ---------------------------------------------------
# No code yet, only pseudocode. Follow it line by line.

# 1. Define severity_label(score): return the label for a score.
#
# Pseudocode:
#   DEFINE FUNCTION severity_label(score)
#       IF score is below 25
#           SET label to "LOW"
#       ELSE IF score is below 50
#           SET label to "MEDIUM"
#       ELSE IF score is below 75
#           SET label to "HIGH"
#       ELSE
#           SET label to "CRITICAL"
#       RETURN label
#   (return the label; do not print inside the function)
#
# TODO: write your function below this comment

# 2. Define format_ioc(indicator, kind, confidence): return one record
#    string built with an f-string.
#
# Pseudocode:
#   DEFINE FUNCTION format_ioc(indicator, kind, confidence)
#       RETURN an f-string in exactly this shape:
#           [IP] 203.0.113.7 (confidence 85%)
#       (the kind in square brackets, then the indicator, then the
#        confidence in parentheses)
#
# TODO: write your function below this comment

# 3. Main section: call both of your functions and print the results.
#
# Pseudocode:
#   CALL severity_label with score 18 and PRINT: Score 18 is LOW
#   REPEAT for scores 42, 67, and 91
#   CALL format_ioc with ("203.0.113.7", "IP", 85) and PRINT the result
#   CALL format_ioc with ("update-cdn.example.net", "DOMAIN", 60) and
#       PRINT the result
#
# TODO: write your calls below this comment
