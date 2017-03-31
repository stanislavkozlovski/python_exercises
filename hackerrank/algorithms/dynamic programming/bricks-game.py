#  https://www.hackerrank.com/challenges/play-game
import resource
import sys


# turn up memory and recursion limit
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

# TODO: Maybe store top tuple in DP
DP = {}


def play_game(bricks, n, take_count, our_sum, opp_sum, idx, our_turn=True):
    global DP
    orig_our, orig_opp = our_sum, opp_sum
    turn_info = (int(our_turn), idx, take_count)
    if idx >= n:
        return our_sum, opp_sum
    if turn_info in DP:
        # Return the overall sums
        return (our_sum + DP[turn_info][0], opp_sum + DP[turn_info][1])

    curr_sum = sum(bricks[idx:min(idx+take_count, n)])

    if our_turn:
        our_sum += curr_sum
    else:
        opp_sum += curr_sum

    # What we determine as optimal, i.e our sum or the opponent. depends on the turn
    sum_max_comp = 1 if our_turn else 0

    one_score = play_game(bricks, n, 1, our_sum, opp_sum, idx+take_count, not our_turn)
    two_score = play_game(bricks, n, 2, our_sum, opp_sum, idx + take_count, not our_turn)
    three_score = play_game(bricks, n, 3, our_sum, opp_sum, idx+take_count, not our_turn)
    optimal_move = max(three_score, max(one_score, two_score, key=lambda x: x[sum_max_comp]),
               key=lambda x: x[sum_max_comp])

    # Store the resulting sums from this point onwards
    DP[turn_info] = optimal_move[0] - orig_our, optimal_move[1] - orig_opp

    return optimal_move

for t in range(int(input())):
    n = int(input())
    nums = [int(p) for p in input().split()]
    DP = {}  # reset storage after each test case
    three_score = play_game(nums, n, 3, 0, 0, 0, True)
    one_score = play_game(nums, n, 1, 0, 0, 0, True)
    two_score = play_game(nums, n, 2, 0, 0, 0, True)
    print(max(three_score, max(one_score, two_score, key=lambda x: x[0]), key=lambda x: x[0])[0])