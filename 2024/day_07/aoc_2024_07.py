from aocd import get_data

def parse(puzzle_input):
    """Parse input."""
    result = []
    for line in puzzle_input.splitlines():
        test_value, operands = line.split(': ')
        test_value, operands = int(test_value), list(map(int, operands.split(' ')))
        result.append((test_value, operands))
    return result

def is_solution_possible_part1(test_value, operands):
    if len(operands) == 1:
        return test_value == operands[0]
    else:  # Assuming len(operands) > 1
        last_operand, remaining_operands = operands[-1], operands[:-1]
        return is_solution_possible_part1(test_value - last_operand, remaining_operands) or is_solution_possible_part1(test_value / last_operand, remaining_operands)

def part1(data):
    """Solve part 1."""
    total = 0
    for test_value, operands in data:
        if is_solution_possible_part1(test_value, operands):
            total += test_value
    return total

def is_solution_possible_part2(test_value, operands):
    last_operand, remaining_operands = operands[-1], operands[:-1]
    if len(operands) == 1:
        return test_value == last_operand
    elif is_solution_possible_part2(test_value - last_operand, remaining_operands):
        return True
    elif test_value % last_operand == 0 and is_solution_possible_part2(test_value // last_operand, remaining_operands):
        return True
    # Test whether concatenation was a possibility
    test_value_str, last_operand_str = str(test_value), str(last_operand)
    if test_value_str.endswith(last_operand_str):
        test_value_stripped = test_value_str.removesuffix(last_operand_str)
    else:
        return False
    if len(test_value_stripped) > 0 and is_solution_possible_part2(int(test_value_stripped), remaining_operands):
        return True
    else:
        return False

def part2(data):
    """Solve part 2."""
    possible_test_values = []
    for test_value, operands in data:
        if is_solution_possible_part2(test_value, operands):
            possible_test_values.append(test_value)
    return sum(possible_test_values)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2024
    day = int("07")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solution_part_1, solution_part_2 = solve(puzzle_input)
    print(f"Part 1: {solution_part_1}")
    print(f"Part 2: {solution_part_2}")