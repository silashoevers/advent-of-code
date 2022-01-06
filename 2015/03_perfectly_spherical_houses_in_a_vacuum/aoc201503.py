import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input  # No sanitization needed


def part1(data):
    """Solve part 1"""
    santa = Santa()
    visited = {(0, 0)}
    for move in data:
        visited.add(santa.move(move))
    return len(visited)


def part2(data):
    """Solve part 2"""
    santas = [Santa(), Santa()]  # Both the real and robot santa
    turn = 0
    visited = {(0, 0)}
    for move in data:
        visited.add(santas[turn].move(move))
        turn = (turn + 1) % 2
    return len(visited)


class Santa:
    def __init__(self):
        self.x, self.y = 0, 0

    def move(self, move):
        """Takes move character: ^, >, v, < and returns resulting coordinates"""
        if move == '^':
            self.y += 1
        elif move == '>':
            self.x += 1
        elif move == 'v':
            self.y -= 1
        elif move == '<':
            self.x -= 1
        return self.x, self.y


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
