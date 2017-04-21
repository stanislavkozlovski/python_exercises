string_count = int(input())

strings = [input() for _ in range(string_count)]

min_count = float('inf')
for curr_str in strings:
    round_count = 0
    for str_to_change in strings:
        if curr_str == str_to_change:
            continue
        curr_count = 0
        max_count = len(str_to_change)
        while str_to_change != curr_str:
            if curr_count == max_count:
                break
            str_to_change = str_to_change[1:] + str_to_change[0]
            curr_count += 1
        if curr_count == max_count and str_to_change != curr_str:
            print(-1)
            exit()
        round_count += curr_count
    if round_count < min_count:
        min_count = round_count

print(min_count)
