"""
link = https://www.codewars.com/kata/53db96041f1a7d32dc0004d2
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. 
If the board is valid return 'Finished!', otherwise return 'Try again!'
"""


def done_or_not(board):
    valid = 'Finished!'

    for i in board:
        if len(i) != len(set(i)):
            valid = 'Try again!'
            return valid
    rotated_board = [list(r) for r in zip(*board[::-1])]

    for i in rotated_board:
        if len(i) != len(set(i)):
            valid = 'Try again!'
            return valid

    for n in range(0, 9, 3):
        start_i = n
        for m in range(0, 9, 3):
            start_j = m
            new_region = []
            for i in range(start_i, start_i+3):
                for j in range(start_j, start_j+3):
                    if board[i][j] in new_region:
                        valid = 'Try again!'
                        new_region.append(board[i][j])
                        return valid
                    else:
                        new_region.append(board[i][j])
    return valid


def main():
    print(
        done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                 [4, 9, 8, 2, 6, 1, 3, 7, 5],
                 [7, 5, 6, 3, 8, 4, 2, 1, 9],
                 [6, 4, 3, 1, 5, 8, 7, 9, 2],
                 [5, 2, 1, 7, 9, 3, 8, 4, 6],
                 [9, 8, 7, 4, 2, 6, 5, 3, 1],
                 [2, 1, 4, 9, 3, 5, 6, 8, 7],
                 [3, 6, 5, 8, 1, 7, 9, 2, 4],
                 [8, 7, 9, 6, 4, 2, 1, 5, 3]]),
    'Finished!')

    print(
        done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                 [4, 9, 8, 2, 6, 1, 3, 7, 5],
                 [7, 5, 6, 3, 8, 4, 2, 1, 9],
                 [6, 4, 3, 1, 5, 8, 7, 9, 2],
                 [5, 2, 1, 7, 9, 3, 8, 4, 6],
                 [9, 8, 7, 4, 2, 6, 5, 3, 1],
                 [2, 1, 4, 9, 3, 5, 6, 8, 7],
                 [3, 6, 5, 8, 1, 7, 9, 2, 4],
                 [8, 7, 9, 6, 4, 2, 1, 3, 5]]),
    'Try again!')


if __name__ == "__main__":
    main()
