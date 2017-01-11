def build_matrix(n, k, array):
    """
    Builds a NxK matrix, representing the given number and remainders
    n = 5, number = 12345, k=8
 n |   0  1  2  3  4  5  6  7  <== remainders k
 1    [1, 1, 0, 0, 0, 0, 0, 0]
 2    [0, 0, 0, 0, 0, 0, 0, 0]
 3    [0, 0, 0, 0, 0, 0, 0, 0]
 4    [0, 0, 0, 0, 0, 0, 0, 0]
 5    [0, 0, 0, 0, 0, 0, 0, 0]
    ]  ^---- answer will be here,
             the number of subsequences which have a remainder of 0 when divided by k (8)
             m[0]][0] is 1 because there an empty subsequence % 8 is always 0
             next, we make m[0][number[0]%k] += 1, which is
                number[0] % k = 1 % 8 = 1,
             m[0][1] += 1 => 0 + 1 = 1
    """
    matrix = []

    for _ in range(n):
        matrix.append([0] * k)

    matrix[0][0] += 1
    matrix[0][int(array[0]) % k] += 1

    return matrix


def fill_matrix(n, k, matrix, array, modulo):
    for i in range(1, n):
        ith_lucky_num = int(array[i])
        for j in range(k):
            matrix[i][j] = matrix[i-1][j]
        for j in range(k):
            new_j = ((j*10) + ith_lucky_num) % k
            matrix[i][new_j] = modulo_addition(  # add a+b while applying modulo
                                a=matrix[i][new_j],
                                b=matrix[i-1][j],
                                mod=modulo)
        if i-2 >= 0:
            matrix[i-2] = None  # clear some memory

    return matrix


def modulo_addition(a, b, mod) -> int:
    """
    Given two numbers, return their sum while applying modulo some number to them.
    This is done to prevent storage of big numbers.
    ex:
    if 1 + 2 = 3,
    we'd do ((1 % mod) + (2 % mod)) % mod
    """
    return ((a % mod) + (b % mod)) % mod


def main():
    n = int(input())
    lucky_num = input()
    modulo = 1000000007
    k = 8
    matrix = build_matrix(n,k, lucky_num)
    filled_matrix = fill_matrix(n, k, matrix, lucky_num, modulo)
    result = filled_matrix[-1][0] - 1  # we subtract 1 because we do not count the empty subsequence

    if result < 0:
        result = 0

    print(result % modulo)


if __name__ == '__main__':
    main()
