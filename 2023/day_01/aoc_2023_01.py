import regex as re  # To enable overlapped flag on re.findall

# Parse puzzle input
with open("input.txt") as f:
    puzzle_input = f.read().splitlines()

print(puzzle_input)

# Part 1
# Remove letters from strings
small_case_reg = "[a-z]"
number_reg = "[0-9]"
small_case_removed = list(map(lambda l: re.sub(small_case_reg, "", l), puzzle_input))

result = 0
for line in small_case_removed:
    result += int(line[0] + line[-1])

# Parse puzzle input (again)
with open("input.txt") as f:
    puzzle_input = f.read().splitlines()

# Part 2
str_to_int_replace_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

number_string_regex = re.compile("one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9")

result = 0
for line in puzzle_input:
    matches = re.findall(number_string_regex, line, overlapped=True)
    result += int(str_to_int_replace_dict.get(matches[0]) + str_to_int_replace_dict.get(matches[-1]))

print(result)
