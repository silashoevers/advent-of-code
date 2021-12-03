def surface(length, width, height):
    return 2*length*width + 2*width*height + 2*height*length


def surface_smallest_side(length, width, height):
    sorted_dims = sorted([length, width, height])
    return sorted_dims[0] * sorted_dims[1]


def perimeter_smallest_side(length, width, height):
    sorted_dims = sorted([length, width, height])
    return sorted_dims[0] * 2 + sorted_dims[1] * 2


def volume(length, width, height):
    return length*width*height


if __name__ == '__main__':
    presents = []
    with open('input/2015_Day_2.txt', 'r') as f:
        for line in f:
            dimensions = [int(dim.strip()) for dim in line.split('x')]
            presents.append(dimensions)

    # Compute total amount of wrapping paper needed
    total_wrapping_paper = 0
    for l, w, h in presents:
        total_wrapping_paper += surface(l, w, h) + surface_smallest_side(l, w, h)
    print("Total wrapping:", total_wrapping_paper)




