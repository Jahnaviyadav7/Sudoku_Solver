# Sudoku Solver

A desktop application for solving 4×4 (Shidoku) and 9×9 Sudoku puzzles, built with Python and CustomTkinter. Originally developed as an A-Level Computer Science NEA project, and now being actively improved.

---

## Features

- **Two grid modes** — 4×4 Shidoku for beginners and 9×9 Sudoku
- **Solve** — fully solves the puzzle using backtracking combined with human-logical techniques
- **Hint** — partially solves the grid one step at a time, so you can stay in control
- **Validity checker** — detects rule violations across rows, columns, and boxes before solving
- **Save** — exports the current grid state to a `.txt` file
- **Value differentiation** — user-entered numbers and computer-generated solutions are displayed in different colours
- **Help page** — in-application reference for all buttons and controls

---

## Demo

> *Screenshots coming soon*

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/Jahnaviyadav7/sudoku-solver.git
cd sudoku-solver
pip install -r requirements.txt
python Solver.py
```

### Requirements

```
customtkinter
```

---

## How to Use

1. Launch the application and choose **Shidoku (4×4)** or **Sudoku (9×9)** from the start screen
2. Click a cell, type a number, then press **Enter** to confirm the value.
   You can press Enter after each cell or after filling in multiple cells — both work fine.
3. Use the buttons on the right-hand panel:
   - **Check** — highlights any rule violations in your current grid
   - **Hint** — fills in one correct value to nudge you in the right direction
   - **Solve** — solves the entire puzzle instantly
   - **Save** — saves the grid to a `.txt` file on your device
4. Open the **Help** page (blue button) for a full button guide

**Note:** The Check button has a known issue and does not currently work as intended.
Validity checking is instead triggered automatically when you press Enter. This is noted in the roadmap to fix.

---

## How the Solver Works

The solver uses a hybrid approach combining logical techniques with backtracking:

1. **Validation** — checks rows, columns, and boxes for rule violations before attempting to solve
2. **Last Remaining Cell** — fills in any cell where only one value is possible
3. **Last Free Cell** — identifies the only empty cell remaining in a row, column, or box
4. **Last Possible Number** — finds the only remaining position a number can go in a given section
5. **Backtracking** — if logical techniques stall, the solver uses recursive backtracking to try candidate values and undo dead ends

This mirrors how a human solver would approach a puzzle — logic first, trial-and-error only when necessary.

---

## Project Background

This project was originally built as part of my **A-Level Computer Science NEA** (Non-Examined Assessment). 
The brief was to design, develop, and evaluate a working software solution — I chose a Sudoku solver because it let me explore both algorithm design and GUI development.

The project involved:
- Researching existing solvers and conducting a stakeholder interview to inform the design
- Iteratively building the GUI and solver logic
- Testing with both black-box test cases and real user feedback

Now in my first year of university, I'm revisiting the codebase to improve its structure and extend its features.

---

## Roadmap

These are the improvements I'm working on:

- [ ] Fix range errors
- [ ] Refactor into OOP — separate classes
- [ ] Split into multiple modules
- [ ] Add arrow key navigation across the grid
- [ ] Add candidate number display in each cell
- [ ] Add a solve timer
- [ ] Add a difficulty rating based on techniques required to solve
- [ ] Improve box boundary visibility in the 9×9 grid
- [ ] Add a colour theme selector
- [ ] Fix the Check button — move validity checking out of the Enter key handler and into its own function
- [ ] Provide sample sudokus

