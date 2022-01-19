
part_one = False


def solve(crabs, goal):
    return sum(map(lambda x: fuel_required(x, goal), crabs))


def fuel_required(current, goal):
    if part_one:
        return abs(current - goal)
    else:
        # Inefficient but works
        true_dist = abs(current - goal)
        return true_dist * (true_dist + 1) // 2


if __name__ == '__main__':
    # Parse input
    with open('input/Day_07.txt') as f:
        crab_pos = list(map(int, f.read().split(',')))
    print(min([solve(crab_pos, pos) for pos in range(min(crab_pos), max(crab_pos) + 1)]))
