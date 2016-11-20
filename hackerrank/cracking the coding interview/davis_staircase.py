steps = {1: 1, 2: 2, 3: 4}


def main():
    staircase_count = int(input())
    for _ in range(staircase_count):
        print(get_steps(int(input())))


def get_steps(n):
    if n in steps:
        return steps[n]
    else:
        steps[n] = get_steps(n-1) + get_steps(n-2) + get_steps(n-3)
    return steps[n]


if __name__ == '__main__':
    main()