class PLayer:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed


def create_matrix(row, cl):
    matrix = []
    for _ in range(row+1):
        matrix.append([0 for _ in range(cl+1)])
    return matrix
#
# PATHS = [(0, 1), (0,-1), (1, 0), (-1, 0)]
#
# def can_reach_in_time(matrix, s_x, s_y, hoop_x, hoop_y, tm):
#     from collections import deque
#     qq = deque()
#     visited = set()
#     visited.add((s_x, s_y))
#     qq.append((s_x, s_y))
#     qq.append("END")
#     prev = {(s_x, s_y): None}
#     steps = 1
#     while len(qq) != 0:
#         pair = qq.popleft()
#         if pair == 'END':
#             if len(qq) == 0:
#                 break
#             steps += 1
#             qq.append("END")
#             continue
#         s_x, s_y = pair
#         to_break = False
#         for r_add, c_add in PATHS:
#             new_row = s_x + r_add
#             new_col = s_y + c_add
#             if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
#                 if (new_row, new_col) not in visited:
#                     visited.add((new_row, new_col))
#                     qq.append((new_row, new_col))
#                     prev[(new_row, new_col)] = (s_x, s_y)
#                     if (new_row, new_col) == (hoop_x, hoop_y):
#                         to_break = True
#                         break
#         if to_break:break
#
#     # print(steps)
#     #
#     # print("STEPS")
#     return steps * tm
#     # best_path = []
#     # while True:
#     #     best_path.append((hoop_x, hoop_y))
#     #     if prev[(hoop_x, hoop_y)] is None:
#     #         break
#     #     hoop_x, hoop_y = prev[(hoop_x, hoop_y)]
#     # return (len(best_path)-1)
#     #
#     # start_time = 0
#     # best_path_baby = []
#     # for path in reversed(best_path):
#     #     x, y = path
#     #     best_path_baby.append((x, y, start_time))
#     #     start_time += tm

    # return best_path_baby
def find_best_path_to_hoop(s_x, s_y, hoop_x, hoop_y, tm):
    # from collections import deque
    # qq = deque()
    # visited = set()
    # visited.add((s_x, s_y))
    # qq.append((s_x, s_y))
    # prev = {(s_x, s_y): None}
    # while len(qq) != 0:
    #     s_x, s_y = qq.popleft()
    #     for r_add, c_add in PATHS:
    #         new_row = s_x + r_add
    #         new_col = s_y = c_add
    #         if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
    #             if (new_row, new_col) not in visited:
    #                 visited.add((new_row, new_col))
    #                 qq.append((new_row, new_col))
    #                 prev[(new_row, new_col)] = (s_x, s_y)
    #                 if (new_row, new_col) == (hoop_x, hoop_y):
    #                     break
    #
    # best_path = []
    # while True:
    #     best_path.append((hoop_x, hoop_y))
    #     if prev[(hoop_x, hoop_y)] is None:
    #         break
    #     hoop_x, hoop_y = prev[(hoop_x, hoop_y)]
    #
    # start_time = 0
    # best_path_baby = []
    # for path in reversed(best_path):
    #     x, y = path
    #     best_path_baby.append((x, y, start_time))
    #     start_time += tm
    best_path_baby = []
    tm = 1
    # if s_x != hoop_x and s_y != hoop_y:
    #     raise Exception()
    while s_x != hoop_x or s_y != hoop_y:
        # if s_x != hoop_x and s_y != hoop_y:
        #     raise Exception()
        if s_x != hoop_x:
            if hoop_x > s_x:
                s_x += 1
            else:
                s_x -= 1
        if s_y != hoop_y:
            if hoop_y > s_y:
                s_y += 1
            else:
                s_y -= 1
        best_path_baby.append((s_x, s_y, tm))
        tm += 1
    return best_path_baby

def get_distance(x, x_2):
    if x == x_2:
        return 0
    if x < 0 and x_2 < 0:
        return max(abs(x), abs(x_2)) - min(abs(x), abs(x_2))
    elif x < 0 and x_2 >= 0:
        return abs(x) + x_2
    elif x >= 0 and x_2 < 0:
        return abs(x_2) + x
    else:
        return max(x, x_2) - min(x, x_2)
t = int(input())
for _ in range(t):
    hoop_x, hoop_y = [int(p) for p in input().split()]
    x, y, s = [int(p) for p in input().split()]

    players = []
    for _ in range(5):
        p_x, p_y, p_s = [int(p) for p in input().split()]
        player = PLayer(p_x, p_y, p_s)
        players.append(player)

    # for player in players:
    #     matrix[player.x][player.y] = player
    hoop_path = find_best_path_to_hoop(x, y, hoop_x, hoop_y, s)

    printed_no = False
    for hp_path_pair in hoop_path[:-1]:
        x, y, time = hp_path_pair
        to_break = False

        for pl in players:
            x_dist = get_distance(pl.x, x)
            y_dist = get_distance(pl.y, y)
            steps_needed = x_dist + y_dist
            if steps_needed < 0:
                raise Exception()
            if time >= steps_needed * pl.speed:
                print("NO")
                to_break = True
                break
        if to_break:
            printed_no = True
            break
    if not printed_no:
        print("YES")
