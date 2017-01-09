# https://www.hackerrank.com/challenges/vertical-sticks


def calculate_ray_shot_value():
    """
    Because we have to calculate the ray shot value for every permutation, we can simply  get the expected value.
    We calculate the expected ray shot value for each part using Linearity of Expectation
    1. For each number, find the amount of numbers that are greater/equal to him
    ex: for [1,2,3,1] we would get [4, 2, 1, 4]  4 nums are greater/eq to 1 and etc
    2. Knowing the greater/eq number counts, we can get the expected ray value by
        getting the sum of each number+1 divided by the overall length+1
        [4, 2, 1, 4] +1 for each => SUM(5(length+1)/[5, 3, 2, 5]) => 6.16
    """
    _ = input()
    numbers = [int(num) for num in input().split()]
    # 1.
    # what we need to do for each number is calculate the amount of numbers that are greater/equal to him
    gt_number_occurrence = {}  # hold the greater number count for each number so that we don't have to recalculate
    greater_numbers_count = []  # list of the number of greater numbers for each number... WTF?
    for num in numbers:
        if num not in gt_number_occurrence:
            occurrence = len([_num for _num in numbers if _num >= num])
            gt_number_occurrence[num] = occurrence

        greater_numbers_count.append(gt_number_occurrence[num])

    # 2.
    modified_length = len(greater_numbers_count) + 1
    result = sum(modified_length/(gt_num_count + 1) for gt_num_count in greater_numbers_count)
    return result


def main():
    test_case_count = int(input())
    for _ in range(test_case_count):
        result = calculate_ray_shot_value()
        print("{:.2f}".format(result))


if __name__ == '__main__':
    main()