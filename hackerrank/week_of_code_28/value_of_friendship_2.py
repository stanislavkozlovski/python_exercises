from sortedcontainers import sortedset
q = int(input())

for _ in range(q):
    n, m = [int(p) for p in input().split()]
    components = []
    friendships = sortedset.SortedSet(key=lambda x: x[0])
    for _ in range(m):
        friendships.add(tuple([int(p) for p in input().split()]))

    # print(friendships)
    # add the first friendship
    print(friendships)
    a, b = friendships.pop()
    components.append({a, b})
    i = 0
    overall_sum = 2
    current_sum = 2
    while len(friendships) > 0:
        i = len(components) - 1
        to_break = False
        while i >= 0:
            comp = components[i]
            to_remove = []
            for friendship in friendships:
                a, b = friendship
                if a in comp or b in comp and not (a in comp and b in comp):
                    to_remove.append(friendship)
                    current_sum -= len(comp) * (len(comp) - 1)
                    comp.add(a)
                    comp.add(b)
                    current_sum += len(comp) * (len(comp) - 1)
                    to_break = True
                    break
            if to_break:
                for t_r in to_remove:
                    friendships.remove(t_r)
                break
            i -= 1
        if not to_break:
            # create comp
            a, b = friendships.pop()
            components.append({a, b})
            current_sum += 2
        components.sort(key=lambda x: len(x))
        overall_sum += current_sum
        # print(friendships)
    print(overall_sum)