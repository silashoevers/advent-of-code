from aocd import get_data

def parse(puzzle_input):
    """Parse input."""
    ordering_rules, updates = puzzle_input.split('\n\n')
    ordering_rules_parsed = [tuple(map(int, rule.split('|'))) for rule in ordering_rules.splitlines()]
    updates_parsed = [tuple(map(int, update.split(','))) for update in updates.splitlines()]
    return ordering_rules_parsed, updates_parsed

def is_update_correct(update, ordering_rules):
    index_dict = {page_nr: index for index, page_nr in enumerate(update)}
    update_correct = True
    for before, after in ordering_rules:
        if before in index_dict and after in index_dict:  # Are pages in ordering rule both present in our update?
            if not index_dict[before] < index_dict[after]:
                update_correct = False
                break
    return update_correct

def part1(data):
    """Solve part 1."""
    # Create entry to index dictionaries
    ordering_rules, updates = data
    result = 0
    for update in updates:
        update_correct = is_update_correct(update, ordering_rules)
        if update_correct:
            result += update[len(update) // 2]
    return result

def part2(data):
    """Solve part 2."""
    # Every number must appear as many times in update rules as there are other numbers

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year = 2024
    day = int("05")
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=year, day=day)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))