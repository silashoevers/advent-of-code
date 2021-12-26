point_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

matching_open = {
    '}': '{',
    ')': '(',
    ']': '[',
    '>': '<'
}

matching_close = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>',
}


def compute_score(stack):
    score = 0
    stack.reverse()
    for bracket in stack:
        score *= 5
        score += point_table.get(matching_close.get(bracket))
    return score


if __name__ == '__main__':
    # Parse input
    with open('input/Day_10.txt') as f:
        puzzle_input = f.read().split('\n')

    scores = []
    for line in puzzle_input:
        corrupted = False
        current_stack = []
        for char in line:
            # Open or close?
            if char not in matching_open:
                current_stack.append(char)
            else:
                if matching_open.get(char) == current_stack[-1]:
                    current_stack.pop()
                else:
                    corrupted = True
                    break
        if not corrupted:
            scores.append(compute_score(current_stack))
    print(sorted(scores)[len(scores)//2])
