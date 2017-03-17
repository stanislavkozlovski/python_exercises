from fractions import gcd

def stupid_bruteforce(n):
    count = 0
    for k in range(1, n + 1):
        for i in range(1, k + 1):
            for j in range(i, k):
                if i * j == k and gcd(i, j) == 1:
                    count += 1
    return count


n = int(input())
count = 0
k = n
for i in range(1, k+1):
    for j in range(i, k):
        product = i*j
        if product > k:
            break
        if product <= k and i <= product and j < product:
            if gcd(i, j) == 1:
                count += 1

print(count)
