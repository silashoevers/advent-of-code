point_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

matching_open = {
    '}': '{',
    ')': '(',
    ']': '[',
    '>': '<'
}

if __name__ == '__main__':
    # Parse input
    with open('input/Day_10.txt') as f:
        puzzle_input = f.read().split('\n')

    syntax_error_score = 0
    for line in puzzle_input:
        stack = []
        for char in line:
            # Open or close?
            if char not in matching_open:
                stack.append(char)
            else:
                if matching_open.get(char) == stack[-1]:
                    stack.pop()
                else:
                    syntax_error_score += point_table.get(char)
                    break
    print(syntax_error_score)
