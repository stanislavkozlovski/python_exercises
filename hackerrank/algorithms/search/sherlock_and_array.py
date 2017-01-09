def has_equal_sums(arr):
    left_sum = 0
    right_sum = sum(arr)
    for i in arr:
        right_sum -= i

        if left_sum == right_sum:
            return True
        
        left_sum += i

    return False

test_case_count = int(input())
for _ in range(test_case_count):
    input()
    numbers = [int(p) for p in input().split()]
    print('YES' if has_equal_sums(numbers) else 'NO')
