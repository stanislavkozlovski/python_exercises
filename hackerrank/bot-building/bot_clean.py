MATRIX_LENGTH = 5

'''
The way this exercise works is it calls our next_move every time, so we can't
store the dirty spot coordinates anywhere but rather have to recalculate them each time
'''


def main():
    bot_row, bot_col = [int(coord) for coord in input().split()]
    matrix = []
    # read input
    for row_idx in range(MATRIX_LENGTH):
        new_row = list(input())
        if 'm' in new_row:
            bot_row, bot_col = row_idx, new_row.index('m')
        matrix.append(new_row)
    next_move(bot_row, bot_col, matrix)


def next_move(row, col, matrix):
    dirty_spot_coords = get_close_dirty_spot(row, matrix)
    if dirty_spot_coords == 'No Spot':
        raise Exception('NO MORE SPOTS TO BE FOUND EH')

    spot_row, spot_col = dirty_spot_coords

    if matrix[row][col] == 'd':
        # we're at a dirty spot - clean it
        matrix[row][col] = '-'
        print('CLEAN')
    elif row != spot_row:
        if row > spot_row:
            print('UP')
        if row < spot_row:
            print('DOWN')
    elif col != spot_col:
        if col > spot_col:
            print('LEFT')
        if col < spot_col:
            print('RIGHT')


def get_close_dirty_spot(orig_row, matrix):
    # search for a dirty spot on the same row
    dirty_spot_col = contains_dirty_spot(matrix[orig_row])
    if dirty_spot_col != 'No Spot':
        return orig_row, dirty_spot_col

    # we start looking for the other rows, expanding the rows we've covered one by one vertically
    upper_row, lower_row = orig_row, orig_row
    while upper_row >= 0 or lower_row < len(matrix):
        upper_row -= 1
        lower_row += 1
        if upper_row >= 0:
            possible_upper_row_spot = contains_dirty_spot(matrix[upper_row])
            if possible_upper_row_spot != 'No Spot':
                return possible_upper_row_spot  # we've found a dirty spot
        if lower_row >= 0:
            possible_lower_row_spot = contains_dirty_spot(matrix[lower_row])
            if possible_lower_row_spot != 'No Spot':
                return lower_row, possible_lower_row_spot

    return 'No Spot'


def contains_dirty_spot(row: list):
    """ given a list, this function returns the index of a dirty spot in the array, otherwise
        returns 'No Spot' """
    for idx, spot in enumerate(row):
        if spot == 'd':
            return idx

    return 'No Spot'


if __name__ == '__main__':
    main()