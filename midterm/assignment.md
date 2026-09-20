# Midterm Project: Hunt the Intruder

## What you are doing, and why

You will build a complete console game: a battleship-style hunt on a 3x3 grid. It uses the Python from the first half of this course in one program: nested lists for the grid, functions to organize the work, a `while` loop to run the game, conditionals to check input and resolve each move, booleans to track the outcome, and f-strings to report status. This project is worth **60 points**, about double a module assignment, and this page is longer than usual. Read all of it before you write any code.

## Scenario

**Harborwatch Security** runs a tabletop exercise every quarter, and your lead has asked you to build this year's edition. An intruder is hiding on one host in a client's 3x3 network grid, and the analyst playing has 4 probes to find the intruder among the 9 hosts. Each probe checks one host and either comes back clean or finds the intruder. Your program hides the intruder, draws the grid, takes the probes, and reports the result.

## What you are given

- [Starter file](midterm_firstname_lastname.py). A header docstring to complete and three parts: a complete, working board-display function to read and run, a banner with a probe-budget constant to modify, and the rest of the game (two more functions and the main program) to create from line-by-line pseudocode in seven steps. Each step builds on the one before it.

## Instructions

Work in three steps: **read** the working code, **modify** it, then **create** your own from the pseudocode in the starter. On the midterm the create step is the large one: Part 3 has seven pseudocode steps, and most of the 60 points are there.

1. Download the starter file and rename it with your own name, all lowercase: `midterm_jane_doe.py` for Jane Doe. Keep the `midterm_` prefix.
2. Read the whole starter before you write anything, so you can see how the three parts fit together into one game.
3. **Read.** Part 1 is a complete function, `display_board(board)`, plus two demo lines that draw a sample board from the middle of a game. Run the program and study the grid.
   - Column numbers run across the top, and row numbers run down the left side.
   - Each host is one character: `.` for a host not yet probed, `o` for a host probed and found clean, and `X` for the intruder once found.
   - The function already matches the board format in the expected output below exactly, including the `+---+` grid lines. Do not change it. The rest of the game calls it as it is.
4. **Modify.** Part 2 prints the exercise banner, but the starter still has last year's probe budget.
   - Change `PROBES` from `5` to `4`, run again, and confirm the banner reports 4 probes.
   - Change only the constant. The banner's f-string and the rest of the game read `PROBES`, so the whole program follows.
5. **Create.** Part 3 is the rest of the game, in seven steps. Each step has complete line-by-line pseudocode.
   - Translate each line of the pseudocode. Do not invent your own structure.
   - Build one step at a time, and run the program after every step, not only at the end.
   - Step 3.1 deletes the two demo lines from Part 1. The finished game builds its own board and must not print the sample grid.
6. Steps 3.2 and 3.3 are the game's other two functions.
   - Step 3.2 is one input-validation function, used for both the row and the column. It takes a label (`"row"` or `"column"`), uses the label in its prompt, and keeps asking until it gets an integer from 0 to 2.
   - Inside it, use `try`/`except` to catch input that is not a number, and a conditional to catch numbers that are off the grid.
   - Invalid input never costs a probe. The function explains the problem and asks again.
   - Step 3.3 is the probe-resolution function. On a hit it marks the host `X` and returns `True`. Otherwise it marks the host `o` and returns `False`. The game's boolean values come from this function.
7. Step 3.4 is the opening. Ask for the client **case number**, which is an integer. Validate it with `try`/`except`, as you did for the row and column.
   - Work out the intruder's position from the case number: `position = case_number % 9`, then `row = position // 3` and `column = position % 3`.
   - A real program would place the intruder at random, but Python's `random` module is not covered until M09. Until then, the case number the user types stands in for it and gives a position that is hard to predict.
   - Try a few case numbers and watch how the position changes. When you learn `random` in M09, you will stop using this trick.
