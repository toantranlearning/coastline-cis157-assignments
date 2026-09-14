'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M02 Assignment - Dwell-Time Report
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain why the parentheses in the days-and-hours line
change the answer.]
'''

# ---- Part 1: READ -----------------------------------------------------
# print() does more than take one string. It accepts several values at
# once, and two keyword arguments that control the spacing: sep goes
# BETWEEN the values, end goes AFTER the last one. Run the program and
# match each printed line to the call that produced it.
print("Harborwatch", "Security", "dwell-time report")
print("Hours", "Alerts", "Risk", sep=" | ")
print("Report status:", end=" ")
print("DRAFT")

# Observe (nothing to change here):
# - The first call prints three values with no sep given, so Python uses
#   its default, a single space.
# - The second call replaces that default with " | ".
# - The third call ends with a space instead of a new line, which is why
#   DRAFT lands on the same line as "Report status:".

# ---- Part 2: MODIFY ---------------------------------------------------
# Escape sequences put characters into a string that you cannot type
# directly: \n starts a new line, \t jumps to the next tab stop. The
# banner below is followed by a single blank line, because the \n at the
# end of the string adds one and print() adds another. The shop standard
# is TWO blank lines before a report body. Add one more \n to the end of
# the banner string, then run again and count the blank lines.
print("\n=== Harborwatch Security - Dwell-Time Report ===\n")
print("Client:\tMeridian Freight")
print("Analyst:\tJ. Okafor")

# ---- Part 3: CREATE ---------------------------------------------------
# No code yet, only pseudocode. This week's incident is already decided:
# the compromise began at hour 3, it was detected at hour 53, 24 alerts
# were raised, and 18 of them were triaged. You are not asking anyone for
# those numbers; you are writing the arithmetic that turns them into a
# report. Write the numbers straight into your expressions.
#
# Every line below is one print() call. Where a line shows arithmetic,
# put the expression itself inside the print() call and let Python do
# the maths; do not work the answer out yourself and type the result.

# 1. The timeline block.
#
# Pseudocode:
#   PRINT a blank line
#   PRINT: Timeline
#   PRINT "  Began at hour", then 3
#   PRINT "  Detected at hour", then 53
#   PRINT "  Dwell time:", then 53 - 3, then "hours"
#   PRINT "  That is", then (53 - 3) // 24, then "days and",
#       then (53 - 3) % 24, then "hours"
#   (Those parentheses are the point. Without them // and % run BEFORE
#    the subtraction, because they sit higher in the priority table, and
#    the answer comes out wrong. Try it both ways once you have it
#    working, then put the parentheses back.)
# TODO: write your code below this comment

# 2. The alert block.
#
# Pseudocode:
#   PRINT a blank line
#   PRINT: Alerts
#   PRINT "  Raised:", then 24
#   PRINT "  Triaged:", then 18
#   PRINT "  Untriaged:", then 24 - 18
#   PRINT "  Triage rate:", then 18 / 24
#   (Note what / gives you back. Division always produces a float, even
#    when the answer is exact.)
# TODO: write your code below this comment

# 3. The risk block.
#
# Pseudocode:
#   PRINT a blank line
#   PRINT: Risk
#   PRINT "  Score:", then (53 - 3) * 2 + (24 - 18) * 5
#   PRINT "  A beacon doubling hourly for 5 hours reaches", then 2 ** 5
#   PRINT "  Escalation required:", then the Boolean literal True
#       (True and False are literals like 3 and "text" are. Python
#        prints them capitalised, which is how you can tell one from
#        the string "true".)
#   (Multiplication runs before addition, so the score expression would
#    work without its parentheses. Keep them anyway: they say what you
#    meant, and the next person to read the line does not have to
#    remember the priority table.)
# TODO: write your code below this comment

# 4. The footer, printed as one call with a separator between the values.
#
# Pseudocode:
#   PRINT a blank line
#   PRINT "Prepared by", "Harborwatch Security", "Tier 1"
#       with sep set to " / "
# TODO: write your code below this comment
