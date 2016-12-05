from math import factorial
n, m = [int(digit) for digit in input().split()]

print(factorial(n**m-1) % (10**9+7))
