# CIS C157 Assignments

<walkthrough-tutorial-duration duration="10"></walkthrough-tutorial-duration>

Welcome to **CIS C157, Introduction to Python Programming**. You are looking at your own private copy of every starter file in the course, on a free Linux computer that Google runs for you.

You are signed in to Google, which is what makes this Cloud Shell yours. Nobody else can see or reach this copy, and you do **not** need a credit card or a paid trial for any of it. If a banner offers "$300 in free credits," close it. You do not need it.

Python is already installed here. Nothing to download, nothing to configure.

**Check that it is working.** Click the run icon on the command below:

```bash
python3 --version
```

If it prints a version number starting with 3, you are set for the entire term. Click **Next**.

## What you are looking at

The screen has three parts:

- <walkthrough-editor-spotlight spotlightId="file-explorer">The file list on the left</walkthrough-editor-spotlight> holds one folder per assignment: `m01` through `m07`, then `midterm`, then `m09` through `m15`. There is no `m08`, because that slot is the Midterm. Click a folder to open it.
- The **editor** in the middle is where you write your code.
- The black **terminal** across the bottom is where you run your programs.

Each folder holds the starter file you complete and an `assignment.md` with the full instructions, the same ones posted in Canvas.

<walkthrough-footnote>Click the launch link only once. If you click it again later, Cloud Shell makes a second copy of the folder. Next time, just reopen this Cloud Shell tab, or go to shell.cloud.google.com.</walkthrough-footnote>

## Run your first program

Every assignment works the same way. Start by running the starter before you change anything, so you can see what it already does.

```bash
cd m01
```

```bash
python3 m01_firstname_lastname.py
```

That is the M01 starter, and it prints a greeting. Programs that ask you questions work here too: when one stops and waits, type your answer into the terminal and press **Enter**.

**Always move into the assignment's folder first.** That is what the `cd` command does, and it matters: in M14 your program opens a log file by name, and it looks for that file in whichever folder the terminal is sitting in. Work from inside the folder and everything finds everything else.

Now open it and read it. <walkthrough-editor-open-file filePath="m01/m01_firstname_lastname.py">Open the M01 starter</walkthrough-editor-open-file>. Every assignment file has the same three parts: code to **read**, code to **modify**, and pseudocode you turn into your own code.

## Put your name on it

Before you do the work, rename the file with your own name, all lowercase, keeping the prefix. Jane Doe would run:

```bash
mv m01_firstname_lastname.py m01_jane_doe.py
```

You can also right-click the file in the list and choose **Rename**.

Then fill in the header at the top of the file: your name, the date, a one-line description, and the reflection. Save with **Ctrl-S**, or **Cmd-S** on a Mac.

<walkthrough-footnote>Keep the .py ending. A file saved as m01_jane_doe.py.txt will not run, and I cannot grade it.</walkthrough-footnote>

## Hand it in

Canvas is where you submit, so the last step is getting your finished file out of Cloud Shell and onto your own computer.

Right-click the file in the file list and choose **Download**. Your browser saves it, and you upload that one `.py` file to the assignment in Canvas.

The terminal does the same thing:

```bash
cloudshell download m01_jane_doe.py
```

Submit **one** `.py` file. No documents, no screenshots, no pasted text. I run your file.

## Getting updates, and keeping your work

If I correct a starter file or an assignment page during the term, pull the change:

```bash
git pull
```

Your own files are safe. Git only replaces the files I changed, and it will warn you rather than overwrite work you have edited.

Two things worth knowing about this machine:

- Your home folder here holds **5 GB** and it keeps your files between sessions. You get **50 hours a week**, which is far more than this course needs.
- If you do not open Cloud Shell for **120 days**, Google deletes your home folder. That will not happen during a single term, but do not treat this as long-term storage. Once you have submitted an assignment, you already have a copy on your own computer from the download step.

## You are set up

You can run a program, edit it, rename it, and download it to hand in. That is the whole workflow, and it is the same for all fifteen assignments.

Each week, `cd` into that assignment's folder, read its `assignment.md`, and check your output against the **Expected output** section before you submit. To get back to the top from inside a folder, run `cd ..`.

One rule, and it does not change: **you write every line you submit, and you must be able to explain any line I ask about.** AI is welcome as a tutor to explain a concept or an error message. It does not write your code.

If you get stuck, post in the week's discussion in Canvas, sharing no more than three lines of code, or message me in the Canvas Inbox.

<walkthrough-footnote>To bring this panel back any time, run `teachme TUTORIAL.md` in the terminal.</walkthrough-footnote>

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>
