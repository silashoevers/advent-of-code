import hashlib
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data):
    """Solve part 1"""
    for postfix in range(2000000):  # Arbitrary range to replace infinite loop of brute forcing
        message = data + str(postfix)
        if hashlib.md5(message.encode()).hexdigest()[:5] == "00000":
            return postfix
    return None


def part2(data):
    """Solve part 2"""
    for postfix in range(20000000):
        message = data + str(postfix)
        if hashlib.md5(message.encode()).hexdigest()[:6] == "000000":
            return postfix
    return None


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
