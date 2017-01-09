def get_two_elements_that_sum(desired_sum, arr):
    """ return the indexes of the two elements from an array which both sum to the desired sum"""
    for idx, el in enumerate(arr):
        for idx_2 in range(idx+1, len(arr)):
            el_2 = arr[idx_2]
            if el + el_2 == desired_sum:
                return idx, idx_2

test_case_count = int(input())

for _ in range(test_case_count):
    money = int(input())
    input()
    flavours_and_price = [int(p) for p in input().split()]
    flavour_one_idx, flavour_two_idx = get_two_elements_that_sum(desired_sum=money, arr=flavours_and_price)
    print('{} {}'.format(flavour_one_idx + 1, flavour_two_idx + 1))