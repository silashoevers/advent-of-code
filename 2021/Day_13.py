import numpy as np


def print_paper(p):
    for row in p:
        for char in row:
            if char:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


# Initial input parsing. Split coordinates and fold instructions
with open('input/Day_13.txt') as f:
    dot_coordinates, instructions = f.read().split('\n\n')

# Setup paper
coordinates = [tuple(map(int, coordinates.split(','))) for coordinates in dot_coordinates.split('\n')]
x_dim = max(coordinates, key=lambda t: t[0])[0] + 1
y_dim = max(coordinates, key=lambda t: t[1])[1] + 2  # +2 because otherwise paper is not foldable
paper = np.zeros((y_dim, x_dim), dtype=bool)
for (x, y) in coordinates:
    paper[y, x] = True

print(x_dim, y_dim)

# Perform folding
for instruction in instructions.split('\n'):
    direction, pivot = instruction[11:].split('=')
    pivot = int(pivot)
    # Vertical fold |
    if direction == 'x':
        new_x_dim = x_dim // 2  # New dimension due to folding, // already does floor
        new_paper = np.zeros((y_dim, new_x_dim), dtype=bool)
        for y in range(y_dim):
            for x in range(new_x_dim):
                new_paper[y, x] = paper[y, x] or paper[y, x_dim - x - 1]
        x_dim = new_x_dim
    # Horizontal fold -
    else:
        new_y_dim = y_dim // 2
        new_paper = np.zeros((new_y_dim, x_dim), dtype=bool)
        for y in range(new_y_dim):
            for x in range(x_dim):
                new_paper[y, x] = paper[y, x] or paper[y_dim - y - 1, x]
        y_dim = new_y_dim
    paper = new_paper
    # print(f'Number of dots: {np.count_nonzero(paper)}')
print_paper(paper)
