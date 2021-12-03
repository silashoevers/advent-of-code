if __name__ == '__main__':
    count = 0
    with open('input/Day_2.txt') as f:
        for line in f:
            policy, password = line.strip().split(': ')
            bounds, letter = policy.split(' ')
            lower_bound, upper_bound = map(int, bounds.split('-'))
            letter_count = password.count(letter)
            if lower_bound <= letter_count <= upper_bound:
                count += 1
    print(count)