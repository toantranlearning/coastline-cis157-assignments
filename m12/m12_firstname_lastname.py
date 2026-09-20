'''
NAME: First Last
COURSE: CIS C157 - Introduction to Python Programming
ASSIGNMENT: M12 Assignment - Sign-In Sentinel
DATE: YYYY-MM-DD

DESCRIPTION:
[One or two sentences: what this program does.]

REFLECTION:
[2-3 sentences: what you built, the error or unexpected behavior you
hit along the way, why you think it happened, and what fixed it.
Also briefly explain the difference between a class variable and an
instance variable, and why the fleet stats are read from the class.]
'''

import math

# ---- Part 1: READ -----------------------------------------------------
# Everything in this part is already complete. Run the program and look
# at the first line it prints. That distance, Los Angeles to Singapore,
# is the trip one client account claims to have made in a single hour.
# Keep that number in mind; you will see it again in Part 3.
# You call CITY_COORDS and distance_km() in Part 3. You do not modify them.

# City name -> (latitude, longitude). Do not modify.
CITY_COORDS = {
    "Los Angeles": (34.05, -118.24),
    "New York": (40.71, -74.01),
    "London": (51.51, -0.13),
    "Singapore": (1.35, 103.82),
    "Sydney": (-33.87, 151.21),
    "Tokyo": (35.68, 139.69),
}


# Approximate distance in km between two (lat, lon) tuples. This is a
# flat-plane approximation (~111 km per degree). Real systems use the
# haversine formula; this approximation is fine for this exercise.
def distance_km(coord_a, coord_b):
    lat_delta = coord_a[0] - coord_b[0]
    lon_delta = coord_a[1] - coord_b[1]
    return math.sqrt(lat_delta ** 2 + lon_delta ** 2) * 111


la_sg = distance_km(CITY_COORDS["Los Angeles"], CITY_COORDS["Singapore"])
print(f"Los Angeles to Singapore: {la_sg:.0f} km")

# ---- Part 2: MODIFY ---------------------------------------------------
# The alert threshold below is the speed above which travel is flagged
# as impossible. It is set to 900 km/h, but your lead wants the fleet
# tuned tighter: change 900 to 800, run the program again, and confirm
# the threshold line changes.
SPEED_LIMIT_KMH = 900
print(f"Alert threshold: {SPEED_LIMIT_KMH} km/h")

# ---- Part 3: CREATE ---------------------------------------------------
# Build the SignInEvent class and the detection below. Follow the
# pseudocode line by line; indentation shows what goes inside what.

# 1. The class and its two class variables. These live on the class, not
#    on any one object: they are the shared counters for every event.
#
# Pseudocode:
#   DEFINE CLASS SignInEvent
#       SET class variable total_signins TO 0
#       SET class variable flagged_count TO 0
# TODO: your code here

# 2. The constructor, inside the class.
#
# Pseudocode:
#   DEFINE __init__ WITH PARAMETERS self, username, city, hour
#       SET self.username TO username
#       SET self.city TO city
#       SET self.hour TO hour
#       LOOK UP city IN CITY_COORDS AND SET self.coords TO that tuple
#       ADD 1 TO SignInEvent.total_signins
# TODO: your code here

# 3. The summary method, inside the class.
#
# Pseudocode:
#   DEFINE summary WITH PARAMETER self
#       RETURN the f-string: <username> signed in from <city> at hour <hour>
# TODO: your code here

# 4. The detection method, inside the class. Guard the zero-hour case
#    with an if, not exceptions.
#
# Pseudocode:
#   DEFINE is_impossible_travel WITH PARAMETERS self, other
#       COMPUTE distance AS distance_km(self.coords, other.coords)
#       COMPUTE hours AS other.hour MINUS self.hour
#       IF hours IS 0
#           ADD 1 TO SignInEvent.flagged_count
#           RETURN True
#       COMPUTE speed AS distance DIVIDED BY hours
#       IF speed IS GREATER THAN SPEED_LIMIT_KMH
#           ADD 1 TO SignInEvent.flagged_count
#           RETURN True
#       RETURN False
# TODO: your code here

# 5. Below the class: create the four sign-in events and print the log.
#    (Your usernames, cities, and hours may differ; the mchen pair must
#    stay impossible and the dokafor pair must stay possible.)
#
# Pseudocode:
#   CREATE event_a1 AS SignInEvent("mchen", "Los Angeles", 8)
#   CREATE event_a2 AS SignInEvent("mchen", "Singapore", 9)
#   CREATE event_b1 AS SignInEvent("dokafor", "New York", 7)
#   CREATE event_b2 AS SignInEvent("dokafor", "London", 19)
#   CREATE sign_in_log AS a list holding those four events, in that order
#   PRINT a blank line
#   PRINT: === Harborwatch Sign-In Sentinel ===
#   PRINT a blank line
#   PRINT: Sign-in log:
#   LOOP over each event in sign_in_log
#       PRINT that event's summary()
#   (A list can hold objects the same way it holds numbers. Looping over
#    a list of objects and calling the same method on each one works for
#    a hundred events the same way it works for four.)
# TODO: your code here

# 6. The travel check (one pair per user), then the fleet stats, read
#    from the class, not from any one object.
#
# Pseudocode:
#   PRINT a blank line
#   PRINT: Travel check:
#   IF event_a1.is_impossible_travel(event_a2)
#       COMPUTE hours AS event_a2.hour MINUS event_a1.hour
#       IF hours IS 0 (there is no speed to compute: dividing by 0 is an error)
#           PRINT the alert: IMPOSSIBLE TRAVEL: <username> -- <city> (hour <hour>)
#               -> <city> (hour <hour>) in the same hour
#       ELSE
#           COMPUTE speed AS distance_km(event_a1.coords, event_a2.coords)
#               DIVIDED BY hours
#           PRINT the alert: IMPOSSIBLE TRAVEL: <username> -- <city> (hour <hour>)
#               -> <city> (hour <hour>) implies <speed> km/h
#           (format the speed with :.0f, like the distance in Part 1)
#   IF event_b1.is_impossible_travel(event_b2)
#       DO the same for this pair: the same-hour check, then the same alert
#   PRINT a blank line
#   PRINT: Fleet stats (from the class):
#   PRINT: Total sign-ins: SignInEvent.total_signins
#   PRINT: Flagged events: SignInEvent.flagged_count
# TODO: your code here
