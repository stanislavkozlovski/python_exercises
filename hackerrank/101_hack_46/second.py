num_comparisons = 0


def _non_random_quick_sort(array, start, end):
    global num_comparisons
    if end <= start:
        return
    num_comparisons += (end-start)

    pivot_idx = start
    pivot_item = array[pivot_idx]
    i, j = start + 1, start + 1

    has_moved = False
    while j <= end:
        if array[j] < pivot_item:
            has_moved = True
            array[i], array[j] = array[j], array[i]
            array[pivot_idx], array[i] = array[i], array[pivot_idx]
            pivot_idx = i
            i = pivot_idx + 1
        j += 1
    # if not has_moved:
    #     num_comparisons -= comps

    # recursion up until we hit partition every part
    _non_random_quick_sort(array, start, pivot_idx-1)  # do the same for the left part
    _non_random_quick_sort(array, pivot_idx+1, end)  # do the same for the right part


def non_random_quick_sort(array: list):
    _non_random_quick_sort(array, 0, len(array)-1)
    return array


from itertools import permutations
q = int(input())
for _ in range(q):
    c, comparisonz = [int(p) for p in input().split()]
    broke = False
    if c**2 < comparisonz:
        print(-1)
        continue
    non_random_quick_sort(list(reversed(list(range(1, c+1)))))
    worst_case = num_comparisons
    if worst_case < comparisonz:
        print(-1)
        continue
    elif worst_case == comparisonz:
        print(' '.join([str(p) for p in list(reversed(list(range(1, c+1))))]))
        continue
    num_comparisons = 0
    calculated = set()
    # print(list(permutations(list(range(1, c+1)))))
    for array in permutations(list(range(1, c+1))):
        # sorted_arr = list(sorted(nums))
        if array in calculated:
            continue
        calculated.add(array)
        non_random_quick_sort(list(array))
        # print(num_comparisons)
        if num_comparisons == comparisonz:
            print(' '.join([str(p) for p in array]))
            broke = True
            break
        num_comparisons = 0
    if not broke:
        print(-1)
"""
array = [i for i in range(1,11)]
"""
"""
array = [2,8,9,3,7,5,10,1,6,4]
"""
