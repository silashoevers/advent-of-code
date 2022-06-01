import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [(move[0], int(move[1:])) for move in puzzle_input.split(', ')]


def part1(data):
    """Solve part 1"""
    x, y, facing = 0, 0, 0  # 0 is North, 1 is East, etc.
    for turn, distance in data:
        # Apply rotation
        if turn == 'L':
            facing -= 1
        elif turn == 'R':
            facing += 1
        facing %= 4
        # Move
        if facing == 0:
            y += distance
        elif facing == 1:
            x += distance
        elif facing == 2:
            y -= distance
        elif facing == 3:
            x -= distance
    return abs(x) + abs(y)


def part2(data):
    """Solve part 2"""
    paths = set()



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
