_ = input()
nums = [int(p) for p in input().split()]
aa = set(nums)
# P P Y
for idx, num in enumerate(nums):
    p = idx+1
    if p in aa:
        sec_p = nums.index(p) + 1
        if sec_p in aa:
            print(nums.index(sec_p) + 1)
