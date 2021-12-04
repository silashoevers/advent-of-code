import re
import numpy as np


def has_bingo(board):
    # Check rows
    for row in board:
        if sum(row) == -5:
            return True
    # Check columns
    for col in np.transpose(board):
        if sum(col) == -5:
            return True
    # No bingo
    return False


def sign_off(board, number):
    return [[-1 if x == number else x for x in row] for row in board]


def compute_score(board, final_number):
    board_sum = 0
    for row in board:
        for num in row:
            if num >= 0:
                board_sum += num
    return board_sum * final_number


if __name__ == '__main__':
    # Parse input
    with open('input/Day_4.txt') as f:
        lines = f.read().split('\n\n')
    random_numbers = map(int, lines[0].split(','))

    # Split the rows of the boards
    boards = [[list(map(int, re.split(r'\s+', row.strip()))) for row in board.split('\n')] for board in lines[1:]]

    # Play bingo
    for next_number in random_numbers:
        boards = list(map(lambda board: sign_off(board, next_number), boards))
        for board in boards:
            if has_bingo(board):
                print("We've got a winner:", compute_score(board, next_number))
                break
        boards = [board for board in boards if not has_bingo(board)]
