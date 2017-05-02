going_to_win = True

n = int(input())
nums = [int(p) for p in input().split()]

idx = 0
count = 0
while idx < len(nums):
    if idx == 0:
        idx = 1
    idx += nums[idx] + 1
    count += 1
print(count)