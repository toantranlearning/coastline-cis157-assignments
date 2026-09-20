'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M13 Assignment - Platform Access Control
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain why request_tool() raises AccessDeniedError instead
of just printing an error message.]
'''

# ---- Part 1: READ -----------------------------------------------------
# Everything in this part is already complete. Run the program and read
# the output before you change anything. The custom exception and the
# parent class below are the foundation the whole assignment builds on.

class AccessDeniedError(Exception):
    """Raised when a user requests a tool their role does not grant."""
    pass


class PlatformUser:
    """A Harborwatch platform account. Every role starts from this class."""

    user_count = 0  # class variable: shared by every user, counts them all

    def __init__(self, username, role):
        self.username = username
        self.role = role
        PlatformUser.user_count += 1

    def __str__(self):
        return f"{self.username} ({self.role})"

    def login(self):
        print(f"{self.username} logged in to the Harborwatch platform.")

    def get_permissions(self):
        return ["view_dashboard"]

    def request_tool(self, tool_name):
        if tool_name in self.get_permissions():
            return f"Access approved: {self.username} may use {tool_name}."
        raise AccessDeniedError(
            f"Access denied: {self.username} cannot use {tool_name}."
        )


# One demo user, exercised so you can watch the class work.
print("=== Part 1: One Platform User ===")
guest = PlatformUser("Avery", "Contractor")
print(guest)                                 # __str__ does the formatting
guest.login()
print("Permissions:", guest.get_permissions())
print(guest.request_tool("view_dashboard"))  # allowed: returns a message

# The line below asks for a tool Avery does NOT have. Remove the # at the
# start of the print line, run once, and read the traceback in the output:
# the program stops with AccessDeniedError, carrying the message built in
# request_tool(). That crash-with-a-name is what "raise" does. Then put
# the # back so the rest of the program can run.
# print(guest.request_tool("manage_users"))

# ---- Part 2: MODIFY ---------------------------------------------------
# An account with no role of its own should see the alert feed as well as
# the dashboard. (The three role classes you write in Part 3 override
# get_permissions() with their own lists, so this change does not reach them.)
# In get_permissions() above, change the default list
#     ["view_dashboard"]
# to
#     ["view_dashboard", "view_alerts"]
# then run again and compare Avery's permission line with what it printed
# before. Nothing to write in this section - the change happens in Part 1.

# ---- Part 3: CREATE ---------------------------------------------------
# Now build the three roles and prove the access control works.

# 3a. Define the AdminUser child class.
#
# Pseudocode:
#   DEFINE CLASS AdminUser INHERITING FROM PlatformUser
#       DEFINE __init__ taking username
#           CALL super().__init__ with username and "Admin"
#       OVERRIDE get_permissions
#           RETURN ["view_dashboard", "run_scan", "close_ticket",
#                   "export_report", "manage_users"]
# TODO: your code here

# 3b. Define the SeniorAnalyst child class.
#
# Pseudocode:
#   DEFINE CLASS SeniorAnalyst INHERITING FROM PlatformUser
#       DEFINE __init__ taking username
#           CALL super().__init__ with username and "Senior Analyst"
#       OVERRIDE get_permissions
#           RETURN ["view_dashboard", "run_scan", "close_ticket",
#                   "export_report"]
# TODO: your code here

# 3c. Define the JuniorAnalyst child class.
#
# Pseudocode:
#   DEFINE CLASS JuniorAnalyst INHERITING FROM PlatformUser
#       DEFINE __init__ taking username
#           CALL super().__init__ with username and "Junior Analyst"
#       OVERRIDE get_permissions
#           RETURN ["view_dashboard", "run_scan"]
# TODO: your code here

# 3d. Create one object of each child class and introduce it.
#
# Pseudocode:
#   PRINT a blank line, then the header: === Part 3: Platform Users ===
#   CREATE admin AS AdminUser with username "Morgan"
#   CREATE senior AS SeniorAnalyst with username "Dana"
#   CREATE junior AS JuniorAnalyst with username "Riley"
#   FOR EACH user IN [admin, senior, junior]
#       PRINT the user itself (your __str__ does the work)
#       CALL the user's login() method
#       PRINT "Permissions:" and the result of the user's get_permissions()
# TODO: your code here

# 3e. Prove the inheritance is real - one check each.
#
# Pseudocode:
#   PRINT a blank line, then the header: === Class Checks ===
#   PRINT "Riley is a PlatformUser:" and the result of
#       CALLING isinstance with junior and PlatformUser
#   PRINT "JuniorAnalyst is a subclass of PlatformUser:" and the result of
#       CALLING issubclass with JuniorAnalyst and PlatformUser
# TODO: your code here

# 3f. The escalation test, then the head count. This step has no
#     pseudocode: the design is yours. Write your own pseudocode as
#     comments first (UPPERCASE verbs, one line per line of code, the
#     style used in 3a through 3e), then translate it into Python.
#     Your pseudocode stays in the file and is part of what you submit.
#
#     What the code must do: print a blank line and the header
#     === Privilege Escalation Test ===
#     then, in a full try/except/else/finally structure: TRY printing
#     the result of junior.request_tool("run_scan") (allowed) and then
#     junior.request_tool("manage_users") (raises). The except branch
#     catches AccessDeniedError as error and prints the error, then
#     "Exception args:" with error.args. The else branch prints
#     "No escalation attempts detected." (it stays silent here, because
#     it only runs when nothing was raised). The finally branch prints
#     "Access control check complete." After the block, print
#     "Total platform users created:" with PlatformUser.user_count,
#     read from the class itself, not from any one object.
#
# YOUR PSEUDOCODE:
# TODO: your code here
