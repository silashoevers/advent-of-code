import itertools


def find_dim(lines):
    max_x = 0
    max_y = 0
    for (x1, y1), (x2, y2) in lines:
        max_x = max(x1, x2, max_x)
        max_y = max(y1, y2, max_y)
    return max_x + 1, max_y + 1


def print_diagram(diagram):
    for row in diagram:
        for val in row:
            if val == 0:
                print('.', end='')
            else:
                print(val, end='')
        print('')
    print('')


def mark(diagram, coordinates):
    # Check type of direction and base iterator on that
    (x1, y1), (x2, y2) = coordinates
    x_range = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
    y_range = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
    # Row
    if y1 == y2:
        iterator = zip(x_range, itertools.repeat(y1))
    # Column
    elif x1 == x2:
        iterator = zip(itertools.repeat(x1), y_range)
    # Diagonal
    # Comment out for Part One
    else:
        iterator = zip(x_range, y_range)
    for (x, y) in iterator:
        diagram[y][x] += 1
    return diagram


def count_overlap(diagram):
    count = 0
    for row in diagram:
        for val in row:
            if val >= 2:
                count += 1
    return count


if __name__ == '__main__':
    # Parse input
    with open('input/Day_5.txt') as f:
        lines = [[tuple(map(int, tup.split(','))) for tup in line.split(' -> ')] for line in f.read().split('\n')]

    # Determine dimensions
    n, m = find_dim(lines)

    # Setup starting matrix
    mat = [0] * n
    for x in range(n):
        mat[x] = [0] * m

    # Produce the resulting matrix
    for coordinates in lines:
        mat = mark(mat, coordinates)

    # print_diagram(mat)
    print("Part Two:", count_overlap(mat))