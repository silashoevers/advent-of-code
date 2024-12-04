from aocd import get_data
import numpy as np
import re

def parse(puzzle_input):
    """Parse input."""
    return np.array([list(line) for line in puzzle_input.splitlines()])

def count_xmas(lines):
    """
    Counts how many times 'XMAS' occurs in the provided lines (list of lists of characters),
    both in order and in reverse order
    """
    pattern = re.compile(r'XMAS')
    count = 0
    for line in lines:
        line = ''.join(line)
        count += len(pattern.findall(line))
        count += len(pattern.findall(line[::-1]))
    return count

def part1(data):
    """Solve part 1."""
    height, width = data.shape
    xmas_count = 0

    # Go through all possible directions ("scanning lines") and per line check the reverse as well
    xmas_count += count_xmas([data[i, :] for i in range(height)])  # Horizontal
    xmas_count += count_xmas([data[:, j] for j in range(width)])   # Vertical
    xmas_count += count_xmas([data.diagonal(offset) for offset in range(-height+1, height)])  # Diagonal, left to right

    # Diagonal, right to left
    data_fliplr = np.fliplr(data)  # Flip data horizontally
    xmas_count += count_xmas([data_fliplr.diagonal(offset) for offset in range(-height+1, height)])

    return xmas_count



def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2024
    day = int("04")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))