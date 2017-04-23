n = int(input())
a_nums = [int(p) for p in input().split()]
a_sum = sum(a_nums)
b_nums = [int(p) for p in input().split()]
b_sum = sum(b_nums)

used_nums = {0: {abs(a_nums[0]-b_nums[0])}

}
sums = {
    0: {'a': a_nums[0], 'b': b_nums[0]}
}
count = {
    0: 1
}
idx = 1

while idx <= (len(a_nums)//2 + 1):
    min_diff = float('inf')
    best_idx = idx
    curr_num = abs(a_nums[idx]-b_nums[idx])
    for j in range(0, idx):
        if curr_num in used_nums[j]:
            continue

        a_diff = max(a_sum - (sums[j]['a']*2), 0)
        b_diff = max(b_sum - (sums[j]['b']*2), 0)

        if a_diff + b_diff < min_diff:
            min_diff = a_diff = b_diff
            best_idx = j

    if best_idx == idx:
        used_nums[idx] = {abs(a_nums[idx]-b_nums[idx])}
        sums[idx] = {
            'a': a_nums[idx],
            'b': b_nums[idx]
        }
        count[idx] = 1
    else:
        new_set = {abs(a_nums[idx]-b_nums[idx])}
        new_set.update(used_nums[best_idx])
        used_nums[idx] = new_set
        sums[idx] = {
            'a': a_nums[idx] + sums[best_idx]['a'],
            'b': b_nums[idx] + sums[best_idx]['b']
        }
        count[idx] = 1 + count[best_idx]

    idx += 1

for k in sorted(list(sums.keys())):
    if sums[k]['a'] * 2 > a_sum and sums[k]['b'] * 2 > b_sum:
        print(count[k])
        print(' '.join(str(p) for p in used_nums[k]))
        exit()
