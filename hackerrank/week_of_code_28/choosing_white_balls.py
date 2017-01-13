def choose_balls(balls, n, max_op):
    saved_combinations = {}
    chances_to_get_in = {}
    max_operations = max_op

    def _choose_balls(balls: tuple, op):
        nonlocal max_operations
        if op == max_operations:
            return
        if balls in saved_combinations:
            return saved_combinations[balls]
        combinations = 0
        if len(balls) % 2 != 0:
            mid = len(balls) // 2
        else: mid = None
        for i in range(len(balls)):
            ball = balls[i]
            if ball == 'W':
                wb_c = balls.count('W')
                if mid is not None and i == mid and op + 1 != max_op:

                    if balls[i-1] == 'B':
                        n_i = i-1
                        left_balls = balls[:n_i] + balls[n_i + 1:]
                        if left_balls not in saved_combinations:
                            _choose_balls(left_balls, op + 1)
                        if left_balls not in chances_to_get_in:
                            chances_to_get_in[left_balls] = 0
                        chances_to_get_in[left_balls] += 1.5
                        # combinations -= 2
                    if balls[i + 1] == 'B':
                        n_i = i + 1
                        left_balls = balls[:n_i] + balls[n_i + 1:]
                        if left_balls not in saved_combinations:
                            _choose_balls(left_balls, op + 1)
                        if left_balls not in chances_to_get_in:
                            chances_to_get_in[left_balls] = 0
                        chances_to_get_in[left_balls] += 1.5
                        # combinations -= 2
                    continue
                    pass   # NO FEAR
                reversed_idx = len(balls) - i - 1
                add = 0
                if reversed_idx == i or balls[reversed_idx] == 'W':
                    combinations += 1
                    add = 1
                else:
                    combinations += 2
                    add = 2
                left_balls = balls[:i] + balls[i+1:]
                if left_balls not in chances_to_get_in:
                    chances_to_get_in[left_balls] = 0
                chances_to_get_in[left_balls] += add

                if left_balls not in saved_combinations:
                    _choose_balls(left_balls, op+1)
        saved_combinations[balls] = combinations / len(balls)
    _choose_balls(tuple(balls), 0)
    # print(saved_combinations)
    # print(chances_to_get_in)
    return saved_combinations, chances_to_get_in
    pass


#  Balls, BALLS?
n, k = [int(p) for p in input().split()]
balls = list(input())
sav, chances = choose_balls(balls, n, k)

sum = 0
sav = sorted(sav.items(), key=lambda x: -len(x[0]))
# print(sav)
# print(chances)
for comb, chance_to_pick_a_white_ball in sav:
    if comb in chances:
        # print("{COMB} -> {a}".format(COMB=comb, a=chances[comb]/(len(comb)+1)))
        sum += chance_to_pick_a_white_ball * (chances[comb] / (len(comb) + 1))
    else:
        sum += chance_to_pick_a_white_ball
print(sum)