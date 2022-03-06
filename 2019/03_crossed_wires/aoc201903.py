import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return tuple([parse_wire_jump(jump) for jump in wire.split(',')] for wire in puzzle_input.split('\n'))


def parse_wire_jump(jump):
    """Turns 'R100' in ('R', 100)"""
    return jump[0], int(jump[1:])


def part1(data):
    """Solve part 1"""


def part2(data):
    """Solve part 2"""


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
