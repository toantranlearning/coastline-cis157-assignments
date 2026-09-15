# CIS C157 Assignments

<walkthrough-tutorial-duration duration="10"></walkthrough-tutorial-duration>

Welcome to **CIS C157, Introduction to Python Programming**. You are looking at your own private copy of the course content, every starter file and every assignment's instructions, ready to use on a free Linux computer that Google runs for you.

You are signed in to Google, which is what makes this Cloud Shell yours. Nobody else can see or reach this copy, and you do **not** need a credit card or a paid trial for any of it. If a banner offers "$300 in free credits," close it. You do not need it.

Python is already installed here. Nothing to download, nothing to configure.

If a **Gemini Code Assist** notice popped up, dismiss it. You do not need it, and the command below turns it off.

**Start by running this. Do not skip it.** Click the icon beside the command below. That only pastes the command into the terminal; press **Enter** to run it.

```bash
source scripts/start.sh
```

<walkthrough-footnote>Every command in this panel works the same way: the icon pastes it, Enter runs it.</walkthrough-footnote>

Run this **every time** you open the project, not just the first time. It is quick, and its main job is tidying up after Cloud Shell:

- **Clears out the spare copies Google leaves behind.** Every time the setup link is opened, Cloud Shell clones the course folder again instead of reusing the one you already have, and it shows you the new one. That is simply how it works, not something you did wrong, but the copies pile up and you can end up typing into one while your work sits in another. This leaves you with exactly one copy, the one your work is in, and moves your terminal into it.
- **Turns the editor's AI code suggestions off**, because in this course you write every line you submit.
- **Confirms Python is ready** and tells you where your folder is.

When it reports the Python version, you are set for the entire term. Click **Next**.

## What you are looking at

The screen has three parts:

- <walkthrough-editor-spotlight spotlightId="file-explorer">The file list on the left</walkthrough-editor-spotlight> holds one folder per assignment: `m01` through `m07`, then `midterm`, then `m09` through `m15`. There is no `m08`, because that slot is the Midterm. Click a folder to open it.
- The **editor** in the middle is where you write your code.
- The black **terminal** across the bottom is where you run your programs.

Each folder holds the starter file you complete and an `assignment.md` with the full instructions, the same ones posted in Canvas.

<walkthrough-footnote>Come back through the Launch button on the course page or in the README: it reopens this folder and this panel without making another copy. The Set up button makes a fresh copy every time it is used, so if you use it again by habit, the start command tidies up after it.</walkthrough-footnote>

## Run your first program

Every assignment works the same way. Start by running the starter before you change anything, so you can see what it already does.

1. In the file list on the left, click the `m01` folder, then click `m01_firstname_lastname.py`. It opens in the editor. This shortcut does the same: <walkthrough-editor-open-file filePath="m01/m01_firstname_lastname.py">open the M01 starter</walkthrough-editor-open-file>.
2. With that file showing in the editor, click the **Run** triangle at the top right. Run always runs the tab in front, so if you have the instructions or another file open too, click the `.py` tab first. The program's output appears in a panel below it.

That is the M01 starter, and it prints a greeting. Programs that ask you questions work here too: when one stops and waits, type your answer into that panel and press **Enter**.

Read the file while it is open. Every assignment file has the same three parts: code to **read**, code to **modify**, and pseudocode you turn into your own code.

**If you prefer the terminal**, move into the assignment's folder and run the file by name:

```bash
cd m01
```

```bash
python3 m01_firstname_lastname.py
```

Being in the right folder matters whenever a program opens a file that sits beside it, which M14 does. The Run button handles that for you; in the terminal, `cd` first. To go back up a level later, run `cd ..`.

<walkthrough-footnote>If the Run button ever reports that a file such as server.log cannot be found, use the terminal for that assignment: cd into its folder and run it there.</walkthrough-footnote>

## Put your name on it

Before you do the work, rename the file with your own name, all lowercase, keeping the prefix.

1. Right-click the file in the file list and choose **Rename**. Jane Doe would name it `m01_jane_doe.py`.
2. Fill in the header at the top of the file: your name, the date, a one-line description, and the reflection.
3. Save with **Ctrl-S**, or **Cmd-S** on a Mac.

The terminal does the rename too, if you are already there:

```bash
mv m01_firstname_lastname.py m01_jane_doe.py
```

<walkthrough-footnote>Keep the .py ending. A file saved as m01_jane_doe.py.txt will not run, and I cannot grade it.</walkthrough-footnote>

## When something goes wrong

Three tools, and you will want all of them before the term is out.

**Read the error.** When a program fails, Python prints a traceback in the output panel. The last line names the problem and the line above it points at your code. That is usually enough.

**Undo a change.** Open the <walkthrough-editor-spotlight spotlightId="activity-bar-scm">Source Control</walkthrough-editor-spotlight> panel. It lists every file you have changed, and clicking one shows exactly what changed, old on the left and new on the right. Hover a file and click its discard arrow to put that file back to the starter you were given. The terminal equivalent restores a whole assignment folder:

```bash
bash scripts/reset.sh --starter m01
```

**Step through it.** From M04 onward, when loops arrive, it helps to watch your program run one line at a time. Click in the narrow margin to the left of a line number to set a **breakpoint**, a red dot where the program will pause. Then open the <walkthrough-editor-spotlight spotlightId="activity-bar-debug">Run and Debug</walkthrough-editor-spotlight> panel and start it. The program stops at your dot, and the panel lists every variable and its current value, updating as you step forward.

Watching two values trade places is worth more than reading about it. You do not need this for M01. Come back when you reach M04.

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

One rule, and it does not change: **you write every line you submit, and you must be able to explain any line I ask about.** AI is welcome as a tutor to explain a concept or an error message. It does not write your code. The start command switches the editor's AI suggestions off for you, so you are not fighting a tool that wants to finish your sentences while you are learning to write them.

If you get stuck, post in the week's discussion in Canvas, sharing no more than three lines of code, or message me in the Canvas Inbox.

<walkthrough-footnote>To bring this panel back any time, run `teachme TUTORIAL.md` in the terminal.</walkthrough-footnote>

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>
