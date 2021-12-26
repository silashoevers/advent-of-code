from collections import Counter

if __name__ == '__main__':
    # Parse input
    with open('input/Day_06.txt') as f:
        timers = Counter([int(line) for line in f.read().split(',')])

    # Fill in missing counts
    for x in range(9):
        if x not in timers:
            timers[x] = 0

    zero_count = 0
    for _ in range(256):
        timers[0] = 0
        timers[7] += zero_count
        # Shift counts
        for x in range(1, 9):
            timers[x - 1] = timers[x]
        timers[8] = zero_count
        zero_count = timers[0]
    print(sum(timers.values()))

    # Parse input
    # with open('input/Day_06.txt') as f:
    #     timers = [int(line) for line in f.read().split(',')]
    #
    # zero_count = 0
    # for day in range(256):
    #     timers = [x for x in timers if x != 0]
    #     timers.extend([7]*zero_count)  # Reinsert regenerating fish
    #     timers = list(map(lambda x: x - 1, timers))
    #     timers.extend([8]*zero_count)  # Insert new fish
    #     zero_count = timers.count(0)
    # print(len(timers))
