from day_base import Day


def convert_item_to_priority_score(self, item: str):
    if item.islower():
        return ord(item) - 96
    elif item.isupper():
        return ord(item) - 38


class Day3(Day):
    def __init__(self):
        super().__init__(2022, 3, "Rucksack Reorganization", expected_a=157, expected_b=70)

    def parse(self, puzzle_input):
        return puzzle_input.split('\n')

    def part_a(self, parsed_puzzle_input) -> int:
        total = 0
        for rucksack_contents in parsed_puzzle_input:
            halfway = len(rucksack_contents) // 2
            compartment_a, compartment_b = rucksack_contents[:halfway], rucksack_contents[halfway:]
            items_in_both_compartments = set(compartment_a).intersection(compartment_b)
            total += convert_item_to_priority_score(self, list(items_in_both_compartments)[0])
        return total

    def part_b(self, parsed_puzzle_input) -> int:
        total = 0
        for i in range(0, len(parsed_puzzle_input), 3):
            elf1, elf2, elf3 = parsed_puzzle_input[i:i+3]
            shared_items_in_group = set(elf1).intersection(set(elf2), set(elf3))
            total += convert_item_to_priority_score(self, list(shared_items_in_group)[0])
        return total






if __name__ == '__main__':
    Day3().run()
