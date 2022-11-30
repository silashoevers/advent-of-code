from day_base import Day


class Day1(Day):
    def __init__(self):
        super().__init__(2021, 1, "Sonar Sweep")

    def part_a(self) -> int:
        depths = list(map(int, self.input))
        increase_count = 0
        for a, b in zip(depths, depths[1:]):
            if b > a:
                increase_count += 1
        return increase_count

    def part_b(self):
        depths = list(map(int, self.input))
        increase_count = 0
        for a, b, c, d in zip(depths, depths[1:], depths[2:], depths[3:]):
            if b + c + d > a + b + c:
                increase_count += 1
        return increase_count


if __name__ == '__main__':
    Day1().run()
