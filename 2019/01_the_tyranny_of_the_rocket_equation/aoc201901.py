import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(mass) for mass in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    return sum([mass // 3 - 2 for mass in data])


def part2(data):
    """Solve part 2"""
    total_fuel = 0
    for mass in data:
        while (mass := mass // 3 - 2) > 0:
            total_fuel += mass
    return total_fuel


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
