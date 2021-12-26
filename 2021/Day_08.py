import re

if __name__ == '__main__':
    # Setup global information
    original_mapping = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    original_mapping = map(set, original_mapping)

    # Parse input
    with open('input/Day_08.txt') as f:
        entries = [map(set, re.split(r' \| | ', line)) for line in f.read().split('\n')]

    for entry in entries:
        # Setup all possible options
        # possible_mappings = {
        #     'a': {'b', 'c', 'd', 'e', 'f', 'g'},
        #     'b': {'a', 'c', 'd', 'e', 'f', 'g'},
        #     'c': {'a', 'b', 'd', 'e', 'f', 'g'},
        #     'd': {'a', 'b', 'c', 'e', 'f', 'g'},
        #     'e': {'a', 'b', 'c', 'd', 'f', 'g'},
        #     'f': {'a', 'b', 'c', 'd', 'e', 'g'},
        #     'g': {'a', 'b', 'c', 'd', 'e', 'f'}
        # }
