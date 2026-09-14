'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M05 Assignment - Triage Queue
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain how bubble sort decides when to swap two neighbors.]
'''

# ---- Part 1: READ -----------------------------------------------------
# The code below is already complete. The overnight severity scores are
# pre-loaded (CVSS-style, 0.0 to 10.0), and a loop prints each one.
# Run the program and watch the loop walk the list, one score per line.
severities = [7.8, 2.1, 9.6, 5.0, 9.8, 3.3, 6.4, 8.2]

print("Overnight scores in the queue:")
for score in severities:
    print(score)

# ---- Part 2: MODIFY ---------------------------------------------------
# Two more scores came in by phone this morning: 4.7 and 6.9.
# The line below appends a score, but whoever typed it got the value
# wrong. Change 0.5 to 4.7, then add one more append() line right
# below it for the second phoned-in score, 6.9.
severities.append(0.5)

# ---- Part 3: CREATE ---------------------------------------------------
# No code yet -- only pseudocode. Turn each step into Python, in order.
# Do NOT use sorted(), .sort(), max(), or min() anywhere in this part;
# writing the loops yourself is the point of this assignment.

# 3a. Print the full list BEFORE sorting, on one line.
#
# Pseudocode:
#   PRINT the label "All severities (unsorted):" and the list severities
#
# TODO: your code here

# 3b. Find the highest and the lowest score by scanning the list.
#
# Pseudocode:
#   SET highest TO the first score in severities
#   SET lowest TO the first score in severities
#   LOOP over each score in severities
#       IF score > highest THEN
#           SET highest TO score
#       IF score < lowest THEN
#           SET lowest TO score
#   PRINT the label "Highest severity:" and highest
#   PRINT the label "Lowest severity:" and lowest
#
# TODO: your code here

# 3c. Sort the list in ASCENDING order with a hand-written bubble sort.
#     This is the heart of the assignment: an outer loop for the passes,
#     an inner loop that compares each pair of neighbors and swaps them
#     when the left one is bigger.
#
# Pseudocode:
#   SET n TO the length of severities
#   LOOP i FROM 0 UP TO n - 1                 (one pass per score)
#       LOOP j FROM 0 UP TO n - 2             (each pair of neighbors)
#           IF severities[j] > severities[j + 1] THEN
#               SWAP severities[j] AND severities[j + 1]
#                 (in Python:  severities[j], severities[j + 1] =
#                              severities[j + 1], severities[j] )
#
# TODO: your code here

# 3d. Print the full list AFTER sorting, on one line.
#
# Pseudocode:
#   PRINT the label "All severities (sorted):" and the list severities
#
# TODO: your code here

# 3e. Print the triage order WORST-FIRST -- walk the sorted list in
#     reverse, one score per line with its priority number.
#
# Pseudocode:
#   PRINT the heading "Triage order (worst first):"
#   SET priority TO 1
#   LOOP over each score in severities reversed   (the [::-1] slice)
#       PRINT priority, a dash, and the score
#       ADD 1 TO priority
#
# TODO: your code here
