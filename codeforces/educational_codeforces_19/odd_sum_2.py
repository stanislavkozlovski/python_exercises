input()
nums = [int(p) for p in input().split()]
max_sum = sum(nums)

sorted_nums = sorted(nums)

idx = 0
# get the smallest odd number to fix it :)
# 100 -99 -1
banned_idx = None
while max_sum % 2 == 0 and idx < len(sorted_nums):
    if sorted_nums[idx] % 2 != 0:
        max_sum -= sorted_nums[idx]
        banned_idx = idx
        break
    idx += 1

# remove all negative evens
idx = 0
while idx < len(sorted_nums) and sorted_nums[idx] < 0:
    if sorted_nums[idx] % 2 == 0:
        max_sum -= sorted_nums[idx]
    idx += 1

idx = 0
temp_sum = max_sum
while idx < len(sorted_nums) and sorted_nums[idx] < 0:
    if sorted_nums[idx] % 2 != 0 and banned_idx != idx:
        temp_sum -= sorted_nums[idx]
        if temp_sum % 2 != 0 and temp_sum > max_sum:
            max_sum = temp_sum
    idx += 1
if temp_sum % 2 != 0 and temp_sum > max_sum:
    max_sum = temp_sum


if max_sum % 2 != 0:
    print(max_sum)
else:
    print(-1)

# 2 -1 -3 -2