from types import CodeType
from aocd import get_data
from parse import parse
import time
import copy
from collections import deque

class Item:
    def __init__(self, starting_worry_level: int):
        self.worry_level = starting_worry_level

class Monkey:
    template = "Monkey {}:\n" \
               "  Starting items: {items:parse_starting_worry_levels}\n" \
               "  Operation: new = {operation:parse_operation}\n" \
               "  Test: divisible by {test:d}\n" \
               "    If true: throw to monkey {if_true:d}\n" \
               "    If false: throw to monkey {if_false:d}"

    def __init__(self, items: list[Item], operation: CodeType, test: int, if_true: int, if_false: int):
        self.items = deque(items)  # Efficiency in popleft and append
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.num_inspected = 0

    def inspect_all_items(self, all_monkeys):
        while self.items:
            # Inspect an individual item and throw it to the appropriate other monkey
            inspected_item = self.items.popleft()
            old = inspected_item.worry_level
            inspected_item.worry_level = eval(self.operation)
            inspected_item.worry_level //= 3
            if not inspected_item.worry_level % self.test:
                all_monkeys[self.if_true].items.append(inspected_item)
            else:
                all_monkeys[self.if_false].items.append(inspected_item)
            self.num_inspected += 1
        return

    """Methods for turning raw monkey string into Monkey object"""
    @classmethod
    def parse_starting_worry_levels(cls, starting_worry_levels: str):
        return [Item(int(starting_worry_level)) for starting_worry_level in starting_worry_levels.split(', ')]

    @classmethod
    def parse_operation(cls, operation: str):
        return compile(operation,'<string>','eval')

    @classmethod
    def from_string(cls, raw_monkey):
        parse_result = parse(cls.template, raw_monkey, {'parse_starting_worry_levels': cls.parse_starting_worry_levels,
                                     'parse_operation': cls.parse_operation})
        return cls(**parse_result.named)

def parse_puzzle_input(puzzle_input):
    """Parse input."""
    return [Monkey.from_string(raw_monkey) for raw_monkey in puzzle_input.split('\n\n')]

def part1(data):
    """Solve part 1."""
    max_num_rounds = 20
    monkeys = copy.deepcopy(data)

    for _ in range(max_num_rounds):
        # Perform one round: Let each monkey in order inspect all its items
        for monkey in monkeys:
            monkey.inspect_all_items(monkeys)

    # Find the two most active monkeys
    sorted_num_inspect = sorted([monkey.num_inspected for monkey in monkeys], reverse=True)
    return sorted_num_inspect[0] * sorted_num_inspect[1]

def part2(data):
    """Solve part 2."""
    max_num_rounds = 10000
    monkeys = copy.deepcopy(data)

    # TODO: Refactor play into separate function
    for _ in range(max_num_rounds):
        # Perform one round: Let each monkey in order inspect all its items
        for monkey in monkeys:
            monkey.inspect_all_items(monkeys)

    # Find the two most active monkeys
    sorted_num_inspect = sorted([monkey.num_inspected for monkey in monkeys], reverse=True)
    return sorted_num_inspect[0] * sorted_num_inspect[1]


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    # Parse puzzle input. Same input shared by part 1 and 2 solvers
    data = parse_puzzle_input(puzzle_input)

    # Part 1
    before = time.time()
    solution1 = part1(data)
    after = time.time()
    print(f"## Part 1\n{solution1}\n{after - before}s\n")

    # Part 2
    before = time.time()
    solution2 = part2(data)
    after = time.time()
    print(f"## Part 2\n{solution2}\n{after - before}s")

    return

if __name__ == "__main__":
    year = 2022
    day = 11
    print(f"# Year {year}, day {day}")
    puzzle_input = get_data(year=year, day=day)
    solve(puzzle_input)