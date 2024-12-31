from aocd import get_data
import time
from itertools import batched
import numpy as np


def parse(puzzle_input):
    """Parse input. Represent empty spaces by None."""
    return list(map(int, puzzle_input.strip()))

def create_individual_blocks(data):
    """Goes from [1,2,3,4,5] to [0..111....22222]"""
    result = []
    head, tail = data[:-1], data[-1]
    for file_id, (num_files, num_free) in enumerate(batched(head, 2)):
        result.extend([file_id]*num_files)
        result.extend([None]*num_free)
    result.extend([file_id + 1] * tail)
    return result

def compute_filesystem_checksum(filesystem):
    result = 0
    for index, file in enumerate(filesystem):
        if file is not None:
            result += index * file
    return result

def part1(data):
    """Solve part 1."""
    # Create list of file ids and free spaces
    indvididual_blocks = create_individual_blocks(data)
    file_block_stack = [(file_index, file_id) for file_index, file_id in enumerate(indvididual_blocks) if file_id is not None]

    while True:
        file_index, file_id = file_block_stack.pop()  # File to be moved
        i_next_empty = indvididual_blocks.index(None)  # Index of next empty space in filesystem
        if i_next_empty > file_index:
            break
        else:
            indvididual_blocks[i_next_empty], indvididual_blocks[file_index] = indvididual_blocks[file_index], None
    return compute_filesystem_checksum(indvididual_blocks)

# TODO: Fix current runtime: 138.25723266601562s
# 6330095022244 (too low)
def part2(data):
    """Solve part 2."""
    file_stack = []  # Stack of files to be moved
    space_table_shape = len(data), 3  # Columns: content, start_i and size
    space_table = np.ndarray(space_table_shape, dtype=int)
    next_free_index = 0
    for i, size in enumerate(data):
        if i % 2 == 0:  # File
            file_id = i // 2
            space_table[i] = [file_id, next_free_index, size]
            file_stack.append([file_id, next_free_index, size])
        else:  # Empty space
            space_table[i] = [-1, next_free_index, size]
        next_free_index += size
    while len(file_stack) > 0:
        file_id, file_index, file_size = file_stack.pop()
        # Is there a space free?
        try:
            np.where(space_table[:,0] < file_index)
    return

def consolidate_empty_space(file_system):
    # Remove all zero-length empty spaces
    file_system = file_system[file_system[:,2] != 0]
    # Merge consecutive

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    # Parse puzzle input. Same input shared by part 1 and 2 solvers
    data = parse(puzzle_input)

    # Part 1
    before = time.time()
    solution1 = part1(data)
    after = time.time()
    print(f"## Part 1\n{solution1}\n{after - before}s\n")

    # Part 2
    before = time.time()
    solution2 = part2(data)
    after = time.time()
    print(f"## Part 2\n{solution1}\n{after - before}s")

    return

if __name__ == "__main__":
    year = 2024
    day = 9
    print(f"# Year {year}, day {day}")
    puzzle_input = get_data(year=year, day=day)
    solve(puzzle_input)