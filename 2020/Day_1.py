from itertools import combinations

if __name__ == '__main__':
    with open('input/Day_1.txt') as f:
        numbers = [int(line.strip()) for line in f]
    for p, q, r in combinations(numbers, 3):
        if p + q + r == 2020:
            print("Result:", p * q * r)
            break
