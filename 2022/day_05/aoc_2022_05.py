from aocd import get_data
import re

# TODO: Can't rely on spaces
def parse(puzzle_input):
    """Parse input."""
    starting_layout, instructions = puzzle_input.split('\n\n')

    # Parse starting stack layout
    starting_layout = starting_layout.split('\n')[:-1]  # The stack indices are inferred some other way, so we can drop them
    nr_stacks = (len(starting_layout[0]) + 1) // 4  # Neat trick to infer number of stacks

    stacks = [[] for _ in range(nr_stacks)]
    pattern = re.compile(r'\[(.)\]')
    for layer in reversed(starting_layout): # Build stacks from bottom to top
        for match in pattern.finditer(layer):
            stack_index = match.span()[0] // 4  # Boxes appear at a multiple of 4 offset. We shift index one down.
            crate_content = match.groups()[0]
            stacks[stack_index].append(crate_content)

    # Parse instructions
    pattern = re.compile(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)')
    parsed_instructions = [list(map(int, instruction)) for instruction in pattern.findall(instructions)]
    return stacks, parsed_instructions


def part1(data):
    """Solve part 1."""

def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2022
    day = int("05")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))