'''
huntkit.py -- Harborwatch Security's shared hunt utilities.

This is a module: a .py file whose functions other programs use by
importing it, not by copy-pasting it. Any script saved in the same
folder gets everything here with one line:

    import huntkit

Parts 1 and 2 of this assignment happen in this file. Part 1 is the
self-test block at the very bottom -- run this file directly and read
what happens. Part 2 is the section marked MODIFY in the middle. Part 3
-- the main program that imports this module -- lives in the starter
file, not here.
'''


# dwell_time() is already complete. Leave it alone.
def dwell_time(start, end):
    '''Return how many days an intruder sat on the network,
    counting from day-number start to day-number end.'''
    return end - start


# ---- Part 2: MODIFY ---------------------------------------------------
# Two jobs, both in this section -- but do Part 1 (bottom of this file)
# first. Job one: severity_label() below has no code yet, only
# pseudocode. Turn it into code, line by line. Job two: format_ioc()
# works, but it still writes the old line style, ending in
# "confidence=85" -- the SOC standard now shows the scale,
# "confidence=85/100". Add /100 to the end of its f-string. Then run
# this file directly again and check the Shell against the first
# expected output block on the assignment page.
def severity_label(score):
    '''Return the label for a severity score (0-100):
    "LOW" for scores under 40, "GUARDED" for 40 up to but not
    including 70, and "CRITICAL" for 70 and above.'''
    # Pseudocode:
    #   IF score >= 70:
    #       RETURN "CRITICAL"
    #   IF score >= 40:
    #       RETURN "GUARDED"
    #   RETURN "LOW"
    # TODO: write your code below (delete the pass line when you start)
    pass


def format_ioc(indicator, kind, confidence):
    '''Return one standardized IOC line, the same shape every time.'''
    return f"[IOC] {indicator} ({kind}) confidence={confidence}"


# ---- Part 1: READ -----------------------------------------------------
# This block is the module's self-test, and it is already complete.
# Before changing anything, press Run on THIS file (green Run button,
# or F5) and watch the Shell pane: the block prints, because Python
# sets the special variable __name__ to "__main__" when a file is the
# program being run. When another file imports huntkit instead,
# __name__ is "huntkit", the if is False, and the block is skipped --
# the importer gets the functions without the test prints. On this
# first run the severity line shows None None None and the IOC line
# has no /100; both are Part 2's job.
if __name__ == "__main__":
    print("huntkit self-test")
    print(dwell_time(3, 17))
    print(severity_label(12), severity_label(55), severity_label(82))
    print(format_ioc("203.0.113.44", "IP address", 85))
