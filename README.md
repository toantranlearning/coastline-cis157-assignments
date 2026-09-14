# CIS C157 Assignments

Starter files and assignment instructions for **CIS C157, Introduction to Python Programming** at Coastline College.

Everything you need to write your programs is here. Everything that decides your grade is in Canvas.

> [!IMPORTANT]
> **Canvas is the source of truth.** Due dates, grades, announcements, discussions, quizzes and exams all live there, and you submit your finished work there. The instructions in this repository are a convenience copy. If a page here and a page in Canvas ever disagree, Canvas wins, and please tell me so I can fix it.

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

You do not need Git or a GitHub account for this course. Either way works:

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

## Setting up Python

The course-standard editor is [Thonny](https://thonny.org/), whose installer includes Python itself, so there is nothing else to download or configure.

If your computer will not let you install software, a Chromebook or a managed work machine for example, the course orientation module in Canvas has a page on using Google Cloud Shell, which gives you a full Linux machine with Python already on it, in a browser tab, for free.

## One rule

**You write every line you submit, and you must be able to explain any line on request.**

Generative AI is welcome as a tutor. Ask it to explain a concept or tell you what an error message means. No assignment in this course requires an AI tool. AI-written code or reflection text submitted as your own work is plagiarism, and so is code copied from a classmate or the internet without attribution. The full policy is on the Academic Honesty page in Canvas.

## If you get stuck

Post in the week's discussion in Canvas. Share **no more than three lines** of your code there, so your post is a question rather than a solution. For anything specific to you or your grade, message me in the Canvas Inbox.
