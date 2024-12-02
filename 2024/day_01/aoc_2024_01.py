from aocd import get_data
from collections import Counter

def parse(puzzle_input):
    """Parse input."""
    list1 = []
    list2 = []
    for line in puzzle_input.splitlines():
        item1, item2 = line.split('   ')  # Why does \s\s\s not work?
        list1.append(int(item1))
        list2.append(int(item2))
    return list1, list2

def part1(data):
    """Solve part 1."""
    list1, list2 = data
    sorted_list1, sorted_list2 = sorted(list1), sorted(list2)
    total_distance = 0
    for item1, item2 in zip(sorted_list1, sorted_list2):
        total_distance += abs(item1 - item2)
    return total_distance

def part2(data):
    """Solve part 2."""
    list1, list2 = data
    counted_list2 = Counter(list2)
    total_sim_socre = 0
    for item in list1:
        total_sim_socre += item * counted_list2[item]
    return total_sim_socre


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year= "2024"
    day= "01"
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=int(year), day=int(day))
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))