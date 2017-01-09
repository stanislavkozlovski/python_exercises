def get_start_position(row):
    """ Return the index of the start position in the row, if it's there, otherwise return None"""
    for idx, el in enumerate(row):
        if el == 'M':
            return idx
    return None


def build_matrix(n):
    matrix = []
    start_row, start_col = -1, -1
    for row_idx in range(n):
        row = list(input())
        potential_start_col_position = get_start_position(row)
        if potential_start_col_position is not None:
            start_row, start_col = row_idx, potential_start_col_position
        matrix.append(row)

    return matrix, start_row, start_col


def dfs_matrix(matrix, start_row, start_col):
    total_wand_waves = 0
    visited = {(start_row, start_col)}

    def _dfs(row, col, wand_waves):
        nonlocal total_wand_waves, visited
        if matrix[row][col] == '*':
            total_wand_waves = wand_waves
            return

        can_move_up = row - 1 >= 0 and (row-1, col) not in visited and matrix[row-1][col] != 'X'
        can_move_down = row + 1 < len(matrix) and (row+1, col) not in visited and matrix[row+1][col] != 'X'
        can_move_left = col - 1 >= 0 and (row, col-1) not in visited and matrix[row][col-1] != 'X'
        can_move_right = col + 1 < len(matrix[row]) and (row, col+1) not in visited and matrix[row][col+1] != 'X'
        choice_count = can_move_left + can_move_right + can_move_down + can_move_up
        if choice_count >= 2:
            wand_waves += 1
        if can_move_up:
            visited.add((row-1, col))
            _dfs(row-1, col, wand_waves)
        if can_move_down:
            visited.add((row+1, col))
            _dfs(row+1, col, wand_waves)
        if can_move_left:
            visited.add((row, col-1))
            _dfs(row, col - 1, wand_waves)
        if can_move_right:
            visited.add((row, col+1))
            _dfs(row, col + 1, wand_waves)
    _dfs(start_row, start_col, 0)
    return total_wand_waves


def main():
    test_case_count = int(input())
    for _ in range(test_case_count):
        n, m = [int(p) for p in input().split()]
        matrix, start_row, start_col = build_matrix(n)
        wanted_wand_waves = int(input())
        needed_wand_waves = dfs_matrix(matrix, start_row, start_col)
        print('Impressed' if wanted_wand_waves == needed_wand_waves else 'Oops!')

if __name__ == '__main__':
    main()
