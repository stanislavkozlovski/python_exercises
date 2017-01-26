uniques = set()


def get_combinations(combination, b_radiuses, n_idx, n):
    global uniques
    # if n_idx == n:
    #     print(combination)
    #     uniques.add(tuple(combination))
    #     return
    #     # return tuple(combination)
    #
    # for idx in range(len(b_radiuses)):
    #     last_n_idx = n_idx-1
    #     if n_idx == 0:
    #         combination[n_idx] = (idx, 1)
    #     else:
    #         last_idx, count = combination[last_n_idx]
    #
    #         if last_idx == idx and count + 1 > b_radiuses[idx]:
    #             continue  # search for another fucker
    #         if last_idx == idx:
    #             combination[n_idx] = (idx, count + 1)
    #         else:
    #             combination[n_idx] = (idx, 1)
    #
    #     get_combinations(combination, b_radiuses, n_idx+1, n)

    for n_idx in range(n):
        for idx in range(len(b_radiuses)):
            while n_idx != n:
                while idx != len(b_radiuses) or n_idx != n:
                    last_n_idx = n_idx - 1
                    if n_idx == 0:
                        combination[n_idx] = (idx, 1)
                    else:
                        last_idx, count = combination[last_n_idx]
                        if last_idx == idx and count + 1 > b_radiuses[idx]:
                            idx += 1
                        if last_idx == idx:
                            combination[n_idx] = (idx, count + 1)
                        else:
                            combination[n_idx] = (idx, 1)
                    n_idx += 1


shelves_count = int(input())

for i in range(shelves_count):
    n, e = [int(p) for p in input().split()]
    b_radius = [int(p) for p in input().split()]
    if e == 1:
        if b_radius <= n:
            print(0)
            continue
        print(len(b_radius))
        continue
    n_idx = 0
    get_combinations([None]*n, b_radius, 0, n)
    print(len(uniques))
    print(uniques)
    uniques = set()
