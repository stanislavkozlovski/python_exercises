a = int(input())
nums = [int(p) for p in input().split()]

if (len(set(nums)) != len(nums)):
    print("NO")
else:
    print("YES")