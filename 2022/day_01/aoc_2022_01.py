puzzle_input = 'input.txt'

# Parse & preprocess input
with open(puzzle_input) as f:
    split_per_elf = f.read().split('\n\n')
    split_within_elf = map(lambda l: l.split(), split_per_elf)
    to_int = list(map(lambda elf: list(map(int, elf)), split_within_elf))

# Part 1
print(max(map(sum, to_int)))

# Part 2
print(sum(sorted(map(sum, to_int), reverse=True)[:3]))
