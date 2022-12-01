from day_base import Day


class Day1(Day):
    def __init__(self):
        super().__init__(2022, 1, "Calorie Counting", expected_a=24000, expected_b=45000)

    # TODO: Move summing up total calories into this function
    def parse(self):
        pass

    def part_a(self):
        individual_calories = [list(map(int, calories_per_elf.split('\n'))) for calories_per_elf in self.input.split('\n\n')[:-1]]
        total_calories_per_elf = map(sum, individual_calories)
        return max(total_calories_per_elf)

    def part_b(self):
        individual_calories = [list(map(int, calories_per_elf.split('\n'))) for calories_per_elf in self.input.split('\n\n')[:-1]]
        total_calories_per_elf = map(sum, individual_calories)
        sorted_calories_per_elf = sorted(total_calories_per_elf, reverse=True)
        return sum(sorted_calories_per_elf[:3])


if __name__ == '__main__':
    day = Day1()
    day.run()
