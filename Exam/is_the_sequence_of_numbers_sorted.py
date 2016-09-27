"""
Given a sequence of numbers, determine if they are sorted.
If they are not sorted, return the first number that breaks the sort

sample input:
1 8 13 42 501 600 601 633

1  2  3 9   11   10    17   28
"""


# 100/100
def is_sorted(l: list):
    """
    Check if the list is sorted. if it is, return "SORTED", if it is not, return the index of the number that breaks the sort
    """
    for idx, num in enumerate(l):
        if idx is 0:
            continue
        elif l[idx-1]  <= num:
            continue

        return idx


    return "SORTED"


def main():
    try:
        # read the input and try to parse every element in the array into a number.
        numbers_list = [float(num) for num in list(input().split())]
        print(is_sorted(numbers_list))
    except Exception:
        print("INVALID INPUT")

if __name__ == "__main__":
    main()