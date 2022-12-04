from day_base import Day


class Day4(Day):
    def __init__(self):
        super().__init__(2022, 4, "Camp Cleanup", expected_a=2, expected_b=4)

    # TODO: Move section start-stop parsing here
    def parse(self, puzzle_input):
        return puzzle_input.split('\n')

    def part_a(self, parsed_puzzle_input) -> int:
        total = 0
        for section_assignment_pair in parsed_puzzle_input:
            section_a, section_b = section_assignment_pair.split(',')
            section_a_start, section_a_stop = map(int, section_a.split('-'))
            section_b_start, section_b_stop = map(int, section_b.split('-'))
            range_a = set(range(section_a_start, section_a_stop+1))
            range_b = set(range(section_b_start, section_b_stop+1))
            shared_section = range_a.intersection(range_b)
            if shared_section == range_a or shared_section == range_b:
                total += 1
        return total

    def part_b(self, parsed_puzzle_input) -> int:
        total = 0
        for section_assignment_pair in parsed_puzzle_input:
            section_a, section_b = section_assignment_pair.split(',')
            section_a_start, section_a_stop = map(int, section_a.split('-'))
            section_b_start, section_b_stop = map(int, section_b.split('-'))
            range_a = set(range(section_a_start, section_a_stop+1))
            range_b = set(range(section_b_start, section_b_stop+1))
            shared_section = range_a.intersection(range_b)
            if len(shared_section):
                total += 1
        return total

if __name__ == '__main__':
    Day4().run()
