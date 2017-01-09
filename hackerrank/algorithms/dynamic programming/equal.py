from copy import deepcopy


def get_number_of_operations_to_reduce(array, idx, wanted_number):
    """
    Given a number at an index of an array and a wanted number, return the number of operations that are needed
    to reduce the array number to the wanted number by only removing 5, 2 or 1 per operation
    ex: arr = [1,2,3,4], idx = 3, wanted_number = 1: number at arr[idx] is 4. 4 can be reduced to 1 with 2 operations:
        4-2=2 2-1=1
    """
    number = array[idx]
    diff = number - wanted_number
    needed_operations = 0

    while diff != 0:
        needed_operations += 1
        if diff >= 5:
            array[idx] -= 5
        elif diff >= 2:
            array[idx] -= 2
        elif diff > 0:
            array[idx] -= 1
        diff = array[idx] - wanted_number

    return needed_operations


def minimize_chocolates(chocolates, minimize_to_zero=False):
    """
    Get the total number of operations needed to reduce the whole array to a certain value `min_chocolate`
    :param minimize_to_zero: A boolean indicating if we want to reduce the array to 0s
    """
    if minimize_to_zero:
        min_chocolate = 0
    else:
        min_chocolate = min(chocolates)
    operations_needed = {}  # holds a key of the number and the operations needed for it to reach min_chocolate
    overall_operations = 0

    for idx, choc in enumerate(chocolates):
        if choc != min_chocolate:
            if choc not in operations_needed:
                # calculate the number of needed operations to reach the number
                current_operations = get_number_of_operations_to_reduce(chocolates, idx, min_chocolate)
                overall_operations += current_operations
                operations_needed[choc] = current_operations
            else:
                chocolates[idx] = min_chocolate
                overall_operations += operations_needed[choc]
    return overall_operations


def main():
    """
    Since increasing every number except one is equivalent to decreasing one number, we will go with
    the latter to be more efficient

    We have 2 main strategies.
    1 - Get the minimum amount of chocolate in the chocolates and reduce every other chocolate to that amount
    2 - Reduce every chocolate to 0
    In most cases, 1 is more optimal, but in some strange edge cases like - [2,5,5,5,5,5] - reducing to 0 is better
    """
    test_cases = int(input())
    for _ in range(test_cases):
        _ = input()
        chocolates = [int(part) for part in input().split()]

        result_a = minimize_chocolates(deepcopy(chocolates))
        result_b = minimize_chocolates(chocolates, minimize_to_zero=True)

        print(min(result_a, result_b))


if __name__ == '__main__':
    main()


