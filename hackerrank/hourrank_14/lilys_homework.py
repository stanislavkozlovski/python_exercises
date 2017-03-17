def normal_sort_swaps(nums):
    pairs = [(el, idx) for idx, el in enumerate(nums)]
    pairs = list(sorted(pairs, key=lambda x: x[0]))
    vis = [False for i in range(len(pairs))]
    ans = 0

    for i in range(len(pairs)):
        if (vis[i] or pairs[i][1] == i):
            continue
        cycle_size = 0
        j = i
        while (not vis[j]):
            vis[j] = 1
            j = pairs[j][1]
            cycle_size += 1
        ans += (cycle_size - 1)

    return ans


def reverse_sort_swaps(nums):
    pairs = [(el, idx) for idx, el in enumerate(nums)]
    pairs = list(reversed(sorted(pairs, key=lambda x: x[0])))
    vis = [False for i in range(len(pairs))]
    ans = 0

    for i in range(len(pairs)):
        if vis[i] or pairs[i][1] == i:
            continue
        cycle_size = 0
        j = i
        while (not vis[j]):
            vis[j] = 1
            j = pairs[j][1]
            cycle_size += 1
        ans += (cycle_size - 1)

    return ans


_ = input()
numbers = [int(p) for p in input().split()]
# Print the minimum number of swaps it takes to sort the array in either descending or ascending
print(min(normal_sort_swaps(numbers), reverse_sort_swaps(numbers)))
