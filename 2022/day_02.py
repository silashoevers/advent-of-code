from day_base import Day


class Day2(Day):
    def __init__(self):
        super().__init__(2022, 2, "Rock Paper Scissors", expected_a=15, expected_b=12)

    def parse(self, puzzle_input):
        return [strategy_for_round.split(' ') for strategy_for_round in puzzle_input.split('\n')]

    def part_a(self, parsed_puzzle_input) -> int:
        move_equality_dict = {'X': 'A', 'Y': 'B', 'Z': 'C'}
        move_win_dict = {'X': 'C', 'Y': 'A', 'Z': 'B'}  # key wins from value
        move_score_dict = {'X': 1, 'Y': 2, 'Z': 3}

        total_score = 0
        for their_move, our_move in parsed_puzzle_input:
            total_score += move_score_dict[our_move]
            if their_move == move_equality_dict[our_move]:
                total_score += 3
            elif their_move == move_win_dict[our_move]:
                total_score += 6

        return total_score

    def part_b(self, parsed_puzzle_input) -> int:
        move_win_dict = {'A': 'C', 'B': 'A', 'C': 'B'}  # key wins from value
        move_lose_dict = {'A': 'B', 'B': 'C', 'C': 'A'}
        move_score_dict = {'A': 1, 'B': 2, 'C': 3}

        total_score = 0
        for their_move, outcome in parsed_puzzle_input:
            # Lose
            if outcome == 'X':
                total_score += move_score_dict[move_win_dict[their_move]]
            # Draw
            elif outcome == 'Y':
                total_score += 3
                total_score += move_score_dict[their_move]
            # Win
            elif outcome == 'Z':
                total_score += 6
                total_score += move_score_dict[move_lose_dict[their_move]]
        return total_score


if __name__ == '__main__':
    Day2().run()
