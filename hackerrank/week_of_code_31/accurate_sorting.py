# https://www.hackerrank.com/contests/w31/challenges/accurate-sorting
def get_right_indices(nums: list) -> dict:
    """
    Given a list of integers, sort them
        and return a dictionary which denotes the rightful index of each number in the sorted array
    ex: [3, 2, 0] = Sorted([0,2,3]) = Dict({ 0:0, 2:1, 3:2})
    """
    return {num: idx for idx, num in enumerate(list(sorted(nums)))}


def main():
    for q in range(int(input())):
        input()
        nums = [int(p) for p in input().split()]
        right_indices = get_right_indices(nums)
        can_be_sorted = True
        """
            If the numbers are distinct and
            if we know the index at which the number will be in a sorted version of the array,
            We can compare both indices and know that if their difference is more than one, the number cannot be sorted
            into its rightful place, since there's bound to be a number that's bigger than it by our limiting factor (1)
        """
        for idx, num in enumerate(nums):
            rightful_idx = right_indices[num]
            if abs(rightful_idx - idx) > 1:
                can_be_sorted = False
                break
        print('Yes' if can_be_sorted else 'No')

if __name__ == '__main__':
    main()
