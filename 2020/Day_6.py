from collections import Counter


def everyone_yes(group):
    same_answers = set(group[0])
    for answers in group:
        same_answers = same_answers.intersection(set(answers))
    return same_answers


if __name__ == '__main__':
    # Part one or two?
    part_one = False

    # Parse input
    with open('input/Day_6.txt') as f:
        groups = [group.replace('\n', '') if part_one else group.split('\n') for group in f.read().split('\n\n')]

    if part_one:
        print("Part One:", sum([len(Counter(group)) for group in groups]))
    else:
        print("Part Two:", sum([len(everyone_yes(group)) for group in groups]))
