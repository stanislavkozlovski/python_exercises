"""
Given a sequence of numbers, determine if they are sorted.
If they are not sorted, return the first number that breaks the sort

sample input:
1 8 13 42 501 600 601 633

1  2  3 9   11   10    17   28
"""

# TODO: Refactor a bit

# 100/100
def is_sorted(l: list):
    """
    Check if the list is sorted. if it is, return "SORTED", if it is not, return the index of the number that breaks the sort
    """
    for idx, num in enumerate(l):
        if not is_number(num):
            raise Exception  # stops the program and prints invalid input
        l[idx] = float(num)
        num = float(num)
        if idx is 0:
            continue



        if num >= 0 or l[idx-1] >= 0:
            if l[idx-1] <= num:
                continue
            else:  # not sorted
                return idx
        else:
            if num < 0 and l[idx-1] < 0:
                if l[idx-1] > num:
                    continue
                else:  # -1 -2 is not sorted in ascending order
                    return idx


    return "SORTED"

def is_number(num: int):
    """
    Check if what we're given is a number. If it is not, raise an exception
    """
    if str(num).lower() == 'nan':
        return False

    try:
        float(num)
        return True
    except ValueError:
        return False


def main():
    try:
        numbers_list = list(input().split())
        print(is_sorted(numbers_list))
    except Exception:
        print("INVALID INPUT")

if __name__ == "__main__":
    main()