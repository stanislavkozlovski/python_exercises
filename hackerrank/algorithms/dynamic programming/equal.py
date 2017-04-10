from copy import deepcopy


def get_number_of_operations_to_reduce(number, wanted_number):
    """
    Given a number at an index of an array and a wanted number, return the number of operations that are needed
    to reduce the array number to the wanted number by only removing 5, 2 or 1 per operation
    ex: arr = [1,2,3,4], idx = 3, wanted_number = 1: number at arr[idx] is 4. 4 can be reduced to 1 with 2 operations:
        4-2=2 2-1=1
    """
    diff = number - wanted_number
    needed_operations = 0

    while diff != 0:
        needed_operations += 1
        if diff >= 5:
            number -= 5
        elif diff >= 2:
            number -= 2
        elif diff > 0:
            number -= 1
        diff = number - wanted_number

    return needed_operations


def minimize_chocolates(chocolates, subtract_from_min=0):
    """
    Get the total number of operations needed to reduce the whole array to a certain value `min_chocolate`
    :param subtract_from_min: A number we want to subtract from our min value (see main() docstring)
    """
    min_chocolate = min(chocolates) - subtract_from_min

    operations_needed = {}  # holds a key of the number and the operations needed for it to reach min_chocolate
    overall_operations = 0

    for idx, choc in enumerate(chocolates):
        if choc != min_chocolate:
            if choc not in operations_needed:
                # calculate the number of needed operations to reach the number
                current_operations = get_number_of_operations_to_reduce(chocolates[idx], min_chocolate)
                overall_operations += current_operations
                operations_needed[choc] = current_operations
            else:
                overall_operations += operations_needed[choc]
    return overall_operations


def main():
    """
    Since increasing every number except one is equivalent to decreasing one number, we will go with
    the latter to be more efficient

    We have 2 main strategies.
    1 - Get the minimum amount of chocolate in the chocolates and reduce every other chocolate to that amount
    2 - Reduce every chocolate to 0
    3 - Reduce the minimum ammount by some and reduce all others to that
    In most cases, 1 is more optimal, but in some strange edge cases like - [2,5,5,5,5,5] - reducing to 0 is better
    But there are also edge cases like - 6 10 10 10 10 10, where reducing 6 to 5 and all 10s to 5 is the better approach
    """
    test_cases = int(input())
    for _ in range(test_cases):
        _ = input()
        chocolates = [int(part) for part in input().split()]

        result_a = minimize_chocolates(chocolates)
        result_b = minimize_chocolates(chocolates, subtract_from_min=min(chocolates))
        result_c = minimize_chocolates(chocolates, 1)
        result_d = minimize_chocolates(chocolates, 2)
        result_e = minimize_chocolates(chocolates, 5)


        print(min(min(min(min(result_a, result_b), result_c), result_d), result_e))


if __name__ == '__main__':
    main()


