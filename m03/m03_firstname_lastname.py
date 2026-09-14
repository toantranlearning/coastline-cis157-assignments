'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M03 Assignment - IOC Intake Form
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain what print() does.]
'''

# ---- Part 1: READ -----------------------------------------------------
# The two lines below are already complete. Run the program (green Run
# button, or F5), type your name at the prompt, and watch the f-string
# echo it back. input() always hands you a string; the f-string drops it
# into the middle of another string.
analyst = input("Analyst name: ")
print(f"Intake started by {analyst}")

# ---- Part 2: MODIFY ---------------------------------------------------
# The line below builds the intake banner out of two pieces with string
# concatenation (+), but the last word is wrong. Change "TRIAGE" to
# "INTAKE", then run the program again.
print("=== HARBORWATCH IOC " + "TRIAGE ===")

# ---- Part 3: CREATE ---------------------------------------------------
# Collect the rest of the report and print the standardized record.
# The analyst's name is already in the analyst variable from Part 1.
#
# Pseudocode (one line of code per step):
#   PROMPT "Indicator value (IP or file hash): " and SET the reply in a variable
#   PROMPT "Indicator type: " and SET the reply in a variable
#   PROMPT "Source of report: " and SET the reply in a variable
#   PROMPT "Confidence score (0-100): ", cast the reply with int(), SET it in a variable
#   SET a new variable to the confidence score divided by 100 (85 becomes 0.85)
#   PRINT one multi-line f-string using \n and \t: a blank line, the text
#     [IOC RECORD], then one tab-indented line per value -- Analyst,
#     Indicator, Type, Source, and Confidence as <score>/100 (<fraction>) --
#     matching the layout in the assignment's expected output
#
# TODO: write your code below this comment
