# CIS C157 Assignments

Starter files and assignment instructions for **CIS C157, Introduction to Python Programming** at Coastline College.

Everything you need to write your programs is here. Everything that decides your grade is in Canvas.

> [!IMPORTANT]
> **Canvas is the source of truth.** Due dates, grades, announcements, discussions, quizzes and exams all live there, and you submit your finished work there. The instructions in this repository are a convenience copy. If a page here and a page in Canvas ever disagree, Canvas wins, and please tell me so I can fix it.

## Start here

Two ways to get a working Python setup. Pick one.

**1. No install, in a browser tab.** This button opens Google Cloud Shell with every starter file already cloned in and a short guided walkthrough open beside the editor. Python is already installed. Click it once, follow the panel, and you are ready to work.

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/open?cloudshell_git_repo=https://github.com/toantranlearning/coastline-cis157-assignments&cloudshell_tutorial=TUTORIAL.md)

Use that button **once**, to set up. After that, come back through [shell.cloud.google.com](https://shell.cloud.google.com/), which reopens the machine you already have with your work on it. The setup button copies the course folder in fresh every time it is opened, so returning that way just leaves spare copies for `start.sh` to clear up.

> [!WARNING]
> **Sign in with a personal Google account, not your Coastline one.** Google blocks Cloud Shell for Workspace for Education accounts by default, and it is not available to anyone under 18. If the button refuses to open for you, message me in the Canvas Inbox and say which account you tried. Full setup notes are on the Setting Up Google Cloud Shell page in Canvas.

**2. Install it on your own computer.** [Download Thonny](https://thonny.org/). One installer, Python included, nothing to configure. This is the course standard and it is the better option if your computer allows it: it opens faster, works offline, and its debugger is friendlier while loops are new.

Either way, once you can run `print("hello")` you are set for the whole term.

<sub>Cloud Shell users: each time you open the project, run `bash scripts/start.sh` first. Cloud Shell clones a fresh copy of the folder every time the setup link is opened, so this clears out the spares and keeps the one your work is in. It also turns the editor's AI suggestions off and confirms Python is ready.</sub>

## What is in here

One folder per assignment, named the way the course names them.

| Folder | Assignment | What is in it |
|---|---|---|
| `m01` to `m07` | M01 through M07 | The starter file and the instructions |
| `midterm` | M08 Midterm Project | The starter file and the instructions |
| `m09` to `m15` | M09 through M15 | The starter file and the instructions |

There is no `m08` folder. M08 is the Midterm, and its folder is called `midterm`.

Two assignments need a second file, and both are already in their folder:

- **`m09`** also has `huntkit.py`. Your main file imports it, so the two must sit in the same folder.
- **`m14`** also has `server.log`. Your program opens it by name, so it must sit in the same folder as your program.

## How to use it

If you used the Cloud Shell button above, the files are already there and you can skip this section. Otherwise, you do not need Git or a GitHub account for this course. Either way works:

**The simple way.** Open the folder for this week's assignment, open the starter file, and use the **Download raw file** button. Do the same for `huntkit.py` or `server.log` if the folder has one.

**The Git way**, if you already know it or want to learn:

```bash
git clone https://github.com/toantranlearning/coastline-cis157-assignments.git
cd coastline-cis157-assignments
```

Then pull before each new assignment, in case I have corrected something:

```bash
git pull
```

## The workflow, every week

1. Get the starter file for the week.
2. **Rename it with your own name, all lowercase**, keeping the prefix. Jane Doe turns `m01_firstname_lastname.py` into `m01_jane_doe.py`.
3. Complete the numbered requirements in your editor. Every assignment has three parts: read working code, modify working code, then write your own from the pseudocode in the file.
4. Run it and check your output against the **Expected output** section of that folder's `assignment.md`.
5. Fill in the header at the top of the file: your name, the date, a one-line description, and the reflection.
6. **Upload the single `.py` file to Canvas.** No documents, no screenshots, no pasted text. I run your file.

## One rule

**You write every line you submit, and you must be able to explain any line on request.**

Generative AI is welcome as a tutor. Ask it to explain a concept or tell you what an error message means. No assignment in this course requires an AI tool. AI-written code or reflection text submitted as your own work is plagiarism, and so is code copied from a classmate or the internet without attribution. The full policy is on the Academic Honesty page in Canvas.

## If you get stuck

Post in the week's discussion in Canvas. Share **no more than three lines** of your code there, so your post is a question rather than a solution. For anything specific to you or your grade, message me in the Canvas Inbox.
