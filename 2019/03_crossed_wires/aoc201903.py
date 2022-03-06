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
    wire1, wire2 = data
    cross_sections = compute_covered(wire1).intersection(compute_covered(wire2))
    return min(sum(map(abs, cross_section)) for cross_section in cross_sections)


def compute_covered(wire_path) -> set:
    location = (0, 0)
    covered = set()  # Set of coordinates covered by wire
    for direction, distance in wire_path:
        if direction == 'R':
            for _ in range(distance):
                covered.add(location := (location[0] + 1, location[1]))
        elif direction == 'U':
            for _ in range(distance):
                covered.add(location := (location[0], location[1] + 1))
        elif direction == 'L':
            for _ in range(distance):
                covered.add(location := (location[0] - 1, location[1]))
        elif direction == 'D':
            for _ in range(distance):
                covered.add(location := (location[0], location[1] - 1))
    return covered



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
