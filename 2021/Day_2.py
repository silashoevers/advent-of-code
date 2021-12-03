

if __name__ == '__main__':
    with open('input/Day_2.txt') as f:
        steps = [line.strip().split(' ') for line in f]
    x, y, aim = 0, 0, 0
    for (direction, amount) in steps:
        amount = int(amount)
        if direction == 'forward':
            x += amount
            y += aim * amount
        elif direction == 'up':
            # y -= amount
            aim -= amount
        elif direction == 'down':
            # y += amount
            aim += amount
        else:
            print("Oops")
    print(x * y)