8. Steps 3.5 through 3.7 are the game itself.
   - Step 3.5 sets up the board and the game state. Build the board as a **list of three lists**, with every host starting as `"."`. The game state is `PROBES` probes remaining and a boolean that starts as `False` and records whether the intruder has been found.
   - Step 3.6 is the main `while` loop, one turn per pass. Display the board and print an f-string status line with the probes remaining and the hosts cleared. To get the hosts cleared, count the `o` marks. Then get a row and a column with your validation function.
   - A host that was already probed costs no probe. Print the message that says so and go around the loop again. Otherwise spend one probe and resolve it with your probe-resolution function.
   - Step 3.7 is the ending. Display the final board, then print the win line, or the lose line that reveals the intruder's host. Match both lines to the expected output exactly.
9. Play at least three full games.
   - One game that you win.
   - One game that you lose.
   - One game where you type bad input: letters, numbers off the grid, and hosts you already probed. Confirm that none of it costs a probe or crashes the program.
10. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. The reflection prompt in the starter also asks you to explain why the case-number trick is not truly random.

You do not need tuples, dictionaries, classes, file handling, or the `random` module for this project. If you have already met tuples or dictionaries and want to use them, that is allowed. The whole game can be built without them.

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

The session below used case number `2026`. The player probed row 1 column 1, typed an off-grid row of 5, probed row 0 column 0 twice (the second time is the already-probed case), and then probed row 0 column 1. Your session will differ, because the case number, the intruder's position, and the moves are up to the player. The board format, the prompts, the status lines, and the win and lose lines must match this exactly, and the banner must report the 4-probe budget from your Part 2 change. This session is a win, so the lose line does not appear in it. The lose line is: `Out of probes. The intruder was hiding on host (row, column). You lose.` with the real coordinates filled in.

```text
=== HARBORWATCH TABLETOP: HUNT THE INTRUDER ===
An intruder is hiding on one host in the 3x3 network grid.
You have 4 probes to find them. Good hunting.

Enter the client case number for this exercise: 2026

    0   1   2
  +---+---+---+
0 | . | . | . |
  +---+---+---+
1 | . | . | . |
  +---+---+---+
2 | . | . | . |
  +---+---+---+
Probes remaining: 4 | Hosts cleared: 0/9
Enter the row to probe (0-2): 1
Enter the column to probe (0-2): 1
Host (1, 1) is clean.

    0   1   2
  +---+---+---+
0 | . | . | . |
  +---+---+---+
1 | . | o | . |
  +---+---+---+
2 | . | . | . |
  +---+---+---+
Probes remaining: 3 | Hosts cleared: 1/9
Enter the row to probe (0-2): 5
5 is off the grid. No probe used -- try again.
Enter the row to probe (0-2): 0
Enter the column to probe (0-2): 0
Host (0, 0) is clean.

    0   1   2
  +---+---+---+
0 | o | . | . |
  +---+---+---+
1 | . | o | . |
  +---+---+---+
2 | . | . | . |
  +---+---+---+
Probes remaining: 2 | Hosts cleared: 2/9
Enter the row to probe (0-2): 0
Enter the column to probe (0-2): 0
Host (0, 0) was already probed. No probe used -- pick another host.

    0   1   2
  +---+---+---+
0 | o | . | . |
  +---+---+---+
1 | . | o | . |
  +---+---+---+
2 | . | . | . |
  +---+---+---+
Probes remaining: 2 | Hosts cleared: 2/9
Enter the row to probe (0-2): 0
Enter the column to probe (0-2): 1
Contact! The intruder is on host (0, 1).

    0   1   2
  +---+---+---+
0 | o | X | . |
  +---+---+---+
1 | . | o | . |
  +---+---+---+
2 | . | . | . |
  +---+---+---+
You found the intruder. The network is secure -- you win!
```

## What to submit

Upload **one** `.py` file: no document, no screenshots. It is the starter you downloaded, renamed with your own name and completed.

Before you upload, confirm three things: the file is renamed with your own name, it runs without errors and plays a complete game (both a win and a loss) in the format shown above, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in this module's discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
