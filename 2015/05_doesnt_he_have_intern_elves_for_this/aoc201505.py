import pathlib
import sys

vowels = "aeiou"


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1"""
    nice_string_count = 0
    for string in data:
        if sum(map(lambda c: c in vowels, string)) < 3:
            continue
        if sum(map(lambda a: a[0] == a[1], zip(string, string[1:]))) == 0:
            continue
        for naughty_substring in ["ab", "cd", "pq", "xy"]:
            if naughty_substring in string:
                break
        else:
            nice_string_count += 1
    return nice_string_count


def part2(data):
    """Solve part 2"""
    nice_string_count = 0
    for string in data:
        condition_1 = False
        condition_2 = False
        pairs = set()
        parked = None
        for a, b, c in zip(string, string[1:], string[2:]):
            # Condition 1
            if parked is not None:
                pairs.add(parked)
            parked = (a, b)
            if (b, c) in pairs:
                condition_1 = True

            # Condition 2
            if a == c:
                condition_2 = True
        if condition_1 and condition_2:
            nice_string_count += 1
    return nice_string_count


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
