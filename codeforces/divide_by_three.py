#  http://codeforces.com/contest/792/problem/C


def remove_with_remainder(num, num_sum, remainder):
    dig_idx = len(num) - 1
    to_remove = []
    found = True
    while num_sum % 3 != 0:
        if dig_idx < 0 or len(num) - len(to_remove) == 1:
            found = False
            break
        curr_num = int(num[dig_idx])
        if curr_num % 3 == remainder:
            to_remove.append(dig_idx)
            num_sum -= curr_num
        dig_idx -= 1

    return to_remove, found

def rebuild_string(num, indices):
    new_str = ''
    indices = set(indices)

    for idx in range(len(num)):
        if idx in indices:
            continue
        new_str += num[idx]

    while len(new_str) != 0 and new_str[0] == '0':
        if new_str == '0':
            return new_str
        new_str = new_str[1:]

    return new_str


"""
Really inefficient solution which passes all the tests! :)
"""
num = input()
num_sum = sum(int(p) for p in num)

dig_idx = len(num) - 1

remainder = num_sum % 3
to_print = None

if remainder == 0:
    to_print = num
elif len(num) == 1:
    to_print = -1
else:
    """
    Try to greedily remove every number with a remainder of 1 or 2
    The catch is that even if the whole remainder of the sum is 1,
        the right answer might require you to remove two digits whose remainders are 2
        i.e: 553 - sum is 13, whose remainder is 1, although the correct answer is 3, removing both 5s
    """
    idx_removed, is_valid = remove_with_remainder(num, num_sum, 1)
    idx_removed_2, is_valid_2 = remove_with_remainder(num, num_sum, 2)

    if not is_valid and not is_valid_2:
        to_print = -1
    elif is_valid and is_valid_2:
        # Find the better of the two
        str_1, str_2 = rebuild_string(num, idx_removed), rebuild_string(num, idx_removed_2)
        to_print = str_1 if len(str_1) > len(str_2) else str_2
    elif is_valid:
        to_print = rebuild_string(num, idx_removed)
    else:
        to_print = rebuild_string(num, idx_removed_2)

print(to_print)
