if __name__ == '__main__':
    # Parse input file
    with open('input/Day_01.txt') as f:
        depths = [int(line) for line in f]

    # Part 1
    count = 0
    for (x, y) in zip(depths[:-1], depths[1:]):  # Zip together concurrent values
        if y > x:
            count += 1
    print("Part One:", count)

    # Part 2
    sums = [a+b+c for a, b, c in zip(depths[:-2], depths[1:-1], depths[2:])]
    differences = [j-i for i, j in zip(sums[:-1], sums[1:])]
    count = 0
    for diff in differences:
        if diff > 0:
            count += 1
    print("Part Two:", count)
