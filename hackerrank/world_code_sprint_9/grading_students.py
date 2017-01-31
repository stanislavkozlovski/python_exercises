def next_mult(b):
    if b < 38:
        return b
    orig_b = b
    for i in range(2):
        b += 1
        if b % 5 == 0:
            return b
    return orig_b
n = int(input())

grades = []
for i in range(n):
    print(next_mult(int(input())))