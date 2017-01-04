#  https://www.hackerrank.com/challenges/coin-change
wanted_change = int(input().split()[0])
ways_to_reach_memo = {}  # key: number, value: number of ways you can reach it
coins = [int(coin) for coin in input().split()]
can_be_reached = [False] * (wanted_change + 1)
can_be_reached[0] = True
ways_to_reach_memo[0] = 1

for num in coins:
    for idx in range(num, len(can_be_reached)):
        new_idx = idx-num
        can_reach = can_be_reached[new_idx]
        if can_reach:
            if idx not in ways_to_reach_memo:
                ways_to_reach_memo[idx] = 0
            """
            looking at the example below, the number of ways we can reach 9 is increased
            by the number of ways we can reach 2
            """
            ways_to_reach_memo[idx] += ways_to_reach_memo[new_idx]
        if not can_be_reached[idx]:
            """
            ex: num = 7 => we want to reach 9(idx is the number we want to reach)
                9-7 = 2. If 2 can be reached, then we can reach 9 with 7 + 2
                            can_be_reached[idx] = can_be_reached[idx-num]
            """
            can_be_reached[idx] = can_reach

if wanted_change not in ways_to_reach_memo:
    print(0)
else:
    print(ways_to_reach_memo[wanted_change])