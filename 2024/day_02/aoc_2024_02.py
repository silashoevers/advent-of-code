from aocd import get_data
import numpy as np

def parse(puzzle_input):
    """Parse input."""
    levels = puzzle_input.splitlines()
    levels_split = list(map(str.split, levels))
    levels_to_int = [list(map(int, level)) for level in levels_split]
    return levels_to_int

def is_safe(report):
    report = np.array(report)
    # Compute consecutive differences
    diffs = report[1:] - report[:-1]
    # Are all levels increasing or decreasing?
    if not (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)):
        return False
    abs_diffs = list(map(abs, diffs))
    if not (min(abs_diffs) >= 1 and max(abs_diffs) <= 3):
        return False
    return True

def part1(data):
    """Solve part 1."""
    total_safe_reports = 0
    for report in data:
        if is_safe(report):
            total_safe_reports += 1
    return total_safe_reports


def part2(data):
    """Solve part 2."""
    total_safe_reports = 0
    for report in data:
        if is_safe(report):
            total_safe_reports += 1
        else:
            for i in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(i)
                if is_safe(report_copy):
                    total_safe_reports += 1
                    break
    return total_safe_reports




def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year= 2024
    day= int("02")  # TODO: Fix this cursed mess
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))