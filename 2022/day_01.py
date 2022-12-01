from day_base import Day


class Day1(Day):
    def __init__(self):
        super().__init__(2022, 1, "Calorie Counting", expected_a=24000, expected_b=45000)

    # TODO: Move summing up total calories into this function
    def parse(self, puzzle_input):
        individual_calories = [list(map(int, calories_per_elf.split('\n'))) for calories_per_elf in puzzle_input.split('\n\n')[:-1]]
        return list(map(sum, individual_calories))

    def part_a(self, parsed_puzzle_input):
        return max(parsed_puzzle_input)

    def part_b(self, parsed_puzzle_input):
        sorted_calories_per_elf = sorted(parsed_puzzle_input, reverse=True)
        return sum(sorted_calories_per_elf[:3])


if __name__ == '__main__':
    day = Day1()
    day.run()
