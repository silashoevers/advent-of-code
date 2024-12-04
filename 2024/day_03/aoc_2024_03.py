from aocd import get_data
import re

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input  # Parsing is the puzzle

def part1(data):
    """Solve part 1."""
    total = 0
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    valid_muls = re.finditer(pattern, data)
    for nums in valid_muls:
        num1, num2 = map(int, nums.groups())
        total += num1 * num2
    return total

def part2(data):
    """Solve part 2."""
    pattern = re.compile(r"(mul)\((\d+),(\d+)\)|(don't)\(\)|(do)\(\)")
    instructions = re.findall(pattern, data)
    total = 0
    mul_on = True
    for instruction in instructions:
        if 'mul' in instruction:
            if mul_on:
                num1, num2 = map(int, instruction[1:3])
                total += num1 * num2
        elif "don't" in instruction:
            mul_on = False
        elif 'do' in instruction:
            mul_on = True
    return total

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2024
    day = int("03")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))