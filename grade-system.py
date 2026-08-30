def get_grade(mark):
    """Return the letter grade for a given numeric mark (0-100 inclusive)."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def get_valid_mark():
    """Prompt the user until a valid numeric mark between 0 and 100 is entered."""
    while True:
        raw = input("Enter a mark (0-100): ").strip()

        try:
            mark = float(raw)
        except ValueError:
            print(f"Invalid input: '{raw}' is not a number. Please try again.")
            continue

        if mark < 0 or mark > 100:
            print(f"Invalid mark: {mark} is outside the 0-100 range. Please try again.")
            continue

        return mark


def main():
    mark = get_valid_mark()
    grade = get_grade(mark)

    # Show mark as an int if it has no fractional part, otherwise keep decimals
    display_mark = int(mark) if mark == int(mark) else mark
    print(f"Mark entered: {display_mark} -> Grade: {grade}")


if __name__ == "__main__":
    main()