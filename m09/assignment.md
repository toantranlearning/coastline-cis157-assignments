# M09 Assignment - Package the Huntkit

## What you are doing, and why

You will finish a Python module, `huntkit.py`, and write a main program that imports it. A module is a `.py` file that other programs use with `import` instead of copy and paste. The main program practices four imports: the whole module with `import huntkit`, one name with `from huntkit import format_ioc`, and two standard-library modules that ship with Python, `math` and `platform`. You will also see what the `__name__` variable is for, why a module's self-test prints when you run the file but not when you import it, and what `dir()` lists for a module you have loaded.

## Scenario

At **Harborwatch Security**, utilities like the ones you wrote in M06 (dwell-time math, severity labels, standardized IOC lines) have been pasted into many analysts' scripts, and the copies no longer match. One analyst's `severity_label` says `GUARDED` where another's says `ELEVATED`, and two reports disagreed about the same incident. The utilities are moving into a single shared module, `huntkit.py`, that every script imports and nobody copies. You finish the module's last function, confirm that importing the module does not rerun its self-test, and write a hunt report that imports it.

## What you are given

- [Module file](huntkit.py). The shared `huntkit` module. Parts 1 and 2 are in this file: a finished function and self-test to read and run, one line to modify, and line-by-line pseudocode for `severity_label()` to turn into code.
- [Starter file](m09_firstname_lastname.py). A header docstring to complete and Part 3, your main program: five steps, each written as pseudocode for you to turn into code.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter. The read and modify steps happen in `huntkit.py`. The create step happens in your main file.

1. Download both files **into the same folder**.
   - Rename the starter file with your own name, all lowercase: `m09_jane_doe.py` for Jane Doe. Keep the `m09_` prefix.
   - Do **not** rename `huntkit.py`. `import huntkit` finds the module by its filename, so a renamed file cannot be found.
2. **Read.** Part 1 is the self-test block at the bottom of `huntkit.py`. It is already complete.
   - Run `huntkit.py` directly and watch the self-test print in the output.
   - It prints because Python sets the special variable `__name__` to `"__main__"` when a file is the program being run. The comment above the block explains this.
   - On this first run the severity line shows `None None None` and the IOC line has no `/100`. You fix both in Part 2.
3. **Modify.** Part 2 is the marked section in the middle of `huntkit.py`. It has two jobs.
   - Turn the pseudocode in `severity_label()` into code, line by line.
   - Update `format_ioc()` to the current SOC line style: add `/100` to the end of its f-string.
   - Run `huntkit.py` directly again and check the output against the first expected output block below.
4. **Create.** Part 3 is your main file. It has no code yet, only pseudocode, in five steps. Follow the pseudocode line by line.
   - Import `huntkit` whole and call its three functions through the module name.
   - Import `format_ioc` by itself with `from huntkit import`.
   - Print `dir(huntkit)` to list every name the module contains.
   - End with a report footer built on the standard-library `math` and `platform` modules.
   - When you run the main file, the self-test does **not** print. Importing sets `__name__` to `"huntkit"`, not `"__main__"`, so Python skips the self-test block.
5. Run your main file and check it against the second expected output block below. The first time it imports `huntkit`, Python creates a `__pycache__` folder next to your files. The folder holds a compiled copy of the module that Python keeps to speed up later imports. Leave it alone. It is not part of your submission.
6. Complete the header at the top of your main file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain what the __name__ variable is for.

**Try pip once (nothing to submit).** `math` and `platform` ship with Python. Most other Python packages are installed with **pip**. Run `pip install requests` in a terminal. The setup page for your editor says where its package installer is, if it has one. `requests` is the package most Python programs use to talk to web APIs. Watch what pip reports, then uninstall it the same way if you like. This assignment needs no third-party package, and everything above runs offline. The point is to install a package once now, because you will need to do it in later Python work.

Open notes and open book are both fine. Respond in your own words; do not copy from other sources.

**Acceptable AI use.** Itemized for this course; the syllabus policy governs.

> [!TIP]
> **These uses are permitted**
> - Asking an AI to explain a course concept or a Python error message, in general terms, while you study.
> - Grammar and spelling help on the written reflection in your header.
> - After your program works: asking an AI to show a different approach, described in your own words, to compare with what you wrote.

> [!CAUTION]
> **These uses are not permitted**
> - Generating any part of the code or reflection you submit.
> - Pasting the assignment page or the starter file into an AI tool.
> - Submitting or paraphrasing AI output as your own work.

You must be able to explain every line you submit, on request. Undisclosed AI use is handled as academic dishonesty under the syllabus.

## Expected output

There are two runs to check. First, run `huntkit.py` directly after Part 2 is done. It prints the self-test:

```text
huntkit self-test
14
LOW GUARDED CRITICAL
[IOC] 203.0.113.44 (IP address) confidence=85/100
```

Second, run your completed main file. It prints the report below, with no self-test lines in front of it. The last line comes from `platform.platform()` and names your own machine's operating system, so yours will differ from this one. Every other line must match.

```text
Dwell time: 14 days
Severity 82: CRITICAL
[IOC] 203.0.113.44 (IP address) confidence=85/100
[IOC] 44d88612fea8a8f36de82e1278abb02f (file hash) confidence=60/100
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'dwell_time', 'format_ioc', 'severity_label']
Average severity (rounded up): 66
Workstation: macOS-26.6.1-arm64-arm-64bit
```

## What to submit

Upload **two** `.py` files: no document, no screenshots, no `__pycache__` folder. The first is the completed `huntkit.py`, still under its original name. The second is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things:

- The main file is renamed with your own name, and `huntkit.py` keeps its exact name.
- Both files are in the same folder, and the main file runs without errors and matches the expected output.
- Every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
