from itertools import combinations

from aocd import get_data
import numpy as np

def parse(puzzle_input):
    """Parse input."""
    return np.array([[char for char in line] for line in puzzle_input.splitlines()])

def within_np_bounds(row, column, np_array):
    """For a 2D numpy array, checks whether the given row and column index are within the array shape"""
    return 0 <= row < np_array.shape[0] and 0 <= column < np_array.shape[1]

def part1(data):
    """Solve part 1."""
    # Collect coordinates of same type of antenna
    antenna_types = set([data[*location] for location in np.argwhere(data != '.')])
    antennas = {antenna_type: [location for location in np.argwhere(data == antenna_type)] for antenna_type in antenna_types}
    antinode_locations = np.full_like(data, fill_value=False, dtype=bool)
    for antenna_locations in antennas.values():
        for antenna_1, antenna_2 in combinations(antenna_locations, 2):
            antinodes = [antenna_1 - antenna_2 + antenna_1, antenna_2 - antenna_1 + antenna_2]
            for row, column in antinodes:
                if within_np_bounds(row, column, data):
                    antinode_locations[row][column] = antinode_locations[row][column] or True
    return antinode_locations.sum()

def part2(data):
    """Solve part 2."""
    antenna_types = set([data[*location] for location in np.argwhere(data != '.')])
    antennas = {antenna_type: [location for location in np.argwhere(data == antenna_type)] for antenna_type in antenna_types}
    antinode_locations = np.full_like(data, fill_value=False, dtype=bool)
    for antenna_locations in antennas.values():
        for antenna_1, antenna_2 in combinations(antenna_locations, 2):
            # Projection from antenna_1 towards antenna_2
            diff_vector = antenna_2 - antenna_1
            scalar = 1
            next_possible_antinode_point = antenna_1 + scalar * diff_vector
            while within_np_bounds(*next_possible_antinode_point, data):
                next_antinode_row, next_antinode_column = next_possible_antinode_point
                antinode_locations[next_antinode_row][next_antinode_column] = antinode_locations[next_antinode_row][next_antinode_column] or True
                scalar += 1
                next_possible_antinode_point = antenna_1 + scalar * diff_vector

            # Projection from antenna_2 towards antenna_1
            diff_vector = antenna_1 - antenna_2
            scalar = 1
            next_possible_antinode_point = antenna_2 + scalar * diff_vector
            while within_np_bounds(*next_possible_antinode_point, data):
                next_antinode_row, next_antinode_column = next_possible_antinode_point
                antinode_locations[next_antinode_row][next_antinode_column] = antinode_locations[next_antinode_row][next_antinode_column] or True
                scalar += 1
                next_possible_antinode_point = antenna_2 + scalar * diff_vector
    return antinode_locations.sum()

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2024
    day = int("08")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))