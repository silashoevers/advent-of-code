
if __name__ == '__main__':
    count = 0
    with open('input/Day_2.txt') as f:
        for line in f:
            policy, password = line.strip().split(': ')
            bounds, letter = policy.split(' ')
            first_character, second_character = map(int, bounds.split('-'))
            letter_count = password.count(letter)
            if (password[first_character - 1] == letter) ^ (password[second_character - 1] == letter):
                count += 1
    print(count)
