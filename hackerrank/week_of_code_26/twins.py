def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6

    return True

start, end = [int(digit) for digit in input().split()]
pairs = 0
for num in range(start, end+2):
    if is_prime(num):
        if num + 2 <= end and is_prime(num+2):
            pairs += 1
print(pairs)
