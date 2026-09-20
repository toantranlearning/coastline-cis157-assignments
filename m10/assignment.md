# M10 Assignment - Phishing URL Analyzer

## What you are doing, and why

You will write a program that reads a URL and scores how suspicious it looks, using nothing but the string operations from this module (`lower()`, `strip()`, `count()`, `startswith()`, and the `in` operator), plus the conditionals you already know. No regular expressions, no URL libraries: every red flag a phishing link carries is visible to plain string code, and building the checks by hand teaches you what the fancy tools are actually doing.

## Scenario

Half of the incident tickets at **Harborwatch Security** start the same way: "I clicked a link." Your lead wants a first-pass triage tool: something an analyst can paste a reported URL into and get an immediate read on how phishy it looks, with a reason for every point of suspicion. It will not replace a real scanner, but it will tell the analyst which tickets to escalate first. That is this assignment: prompt for a URL, run it through a set of string checks, print a reason line for each red flag, and deliver a verdict.

## What you are given

- [Starter file](m10_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. Reading and changing real code before writing your own is how programmers actually learn a codebase, and it is how you will learn Python.

1. Download the starter file and rename it with your own name, all lowercase: `m10_jane_doe.py` for Jane Doe. Keep the `m10_` prefix.
2. **Read.** Part 1 is already complete: it calls `.lower()` and `.count(".")` on a sample URL. Run the program and match each printed line to the method call that produced it. Note the comment: `.lower()` returns a **new** lowercase string; strings are immutable, so no method ever edits a string in place.
3. **Modify.** Part 2 defines `KEYWORDS`, the list of suspicious words your analyzer will scan for. Analysts just flagged a wave of "account" lures. Add `"account"` to the end of the list and run again; the printout should now show five keywords.
4. **Create.** Part 3 has no code yet, only pseudocode. Follow it line by line to build the analyzer. Each red flag adds 1 to a suspicion score and prints a `[+1]` reason line; a passed check prints `[OK]`:
   - Prompt for a URL, then normalize it by chaining `.lower()` and `.strip()` into a new variable and print it on an `Analyzing:` line.
   - Print a `--- Checks ---` header and set the suspicion score to `0`.
   - Length check with `len()`: over 75 characters is a red flag: very long URLs hide their real destination.
   - Credential trick: `"@" in url`. Browsers ignore everything before an `@`, so the trusted name is bait.
   - Dot count with `.count(".")`: more than 3 suggests subdomains stacked up to bury the real domain.
   - Keywords, encryption, and the verdict: for each word in `KEYWORDS`, the `in` operator tells you whether it appears in the URL. Each hit adds 1 with its own reason line. A URL that fails `.startswith("https")` adds one more: the connection is not encrypted. Then print a `--- Verdict ---` header and the score, and map it through `if`/`elif`/`else`: 4 or more is `[LIKELY PHISHING]`, 2 or 3 is `[SUSPICIOUS]`, otherwise `[CLEAN]`.
   - One last utility: define a function `is_palindrome(text)` that lowercases the text and returns whether it equals its own reverse, using slicing with `[::-1]`. Call it on `"racecar"` and `"harborwatch"` and print both results. A palindrome checker is the classic proof of the slicing skill this module teaches.
5. Run the program one last time against the URL in the expected output below and check that every line matches.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. Every program you submit in this course carries this header; professionals sign their work, and so do you.

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

The URL you analyze may differ; the format of the check lines and the verdict must not.

```text
Lowercased: http://example.com/login
Dots: 1
Watching for keywords: ['login', 'verify', 'update', 'secure', 'account']
Enter a URL to analyze: http://paypa1-login.example.tk/verify@account

Analyzing: http://paypa1-login.example.tk/verify@account

--- Checks ---
[OK] Length 45 (75 or fewer characters)
[+1] Contains "@" - browsers ignore everything before it
[OK] Dots: 2 (3 or fewer)
[+1] Suspicious keyword: "login"
[+1] Suspicious keyword: "verify"
[+1] Suspicious keyword: "account"
[+1] Does not start with "https" - connection is not encrypted

--- Verdict ---
Suspicion score: 5
[LIKELY PHISHING] Do not click. Escalate this URL to your lead.

Palindrome check "racecar": True
Palindrome check "harborwatch": False
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and matches the expected output, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
