# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence

# construct the matrix
def build_matrix(arr, arr2):
    """
    Returns the appropriate matrix for the solution of this problem
    ex: arr1 = 'aba', arr2='arab'
    0 0 a b a
    0 0 0 0 0
    a 0 0 0 0
    r 0 0 0 0
    a 0 0 0 0
    b 0 0 0 0
    """
    matrix = [[0, 0] + arr]
    matrix.append([0]*(len(arr)+2))
    for i in range(len(arr2)):
        matrix.append([arr2[i], 0] + ([0]*len(arr)))

    return matrix


def fill_longest_common_matrix(matrix):
    for row_idx in range(2, len(matrix)):
        for col_idx in range(2, len(matrix[row_idx])):
            if matrix[0][col_idx] == matrix[row_idx][0]:
                matrix[row_idx][col_idx] = matrix[row_idx-1][col_idx-1] + 1
            else:
                matrix[row_idx][col_idx] = max(matrix[row_idx - 1][col_idx], matrix[row_idx][col_idx - 1])


def read_arrays():
    input()
    return [int(part) for part in input().split()], [int(part) for part in input().split()]


def reconstruct_longest_common_subsequence(matrix):
    lcs = []
    row_idx = len(matrix) - 1
    last_row = matrix[row_idx][1:]
    last_len = max(last_row)
    last_number_first_idx = last_row.index(last_len) + 1

    while matrix[row_idx - 1][last_number_first_idx] == last_len:  # find the top most cell with this length
        row_idx -= 1
    while last_len != 0:
        while matrix[row_idx-1][last_number_first_idx] == last_len:  # find the top most cell with this length
            row_idx -= 1
        last_number_first_idx = last_row.index(last_len) + 1


        lcs.append(str(matrix[row_idx][0]))
        # get the new row and length
        last_row = matrix[row_idx][1:]
        last_len = last_row[last_number_first_idx - 2]

    return ' '.join(reversed(lcs))


def main():
    arr1, arr2 = read_arrays()
    matrix = build_matrix(arr1, arr2)
    fill_longest_common_matrix(matrix)
    lcs = reconstruct_longest_common_subsequence(matrix)
    print(lcs)


if __name__ == '__main__':
    main()
