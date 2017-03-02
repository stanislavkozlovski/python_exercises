n, q = [int(p) for p in input().split()]
array = [int(p) for p in input().split()]

# PRECOMPUTE
max_dp = {}
min_dp = {}
differences = {}
for i in range(len(array)):
    for j in range(i, len(array)):
        if i == j:
            max_dp[(i, j)] = array[i]
            min_dp[(i, j)] = array[i]
            if 0 not in differences:
                differences[0] = 0
            differences[0] += 1
        else:
            if (i, j-1) in max_dp:
                max_num = max_dp[(i, j-1)] if max_dp[(i, j-1)] > array[j] else array[j]
                min_num = min_dp[(i, j-1)] if min_dp[(i, j-1)] < array[j] else array[j]
                max_dp[(i, j)] = max_num
                min_dp[(i, j)] = min_num
            else:
                raise Exception()
            difference = max_num - min_num
            if difference not in differences:
                differences[difference] = 0
            differences[difference] += 1
# print(matrix)
for _ in range(q):
    minn, maxx = [int(p) for p in input().split()]
    count = 0
    for i in range(minn, maxx+1):
        count += differences.get(i, 0)
    print(count)
    # print(len([None for _ in matrix if _[-1] >= minn and _[-1] <= maxx]))
    # print(differences)