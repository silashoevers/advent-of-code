def tree_counter(trees, right, down):
    x, y, tree_count = 0, 0, 0
    while True:  # Quick hack for cutoff
        x = (x + right) % 31
        y += down
        if y >= len(rows):
            break
        if rows[y][x] == '#':
            tree_count += 1
    return tree_count


if __name__ == '__main__':
    with open('input/Day_3.txt') as f:
        rows = [line.strip() for line in f]
    total = 1
    for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        total *= tree_counter(rows, r, d)
    print("Total:", total)
