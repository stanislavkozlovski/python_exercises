# https://www.hackerrank.com/challenges/bomber-man
from copy import deepcopy
BOMB_RANGES = [(0, -1), (0, 1), (1, 0), (-1, 0)]
MATRIX_LEN, COL_LEN = 0, 0


def build_matrix(row_count):
    matrix = []
    for _ in range(row_count):
        matrix.append(list(input()))
    return matrix


def bomb_matrix(matrix):
    """
    Detonates all the bombs in the matrix and adds bombs there where a bomb did not do damage,
    effectively simulating steps 3-4, where bomberman puts new bombs and the old ones explode,
    leaving only the new bombs that were not in range of the other bombs
    """
    new_matrix = deepcopy(matrix)
    for row_idx, row in enumerate(matrix):
        for col_idx, col in enumerate(row):
            if matrix[row_idx][col_idx] == 'O' or bomb_is_in_range(matrix, row, row_idx, col_idx):
                # there is a bomb in range which will destroy our bomb, so might as well put nothing
                new_matrix[row_idx][col_idx] = '.'
            else:
                new_matrix[row_idx][col_idx] = 'O'

    return new_matrix


def bomb_is_in_range(matrix, row, row_idx, col_idx):
    """ Returns a boolean value indicating if there is a neighbouring bomb"""
    for row_to_add, col_to_add in BOMB_RANGES:
        new_row = row_idx + row_to_add
        new_col = col_idx + col_to_add
        if (new_row < 0 or new_row >= MATRIX_LEN
           or new_col < 0 or new_col >= COL_LEN):
            # Out of bounds
            continue
        if matrix[new_row][new_col] == 'O':
            return True

    return False


def build_full_of_bombs_matrix(row_count, col_count):
    return [['O'] * col_count] * row_count


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def create_matrices(row_count, col_count):
    """
    Since we bomb periodically, there are a total of 4 different
    matrices that can be generated.
    1. The original matrix
    2. The matrix which is full of bombs
    3. The matrix from the first aftermath
    4. The matrix from the second aftermath (after 3)
    Since we know that, the only second we will have the original matrix will be the 1st second

    After that, the pattern is 2(full)/3(first aftermath)/2(full)/4(second aftermath) and on and on
    """
    original_matrix = build_matrix(row_count)
    matrix_after_first_bomb = bomb_matrix(original_matrix)
    matrix_after_second_bomb = bomb_matrix(matrix_after_first_bomb)
    full_of_bombs_matrix = build_full_of_bombs_matrix(row_count, col_count)

    return original_matrix, matrix_after_first_bomb, matrix_after_second_bomb, full_of_bombs_matrix


def get_result_matrix(wanted_second, original_matrix, first_aftermath_matrix, second_aftermath_matrix, full_matrix):
    """ Take the wanted second and return the resulting matrix"""
    if wanted_second == 1:
        print_matrix(original_matrix)
        return
    possible_matrices = [second_aftermath_matrix, full_matrix, first_aftermath_matrix, full_matrix]
    return possible_matrices[(wanted_second - 1) % 4]


def main():
    global MATRIX_LEN, COL_LEN
    row_count, col_count, wanted_second = [int(part) for part in input().split()]
    MATRIX_LEN, COL_LEN = row_count, col_count

    # create the possible matrices
    orig, aftermath_1, aftermath_2, full = create_matrices(row_count, col_count)
    # get the resulting matrix
    resulting_matrix = get_result_matrix(wanted_second, original_matrix=orig, first_aftermath_matrix=aftermath_1,
                                         second_aftermath_matrix=aftermath_2, full_matrix=full)

    print_matrix(resulting_matrix)

if __name__ == '__main__':
    main()
