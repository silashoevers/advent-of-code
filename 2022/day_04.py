from parse import *
from day_base import Day


# TODO: Replace usage of sets by something more efficient i.e. proper comparisons and arithmatic
class Day4(Day):
    def __init__(self):
        super().__init__(2022, 4, "Camp Cleanup", debug=True, expected_a=2, expected_b=4)

    def parse(self, puzzle_input):
        """
        Returns tuples of sets containing all sections that each elf in a pair has to clean
        """
        result = []
        for section_assignment_pair in puzzle_input.split('\n'):
            parse_format = "{}-{},{}-{}"
            parsed_result = parse(parse_format, section_assignment_pair).fixed

            # Convert strings to integers to use them in computation later on
            parsed_result = map(int, parsed_result)

            # Unpack parsed_result into more human-readable names
            section_a_beginning, section_a_end, section_b_beginning, section_b_end = parsed_result

            # Pretty Python Hack
            sections_covered_by_a = set(range(section_a_beginning, section_a_end + 1))
            sections_covered_by_b = set(range(section_b_beginning, section_b_end + 1))

            result.append((sections_covered_by_a, sections_covered_by_b))
        return result

    def part_a(self, parsed_puzzle_input) -> int:
        total_full_overlapping_sections = 0
        for sections_covered_by_a, sections_covered_by_b in parsed_puzzle_input:
            shared_sections = sections_covered_by_a.intersection(sections_covered_by_b)
            if shared_sections == sections_covered_by_a or shared_sections == sections_covered_by_b:
                total_full_overlapping_sections += 1
        return total_full_overlapping_sections

    def part_b(self, parsed_puzzle_input) -> int:
        total = 0
        for range_a, range_b in parsed_puzzle_input:
            shared_section = range_a.intersection(range_b)
            if len(shared_section):
                total += 1
        return total


if __name__ == '__main__':
    Day4().run()
