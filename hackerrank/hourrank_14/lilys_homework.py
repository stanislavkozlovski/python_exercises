def min_swaps(nums):
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
_ = input()
numbers = [int(p) for p in input().split()]
print(min_swaps(numbers))

"""
// Function returns the minimum number of swaps
// required to sort the array
int minSwaps(int arr[], int n)
{
    int ans = 0;

    // Traverse array elements
    for (int i = 0; i < n; i++)
    {
        // already swapped and corrected or
        // already present at correct pos
        if (vis[i] || arrPos[i].second == i)
            continue;

        while (!vis[j])
        {
            vis[j] = 1;

            // move to next node
            j = arrPos[j].second;
            cycle_size++;
        }

        // Update answer by adding current cycle.
        ans += (cycle_size - 1);
    }

    // Return result
    return ans;
}
"""