import pathlib
import sys
import parse


def parse(puzzle_input):
    """Parse input"""
    return [
        tuple(map(int, dimensions.split('x')))
        for dimensions in puzzle_input.split("\n")
    ]


def part1(data):
    """Solve part 1"""
    total = 0
    for l, w, h in data:
        faces = [l*w, w*h, h*l]
        total += sum(map(lambda x: x*2, faces)) + min(faces)
    return total


def part2(data):
    """Solve part 2"""
    total = 0
    for l, w, h in data:
        total += l * w * h + min([2*l+2*w, 2*w+2*h, 2*l+2*h])
    return total


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
