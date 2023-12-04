import re

symbol_reg_escaped = re.escape("@#*/%$=+-&")
symbol_pattern = re.compile(f"[{symbol_reg_escaped}]")


def is_number_adjacent_to_symbol(start, end, row, matrix, m, n):
    # Normalize indices to not go out of bounds with slicing
    adjacent = False
    if row - 1 < 0:
        top = 0
    else:
        top = row - 1
    bottom = row + 2
    if start - 1 < 0:
        left = 0
    else:
        left = start - 1
    right = end + 1
    for section in matrix[top:bottom]:
        section = section[left:right]
        if symbol_pattern.search(section):
            adjacent = True
    return adjacent


puzzle_input_path = "input.txt"

with open(puzzle_input_path) as f:
    puzzle_input = f.read().splitlines()  # Remove newlines

m = len(puzzle_input)     # Amount of rows in the schema matrix
n = len(puzzle_input[0])  # Amount of columns in the schema matrix

number_reg = "[0-9]+"
number_pattern = re.compile(number_reg)

result = 0
for row, line in enumerate(puzzle_input):
    numbers = number_pattern.finditer(line)
    for number in numbers:
        start, end = number.span()
        if is_number_adjacent_to_symbol(start, end, row, puzzle_input, m, n):
            result += int(number.group())

# Part 2
# Copy pasta from Part 1
number_locations = []  # [(number, start, end, row)]
for row, line in enumerate(puzzle_input):
    numbers = number_pattern.finditer(line)
    for number in numbers:
        start, end = number.span()
        number_locations.append((int(number.group()), start, end, row))

# Iterate over all gears
result = 0
for row, line in enumerate(puzzle_input):
    for column, symbol in enumerate(line):
        if symbol == "*":
            adjacent_numbers = []
            for number_tup in number_locations:
                number, start, end, number_row = number_tup
                if row in [number_row - 1, number_row, number_row + 1] and column >= start - 1 and column <= end:
                    adjacent_numbers.append(number_tup)
            adjacent_numbers = set(adjacent_numbers)
            if len(adjacent_numbers) == 2:
                adjacent_numbers = list(adjacent_numbers)
                result += adjacent_numbers[0][0] * adjacent_numbers[1][0]
                print(adjacent_numbers)
print(result)