def build_matrix(n):
    mat = []
    for _ in range(n):
        mat.append([int(p) for p in input().split()])
    return mat
import sys
def find_best(l, needed):
    best = sys.maxsize
    b_idx = -1
    for idx in range(len(l)):
        capacity = l[idx][1]
        if capacity is None:
            continue
        if capacity >= needed:
            if capacity <= best:
                best = capacity
                b_idx = idx
        else:
            break
    if b_idx == -1:
        return None
    l[b_idx] = (None, None)
    return best

query = int(input())

for _ in range(query):
    n = int(input())
    occ = {}
    container_cap = {}
    max_num_c = n*n
    matrix = build_matrix(n)
    for container, r in enumerate(matrix):
        for typ, num in enumerate(r):
            if typ not in occ:
                occ[typ] = 0
            if container not in container_cap:
                container_cap[container] = 0
            occ[typ] += num
            container_cap[container] += num
    containers = list(reversed(sorted(container_cap.items(), key=lambda x: x[1])))
    numbbers = list(reversed(sorted(occ.items(), key=lambda x: x[1])))
    # print(containers)
    # print(numbbers)
    if len(numbbers) > len(containers):
        print('Impossible')
        continue
    IMPOSSIBLE = False
    for idx in range(len(containers)):
        con_cap = containers[idx][1]
        if con_cap is None:
            continue
        num_c = numbbers[idx][1]
        containers[idx] = (None, None)
        left = num_c - con_cap
        imp = False
        while left > 0:
            best_fit = find_best(containers, left)
            if best_fit is None:
                print('Impossible')
                imp = True
                IMPOSSIBLE = True

                break
            left -= best_fit
        if imp: break
        if num_c > con_cap:
            # LEFTOVER
            print('Impossible')
            IMPOSSIBLE = True
            break
    if not IMPOSSIBLE:
        print('Possible')
