from aocd import get_data
import re

def parse(puzzle_input):
    """Parse input."""
    pattern = re.compile(r'[0-9]+')


    elf_split = puzzle_input.split('\n\n')
    return [list(map(int, elf.split())) for elf in elf_split]

def part1(data):
    """Solve part 1."""
    return max(map(sum, data))

def part2(data):
    """Solve part 2."""
    result = sum(sorted(map(sum, data), reverse=True)[:3])
    return result

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year= "2022"
    day= "01"
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=int(year), day=int(day))
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))