# M09 Assignment - Package the Huntkit

## What you are doing, and why

You will turn three hunt utilities into a proper Python module (a `.py` file other programs use with `import` instead of copy-paste) and write a main program that imports it four different ways: the whole module with `import huntkit`, one name with `from huntkit import format_ioc`, and two standard-library modules, `math` and `platform`, that ship with Python. Along the way you will see what the `__name__` variable is for, why a module's self-test prints when you run the file but not when you import it, and what `dir()` reveals about any module you load. Every real Python program is mostly imports; this week you learn what is actually happening on those first few lines.

## Scenario

At **Harborwatch Security**, the utilities you built back in M06 (dwell-time math, severity labels, standardized IOC lines) have been a hit. Too much of a hit: every analyst has pasted their own copy into their own scripts, and the copies have started to drift. One analyst's `severity_label` says `GUARDED` where another's says `ELEVATED`, and last week two reports disagreed about the same incident. Your lead's fix is the standard one: the utilities move into a single shared module, `huntkit.py`, that every script imports and nobody copies. You will finish the module's last function, prove to yourself that importing it does not rerun its self-test, and write this week's hunt report as the module's first real customer.

## What you are given

- [Module file](huntkit.py). The shared `huntkit` module and the home of Parts 1 and 2: a finished function and self-test to read and run, one line to modify, and full line-by-line pseudocode for `severity_label()` to turn into code.
- [Starter file](m09_firstname_lastname.py). A header docstring to complete and Part 3: your main program, five steps, each written out in pseudocode for you to turn into code.

If you have not set up Thonny yet, do that first: Course Materials, Software & Technology page in Canvas.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. This week the first two steps happen in the module file and the third in your main file, the same split every real Python project has.

1. Download both files **into the same folder**. Rename the starter file with your own name, all lowercase: `m09_jane_doe.py` for Jane Doe. Keep the `m09_` prefix, and do **not** rename `huntkit.py`, because `import huntkit` finds the module by its filename.
2. **Read.** Part 1 is at the bottom of `huntkit.py`: press Run on that file directly and watch its self-test print in the Shell. It prints because Python sets the special variable `__name__` to `"__main__"` when a file is the program being run; the comment above the block tells the story. On this first run the severity line shows `None None None` and the IOC line has no `/100`. Both are Part 2's job.
3. **Modify.** Part 2 is the marked section in the middle of `huntkit.py`, two jobs: turn `severity_label()`'s pseudocode into code, line by line, and update `format_ioc()` to the current SOC line style by adding `/100` to the end of its f-string. Run `huntkit.py` directly again and check it against the first expected output block below.
4. **Create.** Part 3 is your main file, which has no code yet: only pseudocode, five steps of it. Follow it line by line: import `huntkit` whole and call its three functions through the module name, import `format_ioc` by itself with `from huntkit import`, print `dir(huntkit)` to list every name the module contains, and close with a report footer built on the standard-library `math` and `platform` modules. Notice as you run it that the self-test does **not** print: importing sets `__name__` to `"huntkit"`, not `"__main__"`.
5. Run your main file and check it against the second expected output block below. The first time it imports `huntkit`, Python drops a `__pycache__` folder next to your files: the compiled copy it caches to speed up later imports. Leave it alone; it is not part of your submission.
6. Complete the header at the top of your main file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. Every program you submit in this course carries this header; professionals sign their work, and so do you.

**Try pip once (nothing to submit).** `math` and `platform` ship with Python, but most of the Python world lives in packages you install with **pip**. In Thonny, open **Tools > Manage packages**, search for `requests` (the standard library for talking to web APIs), and click **Install**; the terminal equivalent is `pip install requests`. Watch what pip reports, then uninstall it the same way if you like. This assignment deliberately needs no third-party package (everything above runs offline), but installing one is a five-minute skill you will use constantly after this course.

Open notes and open book are both fine. Respond in your own words; do not copy from other sources.

**Acceptable AI use.** Itemized for this course; the syllabus policy governs.

> [!TIP] These uses are permitted
> - Asking an AI to explain a course concept or a Python error message, in general terms, while you study.
> - Grammar and spelling help on the written reflection in your header.
> - After your program works: asking an AI to show a different approach, described in your own words, to compare with what you wrote.

> [!CAUTION] These uses are not permitted
> - Generating any part of the code or reflection you submit.
> - Pasting the assignment page or the starter file into an AI tool.
> - Submitting or paraphrasing AI output as your own work.

You must be able to explain every line you submit, on request. Undisclosed AI use is handled as academic dishonesty under the syllabus.

## Expected output

Two runs to check. First, running `huntkit.py` directly (after Part 2 is done) prints the self-test:

```text
huntkit self-test
14
LOW GUARDED CRITICAL
[IOC] 203.0.113.44 (IP address) confidence=85/100
```

Then, running your completed main file prints the report below, with no self-test lines in front of it. The last line comes from `platform.platform()` and will name your own machine's operating system instead of this one; every other line must match.

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

Upload **two** `.py` files: no document, no screenshots, no `__pycache__` folder. They are the completed `huntkit.py`, still under its original name, and the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the main file is renamed with your own name while `huntkit.py` keeps its exact name, both files sit in the same folder and your main file runs in Thonny without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
