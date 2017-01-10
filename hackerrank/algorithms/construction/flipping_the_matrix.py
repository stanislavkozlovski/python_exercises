#  https://www.hackerrank.com/challenges/flipping-the-matrix


def build_matrix(n):
    matrix = []
    for _ in range(2*n):
        matrix.append([int(p) for p in input().split()])

    return matrix


def get_max_upper_quadrant_elements_sum(matrix):
    overall_sum = 0
    # get the bounds
    max_row = len(matrix) // 2
    max_col = len(matrix[max_row]) // 2

    # traverse the matrix
    for idx in range(max_row):
        for col_idx in range(max_col):
            alt_row = len(matrix) - (idx+1)
            alt_col = len(matrix[max_row]) - (col_idx+1)
            # get the max element
            max_element = max(
                matrix[idx][col_idx],
                max(matrix[alt_row][col_idx],
                    max(matrix[idx][alt_col], matrix[alt_row][alt_col])
                    )
                )
            # add it to the overall sum
            overall_sum += max_element

    return overall_sum


def main():
    test_case_count = int(input())
    for _ in range(test_case_count):
        n = int(input())
        matrix = build_matrix(n)
        print(get_max_upper_quadrant_elements_sum(matrix))


if __name__ == '__main__':
    main()