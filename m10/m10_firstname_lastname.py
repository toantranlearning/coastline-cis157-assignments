'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M10 Assignment - Phishing URL Analyzer
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain what the "in" operator does when used with two
strings, as in "login" in url.]
'''

# ---- Part 1: READ -----------------------------------------------------
# The lines below are already complete. Run the program and match each
# printed line to the method call that produced it. Note that .lower()
# returns a NEW lowercase string - strings are immutable, so no method
# ever edits a string in place.
sample = "HTTP://Example.COM/Login"
print("Lowercased:", sample.lower())
print("Dots:", sample.count("."))

# ---- Part 2: MODIFY ---------------------------------------------------
# KEYWORDS is the list of suspicious words Part 3 scans for. Analysts
# just flagged a wave of "account" lures. Add "account" to the end of
# the list, then run again - the printout should show five keywords.
KEYWORDS = ["login", "verify", "update", "secure"]
print("Watching for keywords:", KEYWORDS)

# ---- Part 3: CREATE ---------------------------------------------------
# Build the analyzer by following the pseudocode line by line. A red
# flag ADDs 1 to the score and PRINTs a [+1] reason; a pass PRINTs [OK].
#
# 1. Get the URL and normalize it:
#   PROMPT "Enter a URL to analyze: " and SET raw to the answer
#   SET url to raw with .lower() and .strip() chained
#   PRINT a blank line
#   PRINT "Analyzing:" followed by url
#   PRINT a blank line
# TODO: your code here

# 2. Start the checks:
#   PRINT the header: --- Checks ---
#   SET score to 0
# TODO: your code here

# 3. Length check - very long URLs hide their real destination:
#   IF the length of url (use len) is greater than 75
#       ADD 1 to score
#       PRINT: [+1] Longer than 75 characters - long URLs hide their destination
#   ELSE
#       PRINT: [OK] Length <length> (75 or fewer characters)
# TODO: your code here

# 4. Credential trick - browsers ignore everything before an "@":
#   IF "@" in url
#       ADD 1 to score
#       PRINT: [+1] Contains "@" - browsers ignore everything before it
#   ELSE
#       PRINT: [OK] No "@" in the URL
# TODO: your code here

# 5. Dot count - stacked subdomains bury the real domain:
#   SET dots to url.count(".")
#   IF dots is greater than 3
#       ADD 1 to score
#       PRINT: [+1] Dots: <dots> - subdomains stacked to bury the real domain
#   ELSE
#       PRINT: [OK] Dots: <dots> (3 or fewer)
# TODO: your code here

# 6. Keywords, encryption, and the verdict:
#   FOR each word IN KEYWORDS
#       IF word in url
#           ADD 1 to score
#           PRINT: [+1] Suspicious keyword: "<word>"
#   IF url.startswith("https")
#       PRINT: [OK] Starts with "https"
#   ELSE
#       ADD 1 to score
#       PRINT: [+1] Does not start with "https" - connection is not encrypted
#   PRINT a blank line
#   PRINT the header: --- Verdict ---
#   PRINT "Suspicion score:" followed by score
#   IF score is 4 or more
#       PRINT: [LIKELY PHISHING] Do not click. Escalate this URL to your lead.
#   ELSE IF score is 2 or more
#       PRINT: [SUSPICIOUS] Verify the sender before anyone clicks.
#   ELSE
#       PRINT: [CLEAN] No red flags - close the ticket.
# TODO: your code here

# 7. One last utility: a palindrome check. A palindrome reads the same
#    forwards and backwards, and writing the checker is the classic
#    proof of the slicing skill this module teaches:
#   DEFINE is_palindrome taking text
#       SET clean to text lowercased
#       RETURN whether clean equals clean reversed with slicing [::-1]
#   PRINT a blank line
#   PRINT: Palindrome check "racecar": followed by is_palindrome("racecar")
#   PRINT: Palindrome check "harborwatch": followed by is_palindrome("harborwatch")
# TODO: your code here
