from aocd import get_data

def parse(puzzle_input):
    """Parse input."""
    result = []
    for pair in puzzle_input.splitlines():
        result.append(tuple([tuple(map(int, elf.split('-'))) for elf in pair.split(',')]))
    return result

def part1(data):
    """Solve part 1."""
    total = 0
    for elf1, elf2 in data:
        sections1, sections2 = set(range(elf1[0], elf1[1]+1)), set(range(elf2[0], elf2[1]+1))
        overlap = sections1.intersection(sections2)
        if overlap == sections1 or overlap == sections2:
            total += 1
    return total

def part2(data):
    """Solve part 2."""
    total = 0
    for elf1, elf2 in data:
        sections1, sections2 = set(range(elf1[0], elf1[1]+1)), set(range(elf2[0], elf2[1]+1))
        overlap = sections1.intersection(sections2)
        if len(overlap) > 0:
            total += 1
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2022
    day = int("04")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))