t_one, t_two, n = [int(p) for p in input().split()]
saved_t = {1: t_one, 2: t_two}


def calculate_fibonacci_t(n):
    global saved_t
    if n in saved_t:
        return saved_t[n]

    wanted_t = calculate_fibonacci_t(n-2) + pow(calculate_fibonacci_t(n-1), 2)
    saved_t[n] = wanted_t
    return wanted_t


print(calculate_fibonacci_t(n))
