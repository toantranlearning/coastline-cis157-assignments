# CIS C157 Assignments

Starter files and assignment instructions for **CIS C157, Introduction to Python Programming** at Coastline College.

Everything you need to write your programs is here. Everything that decides your grade is in Canvas.

> [!IMPORTANT]
> **Canvas is the source of truth.** Due dates, grades, announcements, discussions, quizzes and exams all live there, and you submit your finished work there. The instructions in this repository are a convenience copy. If a page here and a page in Canvas ever disagree, Canvas wins, and please tell me so I can fix it.

## Start here

[![Set up Cloud Shell](https://img.shields.io/badge/Set_up_Cloud_Shell-first_visit-0b4f8a?style=for-the-badge&logo=googlecloud&logoColor=white)](https://shell.cloud.google.com/cloudshell/open?cloudshell_git_repo=https://github.com/toantranlearning/coastline-cis157-assignments&cloudshell_tutorial=TUTORIAL.md)
[![Launch Cloud Shell](https://img.shields.io/badge/Launch_Cloud_Shell-every_visit_after-0b4f8a?style=for-the-badge&logo=googlecloud&logoColor=white)](https://shell.cloud.google.com/cloudshell/open?cloudshell_workspace=cloudshell_open/coastline-cis157-assignments&cloudshell_tutorial=TUTORIAL.md)

Two ways to get a working Python setup. Pick one.

**1. No install, in a browser tab.** Google Cloud Shell gives you a full Linux machine with Python already on it. The two buttons above are the whole workflow:

- **Set up**, on your first visit. It signs you in, builds your machine, and puts a copy of the course content in it ready to use: every starter file and every assignment's instructions. A short walkthrough opens beside the editor.
- **Launch**, every visit after that. It reopens that same folder with your work in it, and brings the walkthrough back so you have the shortcuts to hand. Nothing is copied twice.

If Cloud Shell will not open for you, message me in the Canvas Inbox and say which account you tried.

**2. Install it on your own computer.** [Download Thonny](https://thonny.org/). One installer, Python included, nothing to configure. This is the course standard and it is the better option if your computer allows it: it opens faster, works offline, and its debugger is friendlier while loops are new.

Either way, once you can run `print("hello")` you are set for the whole term.

<sub>Cloud Shell users: each time you open the project, run `source scripts/start.sh` first. Cloud Shell clones a fresh copy of the folder every time the Set up button is used, so this clears out the spares, keeps the one your work is in, and moves your terminal into it. It also turns the editor's AI suggestions off and confirms Python is ready.</sub>

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

If you used the Set up button above, the course content is already there and you can skip this section. Otherwise, you do not need Git or a GitHub account for this course. Either way works:

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
