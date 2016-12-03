from math import sin


def get_numbers(num):
    nums = set()
    if num == 3:
        return [(1, 1, 1)]
    for first in range(1, num - 2):
        for second in range(1, first + 1):
            third = num - (first + second)
            pair = tuple(sorted((first, second, third)))
            if pair in nums:
                break
            if third >= 1:
                nums.add(pair)
            else:
                break
    return nums


num = int(input())

print(format(round(max([sum([sin(p1), sin(p2), sin(p3)]) for p1, p2, p3 in get_numbers(num)]), 9), '.9f'))
