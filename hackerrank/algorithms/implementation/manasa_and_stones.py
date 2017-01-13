test_case_count = int(input())
for _ in range(test_case_count):
    stones_count = int(input())
    a = int(input())
    b = int(input())

    max_val = max(a, b)
    min_val = min(a, b)

    # find the maximum possible value made by all differences being the maximum
    # then start replacing each maximum difference with the minimum
    maximum_possible_sum = max_val * (stones_count-1)
    values = {maximum_possible_sum}
    for _ in range(1, stones_count):
        # simulating replacement of the maximum difference with the minimum
        maximum_possible_sum -= max_val - min_val
        values.add(maximum_possible_sum)
    # at the end, we have got all the unique values
    print(' '.join(str(a) for a in sorted(values)))