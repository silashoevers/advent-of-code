import pathlib
import sys
from parse import compile
import numpy as np


def parse(puzzle_input):
    """Parse input"""
    p = compile("{} {:d},{:d} through {:d},{:d}")
    return [p.parse(line).fixed for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    grid = np.zeros((1000, 1000), dtype=bool)
    for instr, x1, y1, x2, y2 in data:
        if instr == "turn on":
            grid[y1:y2+1, x1:x2+1] = True
        elif instr == "turn off":
            grid[y1:y2+1, x1:x2+1] = False
        elif instr == "toggle":
            grid[y1:y2+1, x1:x2+1] = ~grid[y1:y2+1, x1:x2+1]
    return grid.sum()


def part2(data):
    """Solve part 2"""
    grid = np.zeros((1000, 1000), dtype=int)
    for instr, x1, y1, x2, y2 in data:
        section = grid[y1:y2+1, x1:x2+1]
        if instr == "turn on":
            section += 1
        elif instr == "turn off":
            section -= 1
            section[section < 0] = 0  # Fix values that have dropped below zero
        elif instr == "toggle":
            section += 2
    return grid.sum()


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


def main():
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))


if __name__ == "__main__":
    main()
