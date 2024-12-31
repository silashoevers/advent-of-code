from aocd import get_data
import numpy as np

def parse(puzzle_input):
    """Parse input."""
    return np.array([[char for char in line]for line in puzzle_input.splitlines()])

class Guard:
    """Keeps track of position and direction of guard and provides helper functions for getting and updating"""
    def __init__(self, start_i, start_j, start_dir):
        self.current_i = start_i
        self.current_j = start_j
        self.current_dir = start_dir

    def get_next_pos(self):
        match self.current_dir:
            case 0:
                return self.current_i - 1, self.current_j
            case 1:
                return self.current_i, self.current_j + 1
            case 2:
                return self.current_i + 1, self.current_j
            case 3:
                return self.current_i, self.current_j - 1

    def get_current_pos(self):
        return self.current_i, self.current_j

    def turn(self):
        self.current_dir = (self.current_dir + 1) % 4

    def move_forward(self):
        match self.current_dir:
            case 0:
                self.current_i, self.current_j = self.current_i - 1, self.current_j
            case 1:
                self.current_i, self.current_j = self.current_i, self.current_j + 1
            case 2:
                self.current_i, self.current_j = self.current_i + 1, self.current_j
            case 3:
                self.current_i, self.current_j = self.current_i, self.current_j - 1

def part1(data):
    """Solve part 1."""
    # FOR DEBUGGING
    trail = []

    # Assume that guard always starts facing north
    # Coordinate system throughout solution is matrix based (0,0) = top left
    visited = np.full_like(data, 0, dtype=int)
    i, j = np.where(data == '^')
    guard_i, guard_j = i[0], j[0]
    guard_dir = 0  # direction: 0 = North, 1 = East, 2 = South, 3 = West
    guard = Guard(guard_i, guard_j, guard_dir)
    visited[guard_i, guard_j] = 1
    while True:
        # Check if guard can move on to next position
        next_i, next_j = guard.get_next_pos()
        if next_i < 0 or next_j < 0 or next_i >= data.shape[0] or next_j >= data.shape[1]:
            break
        # Will guard go out of bounds?
        next_content = data[next_i, next_j]
        if next_content == '#':  # Block in the way
            guard.turn()
        else:  # At this point we assume the way is free
            guard.move_forward()
            visited[next_i, next_j] = visited[next_i, next_j] or 1
        trail.append((next_i, next_j))

    total_visited = np.sum(visited)
    return total_visited


def part2(data):
    """Solve part 2."""
    obstacle_locations = np.where(data == '#')


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2024
    day = int("06")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))