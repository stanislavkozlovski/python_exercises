n, a, b, q = [int(p) for p in input().split()]
nums = [int(p) for p in input().split()]

for _ in range(q):
    commands = [int(p) for p in input().split()]
    c = commands[0]
    if c == 1:
        c[commands[1]] = commands[2]
    else:
        l = commands[1]
        r = commands[2]
        nzz = nums[l:r+1]
        print('Yes')
    pass