start_day, end_day, k = [int(part) for part in input().split()]

beautiful_days = 0

for day in range(start_day, end_day+1):
    reversed_day = int(str(day)[::-1])
    beautiful_days += not (abs(day - reversed_day) % k == 0)

print(beautiful_days)
