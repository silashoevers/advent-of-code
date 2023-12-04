import parse


def calculate_number_of_matches(winning_numbers, my_numbers):
    my_winning_numbers = my_numbers.intersection(winning_numbers)
    matches = len(my_winning_numbers)
    return matches


puzzle_input_path = "input.txt"

with open(puzzle_input_path) as f:
    raw_puzzle_input = f.read().splitlines()

# Parse into raw numbers -> [(card_number, [winning_numbers], [my_numbers])]
parsed_puzzle_input = []
for line in raw_puzzle_input:
    # .parse instead of .search because of full match (instead of shortest possible)
    card_number, winning_numbers, my_numbers = parse.parse("Card {}: {} | {}", line).fixed
    card_number = int(card_number)
    winning_numbers = set(map(lambda n: int(n), winning_numbers.split()))
    my_numbers = set(map(lambda n: int(n), my_numbers.split()))
    parsed_puzzle_input.append((card_number, winning_numbers, my_numbers))


# Part 1
total_points = 0
for _, winning_numbers, my_numbers in parsed_puzzle_input:
    matches = calculate_number_of_matches(winning_numbers, my_numbers)
    points = 0
    if matches > 0:
        points = 2 ** (matches - 1)
    total_points += points

# Part 2
number_of_matches = list(map(lambda c: calculate_number_of_matches(c[1], c[2]), parsed_puzzle_input))
number_of_cards = [1] * len(parsed_puzzle_input)
for i in range(len(parsed_puzzle_input)):
    # Card number is i + 1
    cards_i = number_of_cards[i]
    matches_i = number_of_matches[i]
    number_of_cards[i+1:i + 1 + matches_i] = map(lambda a: a + cards_i, number_of_cards[i + 1:i + 1 + matches_i])

print(sum(number_of_cards))