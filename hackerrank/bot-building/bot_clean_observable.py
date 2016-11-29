# neighbour_moves = {'upleft': (-1, -1), 'up': (-1, 0), 'upright': (-1, 1),
#                    'left': (0, -1), 'right': (0, 1),
#                    'downleft': (1, -1), 'down': (1, 0), 'downright': (1, 1)}
import json
neighbour_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
visited_cells = []  # holds a matrix of boolean values


def next_move(row, col, board):
    global visited_cells
    visited_cells[row][col] = True  # we have visited this cell

    if board[row][col] == 'd':
        # we're at a dirty spot - clean it
        board[row][col] = '-'
        print('CLEAN')
        return
    spot_result = get_neighbour_dirty_spot(row, col, board)
    if spot_result == 'No spot!':
        # get the closest spot we haven't visited
        spot_result = get_close_non_visited_spot(row, visited_cells)
    spot_row, spot_col = spot_result


    if row != spot_row:
        if row > spot_row:
            print('UP')
        if row < spot_row:
            print('DOWN')
    elif col != spot_col:
        if col > spot_col:
            print('LEFT')
        if col < spot_col:
            print('RIGHT')


def get_neighbour_dirty_spot(row, col, board):
    # go through each neighbour node and see if it has a dirty spot
    for add_row, add_col in neighbour_moves:
        new_row, new_col = row + add_row, col + add_col
        # check if they're in bounds of the array and if it's a dirty spot
        if (0 <= new_row < len(board) and 0 <= new_col < len(board)
            and board[new_row][new_col] == 'd'):
            return new_row, new_col
    # we have not found a dirty spot
    return 'No spot!'


def get_close_non_visited_spot(orig_row, matrix):
    # search for a dirty spot on the same row
    dirty_spot_col = contains_non_visited_spot(matrix[orig_row])
    if dirty_spot_col != 'No Spot':
        return orig_row, dirty_spot_col

    # we start looking for the other rows, expanding the rows we've covered one by one vertically
    upper_row, lower_row = orig_row, orig_row
    while upper_row >= 0 or lower_row < len(matrix):
        upper_row -= 1
        lower_row += 1
        if upper_row >= 0:
            possible_upper_row_spot = contains_non_visited_spot(matrix[upper_row])
            if possible_upper_row_spot != 'No Spot':
                return upper_row, possible_upper_row_spot  # we've found a spot we haven't visited
        if lower_row < len(matrix):
            possible_lower_row_spot = contains_non_visited_spot(matrix[lower_row])
            if possible_lower_row_spot != 'No Spot':
                return lower_row, possible_lower_row_spot


def contains_non_visited_spot(row: list):
    """ given a list, this function returns the index of a spot we have not visited in the array, otherwise
        returns 'No Spot' """
    for idx, spot in enumerate(row):
        if not spot:
            return idx  # we have not visited this spot

    return 'No Spot'


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board_ = [[j for j in input().strip()] for i in range(5)]
    try:
        # if we've visited any nodes, read them off the .txt
        with open('visited.txt', 'r', encoding='utf-8') as file:
            visited_cells = eval(file.readline())
    except:
        # the previous code will thrown an error only if we haven't saved visited.txt yet
        visited_cells = [[False for j in i] for i in board_]
    next_move(pos[0], pos[1], board_)
    # write the nodes we've visited after every move
    with open('visited.txt', 'w') as file:
        file.write(str(visited_cells))
