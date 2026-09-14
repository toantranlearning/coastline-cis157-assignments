'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M11 Assignment - Dirty-Log Field Extractor
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain why catching ValueError specifically is better here
than a bare except.]
'''

# The client's gateway log export: one record per string, fields separated
# by "|" in the shape  hour|username|source_ip|status.
# The dirt is deliberate. Do not edit this list.
records = [
    "14|jdoe|203.0.113.44|fail",
    "02|asmith|198.51.100.23|ok",
    " 14 | jdoe | 203.0.113.44 | fail ",
    "15|jdoe|203.0.113.44|ok",
    "xx|npatel|192.0.2.150|ok",
    "03|asmith|198.51.100.23|fail",
    "",
    "22|mallory|203.0.113.99",
    "23|jdoe|203.0.113.44|fail",
    "04|asmith|192.0.2.150|ok",
]

# ---- Part 1: READ -----------------------------------------------------
# The code below is already complete. It takes ONE clean record from the
# list, splits it on "|", and prints each field. Run the program and match
# each printed field back to the record it came from. This is the whole
# parsing move. Part 3 just repeats it in a loop, on records that fight
# back.
sample = records[0]
fields = sample.split("|")
print("record:", sample)
print("hour:", fields[0])
print("user:", fields[1])
print("ip:", fields[2])
print("status:", fields[3])

# ---- Part 2: MODIFY ---------------------------------------------------
# The line below cleans a record with .strip(), but it cleans records[0],
# which was never dirty, so nothing visibly changes. Change records[0] to
# records[2], the whitespace-padded record, and run again. Notice what
# .strip() removed (the outer spaces) and what it did not (the spaces
# around the inner fields). That is why Part 3 strips every field, not
# just the record.
print("cleaned:", records[0].strip())

# ---- Part 3: CREATE ---------------------------------------------------
# The parser. Follow the pseudocode line by line; the indentation shows
# which lines belong inside the loop, the ifs, and the try.
#
# Pseudocode:
#   CREATE an empty list called errors
#   SET parsed_count to 0 and fail_count to 0
#
#   LOOP over each record in records:
#       STRIP the record
#       IF the stripped record is empty:
#           CONTINUE            (a blank line is nothing, not an error)
#
#       SPLIT the record on "|" into fields
#       IF the number of fields is not 4:
#           ADD the record plus the reason "wrong field count" to errors
#           CONTINUE
#
#       STRIP each of the four fields and name them:
#           hour, username, ip, status
#
#       TRY:
#           CONVERT the hour field to a number with int()
#       EXCEPT ValueError:
#           ADD the record plus the reason "hour is not a number" to errors
#       ELSE:
#           PRINT "parsed:" followed by the four fields
#           ADD 1 to parsed_count
#           IF status is "fail": ADD 1 to fail_count
#
#   AFTER the loop:
#       PRINT a blank line, then the header  === Hunt summary ===
#       PRINT "Records parsed:" and parsed_count
#       PRINT "Records rejected:" and the number of entries in errors
#       LOOP over errors: PRINT each entry, indented two spaces
#       PRINT "Failed logins:" and fail_count
#
# TODO: write your code below this comment
