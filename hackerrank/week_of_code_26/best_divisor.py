"""
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers,
the one whose digits sum to a larger number is better than the other.
If the sum of digits is equal for both numbers, then she thinks the smaller number is better.
For example, Kristen thinks that 13 is better than 31 and that 12 is better than 11.

Given an integer, N, can you find the divisor of N that Kristin will consider to be the best?
"""


def get_best_divisor(n):
    if len(set(str(n))) == 1 and len(str(n)) > 3:
        return n
    max_sum, min_num = sum([int(digit) for digit in str(n)]), n
    for num in range(1, n // 2 + 2):
        if n % num == 0:
            current_sum = sum([int(digit) for digit in str(num)])
            if current_sum > max_sum:
                min_num = num
                max_sum = current_sum

    return min_num

n = int(input())


print(get_best_divisor(n))
