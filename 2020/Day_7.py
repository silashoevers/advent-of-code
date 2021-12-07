import re


bag_reg = r'([0-9]+) ([a-z]+ [a-z]+)'

if __name__ == '__main__':
    with open('input/Day_7.txt') as f:
        rules = [rule[:-1] for rule in f.read().split('\n')]  # Remove full stop at end of every line

    # Build dictionary with {bag_type: {smaller_bag_type: max_amount}}
    bag_contains = {}
    for rule in rules:
        outer_bag, contains = rule.split(' bags contain ')
        # Contains no other bags
        if contains == 'no other bags':
            continue
        else:
            bag_contains[outer_bag] = {}
            for contain in contains.split(', '):
                match = re.match(bag_reg, contain)
                bag_type, amount = match.group(2), int(match.group(1))
                bag_contains[outer_bag][bag_type] = amount

    # Part One
    # Count amount of bags that can contain a silver bag
    possible_outer_bags = {'shiny gold'}
    while True:
        current_count = len(possible_outer_bags)
        for outer_bag, contains in bag_contains.items():
            if len(possible_outer_bags.intersection(set(contains))) > 0:
                possible_outer_bags.add(outer_bag)
        # I we have not found a new possible outer bag we can terminate
        if current_count == len(possible_outer_bags):
            break

    # Part Two
    