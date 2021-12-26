
def flash(energy_levels):
    # Increment all energy levels
    energy_levels = [list(map(lambda x: x + 1, row)) for row in energy_levels]

    flashes = 0  # Keep track of amount of flashes
    while True:
        prev_energy_levels = [row.copy() for row in energy_levels]
        for x in range(matrix_dim):
            for y in range(matrix_dim):
                # Does octopus flash?
                if energy_levels[x][y] > 9:
                    flashes += 1
                    energy_levels[x][y] = 0
                    for dx, dy in neighbour_indices(x, y):
                        if energy_levels[dx][dy] != 0:
                            energy_levels[dx][dy] += 1
        if prev_energy_levels == energy_levels:
            break
    return energy_levels, flashes


def neighbour_indices(x, y):
    """
    Inefficient but makes grid based calculations
    more straight forward
    """
    indices = []
    for dx in range(max(0, x - 1), min(matrix_dim - 1, x + 1) + 1):
        for dy in range(max(0, y - 1), min(matrix_dim - 1, y + 1) + 1):
            if not (dx == x and dy == y):
                indices.append((dx, dy))
    return indices


def print_energy_levels(energy_levels):
    for row in energy_levels:
        for energy_level in row:
            print(energy_level, end="")
        print()
    print("\n")


if __name__ == '__main__':
    # Parse input
    with open('input/Day_11.txt') as f:
        current_energy_levels = [list(map(int, line)) for line in f.read().split('\n')]

    # Global-ish variables
    matrix_dim = len(current_energy_levels)
    steps = 100
    total_flashes = 0

    # Let's go
    for step in range(1, steps + 1):
        current_energy_levels, new_flashes = flash(current_energy_levels)
        total_flashes += new_flashes
    print(f"Total flashes = {total_flashes}")
