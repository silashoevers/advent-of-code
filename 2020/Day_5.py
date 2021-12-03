

if __name__ == '__main__':
    # Parse puzzle input
    with open('input/Day_5.txt') as f:
        tickets = [line.strip() for line in f]
    seat_ids = []
    for ticket in tickets:
        # Find row number
        possible_rows = range(128)
        for cut in ticket[:8]:
            if cut == 'F':
                pass
            elif cut == 'B':
                pass

        # Find column number
        possible_columns = range(8)
