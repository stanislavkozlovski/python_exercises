def find_max(limit, rate, amount):
    m = len(amount)
    # amount = reversed(sorted(amount))
    # limit = [(rat, 0) for rat in limit]
    cashback = 0
    for t_i, tans in enumerate(amount):
        max_rate = 0
        for idx, rt in enumerate(limit):
            t_rate = rate[idx*m + t_i]
            if t_rate > max_rate:
                max_rate = t_rate
                l_idx, left = idx, rt
        print(left)
        left -= tans
        left_tans = 0 if left >= 0 else abs(left)
        cashback += max_rate * tans
        while left_tans:
            max_rate = 0
            for idx, rt in enumerate(limit):
                t_rate = rate[idx * m + t_i]
                if t_rate > max_rate:
                    max_rate = t_rate
                    l_idx, left = idx, rt
            left -= tans
            left_tans = 0 if left >= 0 else abs(left)

            cashback += diff * tans

    return cashback
print(find_max([1000, 1000], [1,2], [58]))