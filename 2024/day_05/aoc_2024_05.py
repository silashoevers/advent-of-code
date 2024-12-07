import pandas as pd
from aocd import get_data
from collections import Counter
# Using compare function in sorted possible: https://docs.python.org/3/howto/sorting.html#comparison-functions
from functools import cmp_to_key
import numpy as np
import numpy.ma as ma

def parse(puzzle_input):
    """Parse input."""
    ordering_rules, updates = puzzle_input.split('\n\n')
    ordering_rules_parsed = [tuple(map(int, rule.split('|'))) for rule in ordering_rules.splitlines()]
    updates_parsed = [list(map(int, update.split(','))) for update in updates.splitlines()]
    return ordering_rules_parsed, updates_parsed

def create_cmp_df(ordering_rules):
    """Encode what ordering between page numbers we know:
    -1: row < col, 0: row == col, 1: row > col, NaN: no comp known"""
    possible_page_numbers = set([page for rule in ordering_rules for page in rule])
    cmp_df = pd.DataFrame(index=list(possible_page_numbers), columns=list(possible_page_numbers))
    for before, after in ordering_rules:
        cmp_df.loc[before,after], cmp_df.loc[after, before] = -1, 1
    return cmp_df

def part1(data):
    """Solve part 1."""
    ordering_rules, updates = data
    cmp_df = create_cmp_df(ordering_rules)
    middle_pages_sum = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(lambda a, b: cmp_df.loc[a,b]))
        if update == sorted_update:  # Was update already correctly ordered?
            middle_pages_sum += sorted_update[len(sorted_update) // 2]
    return middle_pages_sum

def part2(data):
    """Solve part 2."""
    ordering_rules, updates = data
    cmp_df = create_cmp_df(ordering_rules)
    middle_pages_sum = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(lambda a, b: cmp_df.loc[a,b]))
        if not update == sorted_update:  # Was update already correctly ordered?
            middle_pages_sum += sorted_update[len(sorted_update) // 2]
    return middle_pages_sum


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