# https://www.hackerrank.com/challenges/maxsubarray
import sys


def get_max_arrays(array):
    max_non_cont_sum = -sys.maxsize
    max_cont_sum, current_sum = -sys.maxsize, 0

    for idx, num in enumerate(array):
        # get the max non-contiguous array sum
        if num > 0 or num > max_non_cont_sum:
            if max_non_cont_sum < 0:
                max_non_cont_sum = 0
            max_non_cont_sum += num
        # get the max contiguous array sum
        current_sum += num
        if current_sum > max_cont_sum or num > max_cont_sum:
            max_cont_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_cont_sum, max_non_cont_sum


def main():
    test_count = int(input())
    for _ in range(test_count):
        input()
        max_cont_sum, max_non_cont_sum = get_max_arrays([int(part) for part in input().split()])
        print("{} {}".format(max_cont_sum, max_non_cont_sum))


if __name__ == '__main__':
    main()
