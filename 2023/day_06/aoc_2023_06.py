import re
import math
import functools
import time

puzzle_input_path = "input.txt"

with open(puzzle_input_path) as f:
    raw_puzzle_input = f.read().splitlines()

race_times = tuple(map(lambda t: int(t), re.findall("[0-9]+", raw_puzzle_input[0])))
record_times = tuple(map(lambda t: int(t), re.findall("[0-9]+", raw_puzzle_input[1])))

# Part 1
# Brute force approach
# Iterate over all races and all possible charge times
number_of_ways_to_beat_record = []
for race_time, record_time in zip(race_times, record_times):
    record_beating_charge_times = []
    for possible_charge_time in range(0, race_time + 1):
        if possible_charge_time * (race_time - possible_charge_time) > record_time:
            record_beating_charge_times.append(record_beating_charge_times)
    number_of_ways_to_beat_record.append(len(record_beating_charge_times))
print(math.prod(number_of_ways_to_beat_record))

# Part 2
#
race_time = int(functools.reduce(lambda a, b: a + b, re.findall("[0-9]+", raw_puzzle_input[0])))
record_time = int(functools.reduce(lambda a, b: a + b, re.findall("[0-9]+", raw_puzzle_input[1])))

record_beating_charge_times = []
for possible_charge_time in range(0, race_time + 1):
    if possible_charge_time * (race_time - possible_charge_time) > record_time:
        record_beating_charge_times.append(possible_charge_time)