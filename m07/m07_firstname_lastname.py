'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M07 Assignment - Threat-Intel Lookup
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain why a lookup miss is treated as unknown, not as safe.]
'''

# ---- Part 1: READ -----------------------------------------------------
# The intel table is given: each key is an indicator (an IP address or a
# file hash), and each value is a TUPLE of (threat_name, confidence, status).
INTEL = {
    "203.0.113.44": ("Emotet C2", "High", "Active"),
    "198.51.100.7": ("Cobalt Strike beacon", "High", "Active"),
    "192.0.2.126": ("Cryptomining pool", "Medium", "Contained"),
    "d41d8cd98f00": ("AgentTesla dropper", "High", "Active"),
    "9e107d9d372b": ("Mirai variant", "Low", "Retired"),
    "e99a18c428cb": ("Phishing kit payload", "Medium", "Active"),
    "203.0.113.99": ("TOR exit scanner", "Low", "Retired"),
}

# The two lines below are already complete. Run the program and look at
# the output. Square brackets with a key pull that key's value out of
# the dictionary. The whole record prints, parentheses and all, because
# the record is a tuple.
record = INTEL["d41d8cd98f00"]
print("d41d8cd98f00 ->", record)

# Tuple unpacking: one assignment splits the record into its three parts.
threat, confidence, status = record
print("Threat:", threat, "| Confidence:", confidence, "| Status:", status)

# One thing to notice (no code needed). The records are tuples on purpose:
# intel entries are evidence, and evidence should not be editable in place.
# If you tried  record[0] = "something else"  Python would stop you with a
# TypeError. That is why the values above sit in parentheses, not brackets.

# ---- Part 2: MODIFY ---------------------------------------------------
# The team has just confirmed a new indicator, and it belongs in the table.
# Adding an entry is one dictionary item assignment: the same square
# brackets as a lookup, but on the left side of an equals sign:
#
#     INTEL["<indicator>"] = ("<threat_name>", "<confidence>", "<status>")
#
# The new record: indicator 198.51.100.23, threat name Qakbot loader,
# confidence High, status Active. Run the program again. Nothing new
# prints yet, but once Part 3 works this entry appears at the end of the
# full table.
# TODO: write your one line of code below this comment

# ---- Part 3: CREATE ---------------------------------------------------
# Build the lookup tool: two functions, a prompt, and a try/except that
# turns a lookup miss into a warning instead of a crash.
#
# Pseudocode:
#   DEFINE lookup_ioc with parameters intel and indicator
#       RETURN intel[indicator]
#
#   DEFINE print_intel with parameter intel
#       PRINT a blank line, then the line: --- Full Threat-Intel Table ---
#       LOOP over intel.items(), unpacking each pair into indicator and record
#           UNPACK record into threat, confidence, status
#           PRINT indicator, threat, confidence, status on one line,
#               separated by " | "
#
#   PRINT a blank line, then the banner: === Harborwatch Threat-Intel Lookup ===
#   ASK the user for an indicator, with the prompt: Enter an indicator (IP or hash):
#   PRINT a blank line
#   TRY
#       CALL lookup_ioc with INTEL and the indicator,
#           and UNPACK the result into threat, confidence, status
#       PRINT the match line: Match: <indicator> | Threat: <threat> |
#           Confidence: <confidence> | Status: <status>
#   EXCEPT KeyError
#       PRINT: No record of <indicator> in intel -- treat it as UNKNOWN, not as safe.
#   CALL print_intel with INTEL
#
# TODO: write your code below this comment
