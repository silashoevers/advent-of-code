import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data):
    """Solve part 1"""
    floor = 0
    for instruction in data:
        if instruction == "(":
            floor += 1  # Go up a floor
        elif instruction == ")":
            floor -= 1  # Go down a floor
    return floor


def part2(data):
    """Solve part 2"""
    floor = 0
    for index, instruction in enumerate(data):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        if floor == -1:
            return index + 1


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
