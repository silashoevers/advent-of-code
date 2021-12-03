if __name__ == '__main__':
    with open('input/Day_1.txt') as f:
        depths = [int(line) for line in f]
    sums = [a+b+c for a, b, c in zip(depths[:-2], depths[1:-1], depths[2:])]
    differences = [j-i for i, j in zip(sums[:-1], sums[1:])]
    count = 0
    for diff in differences:
        if diff > 0:
            count += 1
    print(count)
