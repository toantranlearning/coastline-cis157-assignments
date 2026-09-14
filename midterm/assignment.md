# Midterm Project: Hunt the Intruder

## What you are doing, and why

You will build a complete console game (a battleship-style hunt on a 3x3 grid) using everything from the first half of this course working together in one program: nested lists for the grid, functions to organize the work, a `while` loop to run the game, conditionals to validate input and resolve each move, booleans to track the outcome, and f-strings to report status. Every weekly assignment so far exercised one or two of these at a time; the midterm is where they have to cooperate. This project is worth **60 points**, roughly double a weekly assignment, and the page below is proportionally fuller: read all of it before you write a line of code.

## Scenario

The Harborwatch Security team runs a tabletop exercise every quarter to keep hunt instincts sharp, and your lead has asked you to build this year's edition. The setup: an intruder is hiding on one host in a client's 3x3 network grid, and the analyst playing the exercise has a limited budget of probes to find them. Each probe checks one host and comes back clean or finds the intruder. Four probes, nine hosts: the analyst who probes carelessly runs out of budget and loses the intruder. Your program is the exercise: it hides the intruder, draws the grid, takes the probes, and calls the result.

## What you are given

- [Starter file](midterm_firstname_lastname.py). A header docstring to complete and the same three parts as every assignment: a complete, working board-display function to read and run, a banner with a probe-budget constant to modify, and the rest of the game (two more functions and the main program) to create from full line-by-line pseudocode, seven steps in all, ordered so that each one builds on the previous.

## Instructions

Every assignment in this course follows the same three-step rhythm: **read** working code, **modify** working code, then **create** your own from the pseudocode in the starter. The midterm keeps the rhythm. It is just bigger at the create end: Part 3 is seven pseudocode steps instead of one, and it is where most of the 60 points live.

1. Download the starter file and rename it with your own name, all lowercase: `midterm_jane_doe.py` for Jane Doe. Keep the `midterm_` prefix.
2. Read the whole starter before you write anything, so you can see how the three parts fit together into one game.
3. **Read.** Part 1 is a complete function, `display_board(board)`, plus two demo lines that draw a mid-game sample board. Run the program and study the grid: column numbers across the top, row numbers down the left side, and one character per host: `.` for an unprobed host, `o` for a host probed and found clean, `X` for the intruder once found. This function already matches the board format in the expected output below exactly, including the `+---+` grid lines; the rest of the game calls it as-is.
4. **Modify.** Part 2 prints the exercise banner, but the starter still announces last year's probe budget. Change `PROBES` from `5` to `4`, run again, and confirm the banner reports 4 probes. Change only the constant: the banner's f-string and the rest of the game read `PROBES`, so the whole program follows.
5. **Create.** Part 3 is the rest of the game, in seven steps, each with complete line-by-line pseudocode. Translate each line rather than inventing your own structure. Build one step at a time and run after every step, not just at the end. Step 3.1 deletes Part 1's two demo lines: the finished game builds its own board and must not print the sample grid.
6. Steps 3.2 and 3.3 are the game's other two functions. First one input-validation function, used for both the row and the column: it takes a label (`"row"` or `"column"`), prompts with it, and keeps asking until it gets an integer from 0 to 2: `try`/`except` for input that is not a number, a conditional for numbers off the grid. Invalid input never costs a probe; the function simply explains the problem and asks again. Then a probe-resolution function: on a hit it marks the host `X` and returns `True`, otherwise it marks the host `o` and returns `False`. This function is where the game's booleans live.
7. Step 3.4 is the opening: ask for the client **case number** (an integer: validate it the same `try`/`except` way). The intruder's position is derived from it: `position = case_number % 9`, then `row = position // 3` and `column = position % 3`. This is a deliberate trick, and the page is being honest with you about it: real programs would place the intruder randomly, but Python's `random` module is not covered until M09, so until then we squeeze an unpredictable-feeling position out of whatever number the user types. Try a few case numbers and notice how the position jumps around. When you meet `random` in M09, you will retire this trick.
8. Steps 3.5 through 3.7 are the game itself. Build the board as a **list of three lists**, every host starting as `"."`, with the game state beside it: `PROBES` probes remaining and a boolean, `False` to start, recording whether the intruder has been found. Then the main `while` loop, one turn per pass: display the board, print an f-string status line (probes remaining, hosts cleared: count the `o` marks), get a row and a column with your validation function. An already-probed host costs no probe. Say so and go around again; a real analyst does not pay to re-check a host they already cleared. Otherwise spend one probe and resolve it with your probe-resolution function. Finally the ending: display the final board, then the win line, or the lose line revealing the intruder's host. Match both lines to the expected output exactly.
9. Play at least three full games: one you win, one you lose, and one where you feed the program garbage (letters, numbers off the grid, hosts you already probed) and confirm none of it costs a probe or crashes the program.
10. Complete the header at the top of the file: `NAME`, `DATE`, `DESCRIPTION`, and the `REFLECTION` slot. Every program you submit in this course carries this header; professionals sign their work, and so do you.

You do not need tuples, dictionaries, classes, file handling, or the `random` module for this project. If you have already met tuples or dictionaries and want to use them, that is allowed, but the whole game builds cleanly without them.

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

The session below used case number `2026` and probes at row 1 column 1, an off-grid row of 5, row 0 column 0 (twice: the second one is the already-probed case), and row 0 column 1. Your session will differ (the case number, the intruder's position, and the moves are the player's), but the board format, the prompts, the status lines, and the win and lose lines must match this exactly, and the banner must report the 4-probe budget from your Part 2 change. The lose line, not shown in this winning session, is: `Out of probes. The intruder was hiding on host (row, column). You lose.` with the real coordinates filled in.

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

Before you upload, confirm three things: the file is renamed with your own name, it runs in Thonny without errors and plays a complete game (win and lose) in the format shown above, and every header field contains your text, not the placeholder text.

If you get stuck, post a question in the weekly discussion, but share no more than three lines of your code there, so your post is a question and not a solution.
