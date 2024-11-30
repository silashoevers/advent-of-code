from aocd import get_data

# We can assign every letter it's corresponding "rank". Remember that ranks loop back: Rocks (1) beats Scissors (3)
# By means of a modulus 3 we can quickly calculate winning and losing move for player
shape_letter_to_int = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
    'X': 1,
    'Y': 2,
    'Z': 3,
}

def parse(puzzle_input):
    """Parse input."""
    rounds = puzzle_input.splitlines()
    return [tuple(map(lambda play: shape_letter_to_int[play], round.split())) for round in rounds]

def part1(data):
    """Solve part 1."""
    total_score = 0
    for opponent_play, your_play in data:
        # Did the play result in a win (6 points), draw (3 points) or loss (0 points) for you?
        if (your_play - opponent_play) % 3 == 1: # Are you picking a shape with a higher "rank"?
            total_score += 6
        elif opponent_play == your_play:
            total_score += 3
        # Add score depending on selected shape
        total_score += your_play
    return total_score

def part2(data):
    """Solve part 2."""
    # Second column is round result: 1 = lose, 2 = draw, 3 = means
    total_score = 0
    for opponent_play, round_result in data:
        if round_result == 1:
            your_play = (opponent_play - 2) % 3 + 1
        elif round_result == 2:
            your_play = opponent_play
            total_score += 3
        elif round_result == 3:
            your_play = (opponent_play % 3) + 1
            total_score += 6
        else:
            raise ValueError('Round result has unexpected value')
        total_score += your_play

    return total_score


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    year= "2022"
    day= "02"
    print(f"Solving for year {year}, day {day}:")
    puzzle_input = get_data(year=int(year), day=int(day))
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))