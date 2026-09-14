'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: Midterm Project - Hunt the Intruder
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain why the case-number trick is not truly random.]
'''

# ---- Part 1: READ -----------------------------------------------------
# The function below is complete and already matches the board format in
# the expected output exactly, including the +---+ grid lines. Read it
# top to bottom, then run the program. The two demo lines under the
# function draw a mid-game sample board so you can see every symbol on
# the grid: "." is an unprobed host, "o" is a host probed and found
# clean, "X" is the intruder found. The finished game calls this
# function as-is -- you will not change it.

def display_board(board):
    print("    0   1   2")
    print("  +---+---+---+")
    for row_number in range(3):
        row = board[row_number]
        print(f"{row_number} | {row[0]} | {row[1]} | {row[2]} |")
        print("  +---+---+---+")

# Demo lines: delete BOTH of these in step 3.1 -- the finished game
# builds its own board and must not print this sample grid.
sample_board = [["o", ".", "."], [".", "o", "."], [".", ".", "X"]]
display_board(sample_board)

# ---- Part 2: MODIFY ---------------------------------------------------
# The banner below is complete, but the probe budget is last year's:
# this year's exercise gives the analyst 4 probes, not 5. Change PROBES
# from 5 to 4, run again, and confirm the banner reports 4 probes.
# Change only the constant -- the banner's f-string and the rest of the
# game read PROBES, so the whole program follows.

PROBES = 5
print("=== HARBORWATCH TABLETOP: HUNT THE INTRUDER ===")
print("An intruder is hiding on one host in the 3x3 network grid.")
print(f"You have {PROBES} probes to find them. Good hunting.")

# ---- Part 3: CREATE ---------------------------------------------------
# The rest of the game is yours, in seven steps. Each step's pseudocode
# is complete -- translate it line by line rather than inventing your
# own structure. Build one step, run the program, and only then move on
# to the next.

# 3.1 Delete the two demo lines at the end of Part 1 (the sample_board
#     line and the display_board(sample_board) call). The function
#     itself stays.

# 3.2 The input-validation function, used for both the row and the
#     column. Invalid input never costs a probe -- the function simply
#     explains the problem and asks again.
#
# Pseudocode:
#   DEFINE a function get_coordinate that takes one parameter, label
#       LOOP forever (while True)
#           SET text to input(f"Enter the {label} to probe (0-2): ")
#           TRY
#               SET number to int(text)
#               IF number is at least 0 AND at most 2
#                   RETURN number
#               ELSE
#                   PRINT f"{number} is off the grid. No probe used -- try again."
#           EXCEPT ValueError
#               PRINT f"{text} is not a number. No probe used -- try again."
# TODO: your code here

# 3.3 The probe-resolution function. This is where the game's booleans
#     live.
#
# Pseudocode:
#   DEFINE a function resolve_probe that takes board, row, column,
#          intruder_row, intruder_column
#       IF row equals intruder_row AND column equals intruder_column
#           SET board[row][column] to "X"
#           RETURN True
#       ELSE
#           SET board[row][column] to "o"
#           RETURN False
# TODO: your code here

# 3.4 The opening: ask for the client case number and derive the
#     intruder's position from it. (The pre-random trick -- see the
#     assignment page for the honest explanation. Retired in M09.)
#
# Pseudocode:
#   PRINT a blank line
#   SET have_number to False
#   LOOP while have_number is False
#       SET text to input("Enter the client case number for this exercise: ")
#       TRY
#           SET case_number to int(text)
#           SET have_number to True
#       EXCEPT ValueError
#           PRINT f"{text} is not a number -- try again."
#   SET position to case_number % 9
#   SET intruder_row to position // 3
#   SET intruder_column to position % 3
# TODO: your code here

# 3.5 The board and the game state.
#
# Pseudocode:
#   SET board to a list of three lists, every host starting as ".":
#       [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
#   SET probes_left to PROBES
#   SET found to False
# TODO: your code here

# 3.6 The main game loop -- one full turn per pass.
#
# Pseudocode:
#   LOOP while probes_left is greater than 0 AND found is False
#       PRINT a blank line
#       CALL display_board(board)
#       SET cleared to board[0].count("o") + board[1].count("o") + board[2].count("o")
#       PRINT f"Probes remaining: {probes_left} | Hosts cleared: {cleared}/9"
#       SET row to get_coordinate("row")
#       SET column to get_coordinate("column")
#       IF board[row][column] is not "."
#           PRINT f"Host ({row}, {column}) was already probed. No probe used -- pick another host."
#       ELSE
#           SET probes_left to probes_left - 1
#           SET found to resolve_probe(board, row, column, intruder_row, intruder_column)
#           IF found is True
#               PRINT f"Contact! The intruder is on host ({row}, {column})."
#           ELSE
#               PRINT f"Host ({row}, {column}) is clean."
# TODO: your code here

# 3.7 The ending.
#
# Pseudocode:
#   PRINT a blank line
#   CALL display_board(board)
#   IF found is True
#       PRINT "You found the intruder. The network is secure -- you win!"
#   ELSE
#       PRINT f"Out of probes. The intruder was hiding on host ({intruder_row}, {intruder_column}). You lose."
# TODO: your code here
