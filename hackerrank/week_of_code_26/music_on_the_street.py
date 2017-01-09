n = int(input())
borders = [int(digit) for digit in input().split()]
miles, min_h, max_h = [int(digit) for digit in input().split()]
miles_per_step = miles // (n + 1)
index_to_start = 0

while miles_per_step < min_h:
    n -= 1
    index_to_start += 1
    miles_per_step = miles // (n + 1)

    if n == 1:
        # we need to start at the last border
        print(borders[-1])
        exit()


left_miles = miles - (miles_per_step * n)
miles_per_step += left_miles
if miles_per_step > max_h:
    miles_per_step = max_h

print(borders[index_to_start] - miles_per_step)