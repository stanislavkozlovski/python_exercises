directs = {
    (0, 1), (0, -1), (-1, 0), (1, 0)
}


def exist(board):
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col == '#':
                valid = True
                for x, y in directs:
                    new_r = row_idx + x
                    new_c = col_idx + y
                    if new_r >= 0 and new_r < len(board) and new_c >= 0 and new_c < len(board[new_r]) and board[new_r][new_c] == '#':
                        pass
                    else:
                        valid = False
                if valid:
                    return "Exist"

    return 'Does not exist'

# print(exist([".#.#", "#.#.", ".#.#", "#.#."]))