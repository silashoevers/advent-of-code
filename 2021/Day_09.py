if __name__ == '__main__':
    # Parse input
    with open('input/Day_09.txt') as f:
        heightmap = [[int(char) for char in line] for line in f.read().split('\n')]

    # Iterate over matrix
    risk_level_sum = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            current_height = heightmap[i][j]
            is_lowest_point = True
            # Up
            try:
                if i - 1 >= 0:
                    is_lowest_point = current_height < heightmap[i - 1][j] and is_lowest_point
            except IndexError:
                pass
            # Down
            try:
                is_lowest_point = current_height < heightmap[i + 1][j] and is_lowest_point
            except IndexError:
                pass
            # Left
            try:
                if j - 1 >= 0:
                    is_lowest_point = current_height < heightmap[i][j - 1] and is_lowest_point
            except IndexError:
                pass
            # Right
            try:
                is_lowest_point = current_height < heightmap[i][j + 1] and is_lowest_point
            except IndexError:
                pass
            if is_lowest_point:
                risk_level_sum += current_height + 1
    print("Part One:", risk_level_sum)
