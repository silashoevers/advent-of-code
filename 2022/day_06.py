from day_base import Day


class Day6(Day):
    def __init__(self):
        super().__init__(2022, 6, "Tuning Trouble", expected_a=10, expected_b=29)

    def parse(self, puzzle_input):
        # No special parsing required (as of now)
        return puzzle_input

    def part_a(self, parsed_puzzle_input) -> int:
        for i in range(len(parsed_puzzle_input)):
            if len(set(parsed_puzzle_input[i:i+4])) == 4:
                return i + 4

    def part_b(self, parsed_puzzle_input) -> int:
        for i in range(len(parsed_puzzle_input)):
            if len(set(parsed_puzzle_input[i:i+14])) == 14:
                return i + 14


if __name__ == '__main__':
    Day6().run()
