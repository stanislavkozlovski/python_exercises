#  https://www.hackerrank.com/challenges/angry-children
n = int(input())
k = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

sorted_nums = list(sorted(numbers))

idx = 0
min_difference = float('inf')

while True:
    if idx + (k-1) < len(sorted_nums):
        difference = sorted_nums[idx+(k-1)] - sorted_nums[idx]
        if difference < min_difference:
            min_difference = difference
    else:
        break
    idx += 1

print(min_difference)