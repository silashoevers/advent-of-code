from aocd import get_data
import numpy as np
import regex as re

def parse(puzzle_input):
    """Parse input."""
    return np.array([list(line) for line in puzzle_input.splitlines()])

def count_xmas(lines):
    """
    Counts how many times 'XMAS' occurs in the provided lines (list of lists of characters),
    both in order and in reverse order
    """
    pattern = re.compile(r'XMAS|SAMX')
    count = 0
    for line in lines:
        line = ''.join(line)
        count += len(pattern.findall(line, overlapped=True))
    return count

def part1(data):
    """Solve part 1."""
    height, width = data.shape
    xmas_count = 0

    # Go through all possible directions ("scanning lines")
    xmas_count += count_xmas([data[i, :] for i in range(height)])  # Horizontal
    xmas_count += count_xmas([data[:, j] for j in range(width)])   # Vertical
    xmas_count += count_xmas([np.diag(data, k=offset) for offset in range(-height+1, height)])  # Diagonal, left to right

    # Diagonal, right to left
    data_fliplr = np.fliplr(data)  # Flip data horizontally
    xmas_count += count_xmas([np.diag(data_fliplr, k=offset) for offset in range(-height+1, height)])

    return xmas_count

def find_MAS_or_SAM(array):
    """Per left-right diagonal in 2D array, return all matches of MAS or SAM as (offset, index_of_A)"""
    height, width = array.shape
    pattern = re.compile(r'MAS|SAM')
    matches = []
    for offset in range(-height+1, height):
        matches_in_diag = pattern.finditer(''.join(np.diag(array, k=offset)), overlapped=True)
        matches.extend([(offset, match_in_diag.span()[0]+1) for match_in_diag in matches_in_diag])
    return matches

def part2(data):
    """Solve part 2."""
    # TODO: Rewrite using index iteration over center square
    height, width = data.shape

    left_right_matches = find_MAS_or_SAM(data)
    coordinates_left_right_matches = []
    # Compute all (i,j) coordinates of As that are part of a MAS or SAM
    for match in left_right_matches:
        offset, index = match
        # Big maths to revert diagonal coordinate back to regular coordinate
        i = index + abs(min(0, offset))
        j = index + max(0, offset)
        coordinates_left_right_matches.append((i, j))

    right_left_matches = find_MAS_or_SAM(np.fliplr(data))
    coordinates_right_left_matches = []
    for match in right_left_matches:
        offset, index = match
        i = index + abs(min(0, offset))
        j = (width - 1) - (index + max(0, offset))
        coordinates_right_left_matches.append((i, j))

    return len(set(coordinates_left_right_matches) & set(coordinates_right_left_matches))


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2024
    day = int("04")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))