n = int(input())

are_valid = [True for _ in range(n)]
nums = [None for _ in range(n)]

# read input
to_check = {}
for idx in range(n):
    num, left, right = [int(p) for p in input().split()]
    nums[idx] = num
    # if left != -1