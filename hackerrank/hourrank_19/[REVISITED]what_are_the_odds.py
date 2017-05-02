def get_nim_sum(stacks, start, end):
    if start == end:
        return stacks[start]
    nim_sum = stacks[start] ^ stacks[start+1]
    for i in range(start+2, end+1):
        nim_sum ^= stacks[i]
    return nim_sum

"""
The way to know if you can win is to convert the so-called nim_sum to 0 for your opponent.
A nim sum is the XOR of all the values.
The number of wayys to win is the number of ways to conver the nim_sum to 0, so we try all different possible ranges
i.e on an array of size 5 - 0-5, 1-5, 2-5, 3-5, 4-5, 0-4, 0-3, 0-2, 0-1, 1-4, 2-4, 3-4, 1-3, 1-2, 2-3
"""

_ = input()
def orig_solution():
    """ This is the solution I came up with myself, it's O(N^2) though and does not pass the tests """
    stacks = [int(p) for p in input().split()]
    # Find the number of 0 possible nim sums
    start, end = 0, len(stacks) - 1
    possible_ways = 0
    overall_nim_sum = get_nim_sum(stacks, 0, len(stacks) - 1)
    curr_nim_sum = get_nim_sum(stacks, start, end)

    while start <= end:
        if overall_nim_sum ^ curr_nim_sum == 0:
            possible_ways += 1

        # try all the possibilities from the start to the end
        temp_start = start + 1
        temp_nim_sum = curr_nim_sum
        while temp_start <= end:
            temp_nim_sum ^= stacks[temp_start - 1]  # remove the old sum
            if overall_nim_sum ^ temp_nim_sum == 0:
                possible_ways += 1
            temp_start += 1

        # try all the possibilities from the start to the end
        temp_end = end - 1
        temp_nim_sum = curr_nim_sum
        while temp_end >= start:
            temp_nim_sum ^= stacks[temp_end + 1]
            if overall_nim_sum ^ temp_nim_sum == 0:
                possible_ways += 1
            temp_end -= 1

        start += 1
        end -= 1
        curr_nim_sum ^= stacks[start - 1]
        curr_nim_sum ^= stacks[end + 1]

    print(possible_ways)

"""
AS far as I understand from the editorial:
We need to find two unique prefix/suffixes, whose sum is equal. Since, when they have equal sums their
overall sum is 0 and therefore everything between them is a valid choice to remove, leaving the overall nim sum as 0

[1,2,3,4,5]
inaccurate example:
if 1  ^ 2 == 4 and 4 ^ 5 == 4, then we can remove 3 from the array and be left with [1,2,4,5], whose nim sum would be 0
"""
stacks = [0] + [int(p) for p in input().split()]

# Holds the prefix nim sums of all indices
prefix_sums = {
    0: 0,
    1: stacks[1]
}

# calculates the prefix sums
for i in range(2, len(stacks)):
    prefix_sums[i] = prefix_sums[i - 1] ^ stacks[i]

# Will keep a count of the count of each unique sum we've encountered
sums_count = {

}
# Populate it with all the prefix sums
for i in range(len(stacks)-1):
    if prefix_sums[i] not in sums_count:
        sums_count[prefix_sums[i]] = 0
    sums_count[prefix_sums[i]] += 1

curr_suffix_sum = 0  # this will go through every possible suffix sum
possible_moves = 0
# Iterate in reverse
i = len(stacks) - 2
while i >= 0:
    if curr_suffix_sum in sums_count:  #  there is such a prefix sum already saved, therefore the range in between is a valid move
        possible_moves += sums_count[curr_suffix_sum]

    # We need to remove the prefix_sum that is up until this exact index,
    # otherwise further iterations will compare non-unique ranges: i.e 0:i, i-1:end
    if prefix_sums[i] in sums_count:
        if sums_count[prefix_sums[i]] > 1:
            sums_count[prefix_sums[i]] -= 1
        else:
            del sums_count[prefix_sums[i]]
    curr_suffix_sum ^= stacks[i + 1]

    i -= 1

print(possible_moves)
