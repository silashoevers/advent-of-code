import re
import parse

input_path = "input.txt"

# Read puzzle input
with open(input_path) as f:
    puzzle_input = f.read().splitlines()

game_parser = parse.compile("Game {:d}: {}")
red_parser = parse.compile("{:d} red")
green_parser = parse.compile("{:d} green")
blue_parser = parse.compile("{:d} blue")

# Part 1
gameID_sum = 0
for game in puzzle_input:
    possible = True
    gameID, reveals = game_parser.parse_puzzle_input(game).fixed
    for reveal in reveals.split("; "):
        red = red_parser.search(reveal)
        if red is not None and red[0] > 12:
            possible = False
        green = green_parser.search(reveal)
        if green is not None and green[0] > 13:
            possible = False
        blue = blue_parser.search(reveal)
        if blue is not None and blue[0] > 14:
            possible = False
    if possible:
        gameID_sum += gameID
print(gameID_sum)

# Part 2
power_sum = 0
for game in puzzle_input:
    highest_red = 0
    highest_green = 0
    highest_blue = 0
    gameID, reveals = game_parser.parse_puzzle_input(game).fixed
    for reveal in reveals.split("; "):
        red = red_parser.search(reveal)
        if red is not None and red[0] > highest_red:
            highest_red = red[0]
        green = green_parser.search(reveal)
        if green is not None and green[0] > highest_green:
            highest_green = green[0]
        blue = blue_parser.search(reveal)
        if blue is not None and blue[0] > highest_blue:
            highest_blue = blue[0]
    power = highest_red * highest_green * highest_blue
    power_sum += power
print(power_sum)