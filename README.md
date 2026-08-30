# Student Grade Calculator

A lightweight Python script that reads student names and subject marks from an Excel spreadsheet, calculates each student's total and average marks, assigns a letter grade based on a standard grading scale, and writes a clean summary report back out to a new Excel file.

Built with pure Python logic and [`openpyxl`](https://openpyxl.readthedocs.io/) — no frameworks, no other dependencies.

## Features

- Reads student marks directly from an `.xlsx` file
- Supports any number of subjects (just add more columns)
- Calculates each student's **total** and **average** mark
- Assigns a **letter grade (A–E)** based on the average
- Prints a readable report to the terminal
- Exports the full results to a new Excel file (`grade_report.xlsx`)

## Grading Scale

| Average Mark | Grade |
|--------------|-------|
| 90 – 100     | A     |
| 80 – 89      | B     |
| 70 – 79      | C     |
| 60 – 69      | D     |
| Below 60     | E     |

Boundaries are inclusive — an average of exactly 90 is an A, exactly 80 is a B, and so on.

## Requirements

- Python 3.8+
- [`openpyxl`](https://pypi.org/project/openpyxl/)

## Setup

Clone the repo, then install the one dependency:

```bash
pip install openpyxl
```

> On newer macOS/Homebrew Python setups, you may need:
> ```bash
> pip install openpyxl --break-system-packages
> ```
> Or, better, use a virtual environment:
> ```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install openpyxl
> ```

## Input File Format

The script expects an Excel file (default: `sample_marks.xlsx`) in the same folder, with the **first row as headers** and the **first column as student names**:

| Name    | Maths | Science | English | History |
|---------|-------|---------|---------|---------|
| Alice   | 95    | 88      | 91      | 85      |
| Bob     | 72    | 68      | 75      | 70      |
| Charlie | 55    | 62      | 48      | 58      |

You can add or remove subject columns freely — the script adapts automatically based on the header row.

## Usage

1. Place your marks spreadsheet in the same folder as the script, named `sample_marks.xlsx` (or edit the `filename` variable in the script to match your file name).
2. Run the script:

```bash
python3 grade_calculator.py
```

3. The results are:
   - Printed to the terminal
   - Saved to a new file, `grade_report.xlsx`, in the same folder

### Example terminal output

```
STUDENT GRADE REPORT
========================================

Alice
  Maths: 95
  Science: 88
  English: 91
  History: 85
  Total: 359
  Average: 89.75
  Grade: B

Bob
  Maths: 72
  Science: 68
  English: 75
  History: 70
  Total: 285
  Average: 71.25
  Grade: C

Saved results to grade_report.xlsx
```

### Example output file (`grade_report.xlsx`)

| Name  | Maths | Science | English | History | Total | Average | Grade |
|-------|-------|---------|---------|---------|-------|---------|-------|
| Alice | 95    | 88      | 91      | 85      | 359   | 89.75   | B     |
| Bob   | 72    | 68      | 75      | 70      | 285   | 71.25   | C     |

## Project Structure

```
.
├── grade_calculator.py   # Main script
├── sample_marks.xlsx     # Example input file
├── grade_report.xlsx     # Generated output (created after running the script)
└── README.md
```

## License

Feel free to use, modify, and share this project for learning or personal use.
