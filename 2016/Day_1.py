

if __name__ == '__main__':
    with open('input/Day_1.txt') as f:
        instructions = f.read().split(', ')
    direction = 0  # North = 0, South = 1, etc.
    x, y = 0, 0    # Coordinate (0,0) is starting point
    checkpoints = [(x, y)]
    for instruction in instructions:
        direction = instruction[0]
        steps = instruction[1:]
        if direction == 0:
            y += steps
        elif direction == 1:
            x += steps
        elif direction == 2:
            y -= steps
        elif direction == 3:
            x -= steps
        else:
            print("Well, this is awkward")

