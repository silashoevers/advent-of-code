from aocd import get_data
import itertools

def parse(puzzle_input):
    """Parse input."""
    all_rucksacks = []
    for rucksack in puzzle_input.splitlines():
        hw = len(rucksack) // 2  # Halfway index
        first_compartment, second_compartment = rucksack[:hw], rucksack[hw:]  # Thank go to slices
        all_rucksacks.append((first_compartment, second_compartment))
    return all_rucksacks

def item_priority(item):
    if item.islower():
        return ord(item) - 96
    elif item.isupper():
        return ord(item) - 38

def part1(data):
    """Solve part 1."""
    total_priority = 0
    for first_compartment, second_compartment in data:
        shared_items = list(set(first_compartment) & set(second_compartment))
        shared_item = shared_items[0]
        total_priority += item_priority(shared_item)
    return total_priority


def part2(data):
    """Solve part 2."""
    total_priority = 0
    for group in itertools.batched(data, 3):
        elf1, elf2, elf3 = map(lambda elf: set(''.join(elf)), group)  # Need to join left and right rucksack: Shot ourselves in the foot with that one
        group_badge = elf1.intersection(elf2, elf3).pop()
        total_priority += item_priority(group_badge)
    return total_priority


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year= 2022
    day= int("03")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))