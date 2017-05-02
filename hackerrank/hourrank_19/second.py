def is_valid(balls):
    if not balls:
        return 0
    nim_sum = balls[0]
    for i in balls[1:]:
        nim_sum ^= i
    return nim_sum


n = int(input())
balls = [int(p) for p in input().split()]
sums_up_to = [0 for ball in balls]
sums_down_to = [0 for ball in balls]

curr_sum = 0
nim_sum = balls[0]
sums_up_to[0] = balls[0]
for idx, i in enumerate(balls[1:]):
    nim_sum ^= i
    sums_up_to[idx+1] = nim_sum

nim_sum = balls[-1]
sums_down_to[-1] = balls[-1]
for idx in reversed(range(len(balls[:-1]))):
    i = balls[idx]
    nim_sum ^= i
    sums_down_to[idx] = nim_sum
# print(sums_up_to, sums_down_to)
wins = 0
for b in range(len(balls)):
    for e in range(b, len(balls)):
        rem_indices = list(range(len(balls)))[:b] + list(range(len(balls)))[e+1:]
        # print(b, e)
        if sums_up_to[b-1] ^ sums_down_to[e] == 0:
        # if is_valid([balls[idx] for idx in rem_indices]) == 0:
            wins += 1
print(wins)