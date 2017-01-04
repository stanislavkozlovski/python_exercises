#  https://www.hackerrank.com/challenges/unbounded-knapsack/forum

test_case_count = int(input())

for _ in range(test_case_count):
    _, wanted_sum = [int(part) for part in input().split()]
    numbers = [int(part) for part in input().split()]

    """
    The approach is to keep an array of length wanted_sum + 1, where each index holds a boolean
    value indicating if the number can be calculated using the given numbers.

    This way, we know that the most right True value is the closest sum.
    To prevent another potential N loop, we keep the max true index.
    """
    can_be_reached = [False] * (wanted_sum + 1)
    can_be_reached[0] = True
    biggest_true_index = 0

    for num in numbers:
        for idx in range(num, len(can_be_reached)):
            if not can_be_reached[idx]:
                """
                ex: num = 7 => we want to reach 9(idx is the number we want to reach)
                    9-7 = 2. If 2 can be reached, then we can reach 9 with 7 + 2
                                can_be_reached[idx] = can_be_reached[idx-num]
                """
                can_be_reached[idx] = can_be_reached[idx-num]
            if idx > biggest_true_index and can_be_reached[idx]:
                biggest_true_index = idx

    # get minimum sum
    print(biggest_true_index)
