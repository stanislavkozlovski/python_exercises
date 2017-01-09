"""
An ugly 13.3/15 score solution to the problem Candy Piles of the
60 minute HourRank 16 competition.
"""
import sys
min_hap = int(input())
piles = [int(part) for part in input().split()]

min_num = sys.maxsize
last_min = sys.maxsize
amount = {}
for pile in piles:
    if pile == 0:
        print('0 {}'.format(len(piles)))
        exit()
    if pile <= min_num:
        if pile not in amount:
            amount[pile] = 0
        amount[pile] += 1
        if pile < min_num:
            last_min = min_num
        min_num = pile
    else:
        if pile < last_min:
            last_min = pile


first = None
if amount[min_num] > 1:
    first = min_num
    second = len(piles)
elif amount[min_num] == 1:
    second = 1
    if last_min != min_num and last_min < min_num * 2:
        first = last_min
    else:
        first = min_num * 2


print("{} {}".format(first, second))