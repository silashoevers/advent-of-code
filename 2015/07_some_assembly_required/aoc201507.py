import pathlib
import sys
from parse import compile


def parse(puzzle_input):
    """Parse input"""
    p = compile("{} -> {}")
    return [p.parse(line).fixed for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    # TODO Make independent of order of instructions
    signals = dict()
    for instr, output in data:
        # Determine how instruction needs to be interpreted
        if "AND" in instr:
            wire1, wire2 = instr.split(" AND ")
            signals.update({output: signals.get(wire1) & signals.get(wire2)})
        elif "OR" in instr:
            wire1, wire2 = instr.split(" OR ")
            signals.update({output: signals.get(wire1) | signals.get(wire2)})
        elif "LSHIFT" in instr:
            wire, shift = instr.split(" LSHIFT ")
            signals.update({output: signals.get(wire) << int(shift)})
        elif "RSHIFT" in instr:
            wire, shift = instr.split(" RSHIFT ")
            signals.update({output: signals.get(wire) >> int(shift)})
        elif "NOT" in instr:
            wire = instr[4:]
            signals.update({output: signals.get(wire) ^ 0b1111111111111111})
        else:
            signals.update({output: int(instr)})
    return signals


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
