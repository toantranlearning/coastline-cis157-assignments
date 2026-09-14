'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M09 Assignment - Package the Huntkit
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain what the __name__ variable is for.]
'''

# ---- Part 3: CREATE ---------------------------------------------------
# This file has no code yet -- only pseudocode. Parts 1 and 2 live in
# huntkit.py; do those first, and keep huntkit.py in the same folder as
# this file. Then work the five steps below in order, turning the
# pseudocode into code.

# 3.1 Import the whole module. When you run this file, huntkit's
#     self-test does NOT print -- importing sets __name__ to "huntkit",
#     not "__main__".
#
# Pseudocode:
#   IMPORT huntkit
# TODO: your code here

# 3.2 Call each of the three functions through the module name and
#     print three lines matching the expected output.
#
# Pseudocode:
#   CALL huntkit.dwell_time WITH 3 AND 17, PRINT as: Dwell time: <result> days
#   CALL huntkit.severity_label WITH 82, PRINT as: Severity 82: <result>
#   CALL huntkit.format_ioc WITH "203.0.113.44" AND "IP address" AND 85,
#       PRINT the result as-is
# TODO: your code here

# 3.3 Import one name directly, then call it bare -- no module name in
#     front.
#
# Pseudocode:
#   FROM huntkit IMPORT format_ioc
#   CALL format_ioc WITH "44d88612fea8a8f36de82e1278abb02f" AND "file hash"
#       AND 60, PRINT the result
# TODO: your code here

# 3.4 List every name the module contains. Your three functions appear
#     alongside Python's double-underscore names, __name__ among them.
#
# Pseudocode:
#   PRINT dir(huntkit)
# TODO: your code here

# 3.5 Report footer, built on two standard-library modules.
#
# Pseudocode:
#   IMPORT math
#   IMPORT platform
#   SET average TO (82 + 55 + 60) DIVIDED BY 3
#   CALL math.ceil WITH average, PRINT as: Average severity (rounded up): <result>
#   CALL platform.platform, PRINT as: Workstation: <result>
# TODO: your code here
