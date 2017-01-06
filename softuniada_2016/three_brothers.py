import copy
# arr = [1, 3, 4, 5, 3, 2]

def can_be_evenly_divided_in_three_parts(arr):
    arr_sum = sum(arr)
    if arr_sum % 3 != 0:
        return False
    target_sum = arr_sum//3
    sum_reached = []
    for i in range(target_sum+1):
        sum_reached.append([False]*(target_sum+1))
    sum_reached[0][0] = True
    for num in arr:
        for i in reversed(range(target_sum+1)):
            for j in reversed(range(target_sum+1)):
                if sum_reached[i][j]:
                    new_num = num + i
                    if new_num <= target_sum and not sum_reached[new_num][j]:
                        sum_reached[new_num][j] = True
                    new_num = num + j
                    if new_num <= target_sum and not sum_reached[i][new_num]:
                        sum_reached[i][new_num] = True
    return sum_reached[target_sum][target_sum]


test_case_count = int(input())
sums = {}
for _ in range(test_case_count):
    arr = [int(p) for p in input().split()]
    print('Yes' if can_be_evenly_divided_in_three_parts(arr) else 'No')
