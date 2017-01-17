gcd_dp = {}




# def gcd(xa, xb):
#     """Calculate the Greatest Common Divisor of a and b.
#
#     Unless b==0, the result will have the same sign as b (so that when
#     b is divided by it, the result comes out positive).
#     """
#     if (xa, xb) in gcd_dp:
#         return gcd_dp[(xa, xb)]
#     if (xb, xa) in gcd_dp:
#         return gcd_dp[(xb, xa)]
#     gcddd = GCD(xb, xa % xb)
#
#     return gcddd
#     while xb:
#         xa, xb = xb, xa % xb
#     gcd_dp[(xa, xb)] = xa
#     gcd_dp[(xb, xa)] = xa
#     return xa
import functools


_ = input()
nums = [int(p) for p in input().split()]
maxx = 2 * 10**18

lcm = None
nums = list(sorted(nums))
if len(nums) == 1:
    print(nums[0])
    exit()
if len(nums) == 2:
    print(GCD(nums[0], nums[1]))
    exit()
dp = {}


for idx in range(len(nums)):
    if nums[idx] in dp:
        continue
    dp[nums[idx]] = True

    last_num = 0
    for idxd in range(1, len(nums)):
        if idxd == idx:
            continue
        if idxd - 1 == idx:
            if idxd - 1 > 1:
                xa = idxd - 2
            else:
                continue
        if not last_num:
        xa = new_nums[idxd-1]
        xb = new_nums[idxd]

        if (xa, xb) in gcd_dp:
            xa = gcd_dp[(xa, xb)]
            continue
        if (xb, xa) in gcd_dp:
            xa = gcd_dp[(xb, xa)]
            continue
        while xb:
            xa, xb = xb, xa % xb
        gcd_dp[(xa, xb)] = xa
        gcd_dp[(xb, xa)] = xa
        last_num = xa
    a = new_nums[-1]

    if a == 0:
        continue
    if nums[idx] % a != 0 and a > 1 and a <maxx :
        print(a)
        break
