def find_num(n):
    start_num = 2
    while n % start_num != 0 or start_num > n:
        start_num += 1
    return n/start_num, start_num
def find_two_nums_eq(n):
    num_1, num_2 = 2, 2
n, k = [int(p) for p in input().split()]

nums = []

k_nums = [2 for _ in range(k)]
k_product = 2**k

if k_product > n:
    print(-1)
    exit()

found_answer = False
idx_to_inc = 0
while k_product < n:
    if idx_to_inc == len(k_nums):
        break
    old_product = k_product / k_nums[idx_to_inc]
    k_nums[idx_to_inc] += 1
    new_product = old_product * k_nums[idx_to_inc]
    if new_product > n:
        idx_to_inc += 1
    elif abs(new_product - n) < 0.1:
        found_answer = True
        break
    else:
        k_product = new_product
if found_answer:
    print(' '.join(str(p) for p in k_nums))
else:
    print(-1)