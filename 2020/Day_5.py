

if __name__ == '__main__':
    # Parse puzzle input
    with open('input/Day_5.txt') as f:
        tickets = [line.strip() for line in f]
    seat_ids = []
    for ticket in tickets:
        # Find row number
        possible_rows = range(128)
        for cut in ticket[:7]:
            if cut == 'F':
                possible_rows = possible_rows[:len(possible_rows)//2]
            elif cut == 'B':
                possible_rows = possible_rows[len(possible_rows)//2:]

        # Find column number
        possible_columns = range(8)
        for cut in ticket[7:]:
            if cut == 'L':
                possible_columns = possible_columns[:len(possible_columns)//2]
            elif cut == 'R':
                possible_columns = possible_columns[len(possible_columns)//2:]
            else:
                print("Oops")

        seat_ids.append(possible_rows[0] * 8 + possible_columns[0])
    print("Part 1:", max(seat_ids))
