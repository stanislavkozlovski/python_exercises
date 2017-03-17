n = int(input())
unset_bits = 0
while n:
    if (n & 1) == 0:
        unset_bits += 1
    n = n >> 1
print(1 << unset_bits)