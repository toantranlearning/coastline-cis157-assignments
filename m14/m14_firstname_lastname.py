'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M14 Assignment - Server-Log Hunt
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain why a generator with yield can handle a log file
too large to fit in memory.]
'''

# ---- Part 1: READ -----------------------------------------------------
# This part is already complete. It opens server.log with a `with`
# statement, reads it LINE BY LINE (`for line in log_file`, never
# read() or readlines()), and counts the lines. Line-by-line reading
# holds one line in memory at a time, so this exact loop works on a
# million-line log. Run the program and check the count in the output.
line_count = 0
with open("server.log", "r") as log_file:
    for line in log_file:
        line_count = line_count + 1
print("Lines in log:", line_count)

# ---- Part 2: MODIFY ---------------------------------------------------
# The demo below counts every line containing PATTERN. Right now it
# hunts for "ERROR". Change PATTERN to "WARNING", run again, and watch
# the count change: one constant decides what this loop counts.
PATTERN = "ERROR"
pattern_count = 0
with open("server.log", "r") as log_file:
    for line in log_file:
        if PATTERN in line:
            pattern_count = pattern_count + 1
print("Lines containing " + PATTERN + ":", pattern_count)

# ---- Part 3: CREATE ---------------------------------------------------
# The hunt. Six steps, spelled out below. Follow the pseudocode line
# by line. It scans the whole log, pulls out every ERROR line (through
# a generator) and every WARNING line (in the reading loop), writes
# them to findings.txt, and prints the summary.
#
# Pseudocode:
#
#   Step 1. The generator (define it first, above the code that uses it):
#     DEFINE a generator function error_lines taking path
#         OPEN path WITH a with statement, as log_file
#             LOOP over each line in log_file
#                 IF "ERROR" IN line
#                     YIELD line
#
#   Step 2. Scan the log (start a TRY block; steps 2-6 live inside it):
#     TRY
#         SET total_lines to 0
#         SET warning_list to an empty list
#         OPEN "server.log" WITH a with statement, as log_file
#             LOOP over each line in log_file
#                 ADD 1 to total_lines
#                 IF "WARNING" IN line
#                     APPEND line to warning_list
#
#   Step 3. Consume the generator:
#         SET error_list to an empty list
#         LOOP over each line in error_lines("server.log")
#             APPEND line to error_list
#
#   Step 4. Write the report (careful: "w" truncates the file the
#             moment it opens, so write to findings.txt and nothing else):
#         OPEN "findings.txt" WITH a with statement, mode "w", as report
#             WRITE the header line "=== Findings report: server.log ==="
#                 followed by a newline
#             LOOP over each line in error_list
#                 WRITE line to report
#             LOOP over each line in warning_list
#                 WRITE line to report
#
#   Step 5. The summary (still inside the TRY block):
#         PRINT "Lines scanned:" and total_lines
#         PRINT "ERROR findings:" and the length of error_list
#         PRINT "WARNING findings:" and the length of warning_list
#         PRINT "Total findings:" and the two lengths added together
#         PRINT "Findings report written to findings.txt"
#
#   Step 6. The safety net:
#     EXCEPT FileNotFoundError
#         PRINT a friendly message: say server.log is missing and that
#             it must be downloaded into the same folder as this program
#
# TODO: write your code below this comment
