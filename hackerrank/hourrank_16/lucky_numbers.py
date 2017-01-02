"""
A 25/25 score solution to the Lucky Numbers problem of the HourRank 16 competition
"""

def check_num(num):
    while num > 0:
        num -= 4
        if num % 7 == 0:
            return True
    return False

count = int(input())

for _ in range(count):
    num = int(input())
    if num % 4 == 0 or num % 7 == 0 or check_num(num):
        print('Yes')
    else:
        print('No')
