# Inefficient solution for https://www.hackerrank.com/challenges/service-lane
_, test_cases = [int(part) for part in input().split()]
width = [int(part) for part in input().split()]

for _ in range(test_cases):
    start, end = [int(part) for part in input().split()]
    print(min(width[start:end+1]))