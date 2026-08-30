# Student Grade Calculator

A collection of Python scripts that convert numeric marks into letter grades. The project has three variants, ranging from a simple single-mark terminal tool to a full Excel-in, Excel-out grading pipeline for multiple students and subjects.

Built with pure Python and [`openpyxl`](https://openpyxl.readthedocs.io/) (for the Excel-based variants) viz., no other frameworks or dependencies.

## Grading Scale

All three variants use the same grading scale, applied to a mark (or average mark) out of 100:

| Mark / Average | Grade |
|-----------------|-------|
| 90 – 100        | A     |
| 80 – 89         | B     |
| 70 – 79         | C     |
| 60 – 69         | D     |
| Below 60        | E     |

Boundaries are inclusive say., exactly 90 is an A, exactly 80 is a B, and so on.

## Requirements

- Python 3.8+
- [`openpyxl`](https://pypi.org/project/openpyxl/) — required for **Variant 2** and **Variant 3** only

Install `openpyxl`:
```bash
pip install openpyxl
```

> On newer macOS/Homebrew Python setups, you may need:
> ```bash
> pip install openpyxl --break-system-packages
> ```
> Or use a virtual environment:
> ```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install openpyxl
> ```

---

## Variant 1: Single Mark → Grade (Terminal Input)

**File:** `grade_system.py`

The simplest version. Prompts the user to type in one mark (0–100) and prints the matching letter grade. No files involved — pure terminal input/output.

### Usage
```bash
python3 grade_system.py
```

### Example
```
Enter a mark (0-100): 88
Mark entered: 88 -> Grade: B
```

Invalid input (non-numeric, or outside 0–100) is caught and the user is re-prompted rather than the program crashing.

---

## Variant 2: Excel Input → Terminal Output

**File:** `grade_system_usingfile.py`

Reads student names and subject marks from an Excel file, then prints each student's name, subject marks, average, and grade to the terminal. Nothing is written back to a file viz., output is terminal-only.

### Input file format

First row = headers, first column = student name. Any number of subject columns is supported.

| Name    | Maths | Science | English | History |
|---------|-------|---------|---------|---------|
| Alice   | 95    | 88      | 91      | 85      |
| Bob     | 72    | 68      | 75      | 70      |

By default the script looks for `sample_marks.xlsx` in the same folder

### Usage
```bash
python3 grade_from_excel.py
```

### Example output
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
```

---

## Variant 3: Excel Input → Excel Output

**File:** `grade_system_io&opasfile.py`

Same as Variant 2, but also saves the full results: name, subject marks, total, average, and grade into a new Excel file, in addition to printing to the terminal.

### Input file format

Same as Variant 2 — `sample_marks.xlsx` by default.

### Usage
```bash
python3 grade_system_io&opasfile.py
```

This will:
- Print the report to the terminal (same as Variant 2)
- Create/overwrite `grade_report.xlsx` in the same folder

### Example output file (`grade_report.xlsx`)

| Name  | Maths | Science | English | History | Total | Average | Grade |
|-------|-------|---------|---------|---------|-------|---------|-------|
| Alice | 95    | 88      | 91      | 85      | 359   | 89.75   | B     |
| Bob   | 72    | 68      | 75      | 70      | 285   | 71.25   | C     |

---

## Project Structure

```
.
├── grade_system.py             # Variant 1: single mark, terminal only
├── grade_from_excel.py         # Variant 2: Excel input, terminal output
├── grade_from_excel_full.py    # Variant 3: Excel input, Excel output
├── sample_marks.xlsx           # Example input file (Variants 2 & 3)
├── grade_report.xlsx           # Generated output (Variant 3, created after running)
└── README.md
```

## Notes

- Make sure your terminal's current directory is the folder containing the script **and** the Excel file. Python looks for `sample_marks.xlsx` relative to where you run the command from, not where the script file lives.
- If you create your own `sample_marks.xlsx` in Excel or Numbers, save it explicitly as `.xlsx` format (Numbers in particular defaults to its own `.numbers` format).

## License

Feel free to use, modify, and share this project for learning or personal use.
