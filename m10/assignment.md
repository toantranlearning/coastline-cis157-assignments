# M10 Assignment - Phishing URL Analyzer

## What you are doing, and why

You will write a program that reads a URL and scores how suspicious it looks. It uses the string operations from this module (`lower()`, `strip()`, `count()`, `startswith()`, and the `in` operator) and the conditionals you already know. Do not use regular expressions or URL libraries. Every check in this assignment can be written with plain string code.

## Scenario

At **Harborwatch Security**, many incident tickets begin with someone clicking a link. Your lead wants a first-pass triage tool: an analyst pastes in a reported URL and uses the result to decide which tickets to escalate first. Your program prompts for a URL, runs it through a set of string checks, prints a reason line for each red flag, and prints a verdict.

## What you are given

- [Starter file](m10_firstname_lastname.py). A header docstring to complete and three parts: working code to read, working code to modify, and pseudocode to turn into your own code.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter.

1. Download the starter file and rename it with your own name, all lowercase: `m10_jane_doe.py` for Jane Doe. Keep the `m10_` prefix.
2. **Read.** Part 1 is already complete. It calls `.lower()` and `.count(".")` on a sample URL. Run the program and match each printed line to the method call that produced it. Then read the comment: `.lower()` returns a **new** lowercase string. Strings are immutable, so no method ever edits a string in place.
3. **Modify.** Part 2 defines `KEYWORDS`, the list of suspicious words your analyzer will scan for. Analysts have flagged a wave of "account" lures. Add `"account"` to the end of the list and run again. The printout should now show five keywords.
4. **Create.** Part 3 has no code yet, only pseudocode. Follow it line by line to build the analyzer. Each red flag adds 1 to a suspicion score and prints a `[+1]` reason line. A check that passes prints an `[OK]` line. The pseudocode gives the exact wording of every line.
   - Prompt for a URL. Normalize it by chaining `.lower()` and `.strip()` into a new variable, then print it on an `Analyzing:` line.
   - Print a `--- Checks ---` header and set the suspicion score to `0`.
   - Length check: use `len()`. Over 75 characters is a red flag, because a very long URL hides its real destination.
   - Credential trick: test `"@" in url`. Browsers ignore everything before an `@`, so a trusted name placed in front of it is bait.
   - Dot count: use `.count(".")`. More than 3 dots is a red flag, because subdomains stacked up bury the real domain.
   - Keywords: for each word in `KEYWORDS`, use the `in` operator to test whether the word appears in the URL. Each hit adds 1 and prints its own reason line.
   - Encryption: a URL that fails `.startswith("https")` adds 1, because the connection is not encrypted.
   - Verdict: print a `--- Verdict ---` header and the score. Then map the score through `if`/`elif`/`else`: 4 or more is `[LIKELY PHISHING]`, 2 or 3 is `[SUSPICIOUS]`, otherwise `[CLEAN]`.
   - Palindrome check: define a function `is_palindrome(text)` that lowercases the text and returns whether it equals its own reverse, using slicing with `[::-1]`. Call it on `"racecar"` and `"harborwatch"` and print both results.
5. Run the program one last time. Enter the URL shown in the expected output below and check that every line matches.
6. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain what the "in" operator does when used with two strings, as in "login" in url.

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

The URL you analyze may differ. The format of the check lines and the verdict must match this.

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
