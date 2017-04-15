# Dynamic Programming bsed Python implementation of Maximum Sum Increasing
# Subsequence (MSIS) problem

# maxSumIS() returns the maximum sum of increasing subsequence in arr[] of
# size n
max_sum = -1
def maxSumIS(arr, n):
    global  max_sum
    max_even, max_odd = 0, 0
    msis = [0 for x in range(n)]
    msis_odd = [0 for x in range(n)]
    # Initialize msis values for all indexes
    for i in range(n):
        msis[i] = arr[i]
        msis_odd[i] = arr[i]

    # Compute maximum sum values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            new_sm = msis[j] + arr[i]
            new_sm_2 = msis_odd[j] + arr[i]
            if new_sm % 2 == 0 and new_sm > msis[i]:
                msis[i] = new_sm
            if new_sm_2 % 2 == 0 and new_sm_2 > msis[i]:
                msis[i] = new_sm_2
            if new_sm % 2 != 0 and new_sm > msis_odd[i]:
                msis_odd[i] = new_sm
            if new_sm_2 % 2 != 0 and new_sm_2 > msis_odd[i]:
                msis_odd[i] = new_sm_2

    # Pick maximum of all msis values
    # for i in range(n):
    #     if max_even < msis[i]:
    #         max = msis[i]
    #         if max % 2 != 0 and max > max_sum:
    #             max_sum = max
        # if max_odd < msis_odd[i]:
        #
        #     pass
    if len(msis_odd) == 0:
        max_sum = -1
    else:
        max_sum = max(msis_odd)


n = int(input())
arr = [int(p) for p in input().split()]
maxSumIS(arr, n)


print(max_sum)