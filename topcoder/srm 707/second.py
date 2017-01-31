from collections import deque
from copy import deepcopy

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
OPPOSITE = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}
def construct(board, k):
    if board[0][0] == '#':
        return ''
    matrix = deepcopy(board)
    steps = bfs(board)
    if steps[-1][-1] > k:
        return ''
    else:
        str_steps = reconstruct(steps)
        diff = k - len(str_steps)
        last = str_steps[-1]
        opposite = OPPOSITE[str_steps[-1]]
        if diff % 2 == 0:
            times = diff // 2
            str_steps += times * '{}{}'.format(opposite, last)
        else:
            return ''
            # if diff < 3:
            #     return ''
            # left = diff - 3
            # reserve = 3
            # times = left // 2
            # str_steps += times * '{}{}'.format(opposite, last)

        return str_steps

def is_valid(x, y, max_len):
    return x >= 0 and x < max_len and y >= 0 and y < max_len

def copy_m(board):
    new_b = []
    for row in board:
        new_b.append([None] * len(row))
    return new_b

def bfs(board):
    visited = {(0, 0)}
    steps_board = copy_m(board)
    x, y = 0, 0
    to_visit = deque()
    steps_board[0][0] = 0
    # to_visit.append((0, 0))
    to_visit.append((0, 1))
    to_visit.append((1, 0))
    to_visit.append((None, None))
    steps = 1
    while to_visit:
        x, y = to_visit.popleft()
        if x is None and y is None:
            steps += 1
            if len(to_visit) == 0:
                break
            to_visit.append((None, None))
            continue
        steps_board[x][y] = steps
        visited.add((x, y))
        for row, col in DIRECTIONS:
            new_x = x + row
            new_y = y + col
            if is_valid(new_x, new_y, len(board)) and (new_x, new_y) not in visited and board[new_x][new_y] != '#':
                visited.add((new_x, new_y))
                to_visit.append((new_x, new_y))
    # from pprint import pprint
    # pprint(steps_board)
    return steps_board

def reconstruct(board):
    path = ''
    x, y = len(board) - 1, len(board) - 1

    while (x, y) != (0, 0):
        dirs = []
        for addx, addy in DIRECTIONS:
            new_x, new_y = x + addx, y + addy
            if is_valid(new_x, new_y, len(board)) and board[new_x][new_y] is not None:
                dirs.append((board[new_x][new_y], new_x, new_y))
        dirs.sort(key=lambda x: x[0])
        min_dist, n_x, n_y = dirs[0]
        if n_x < x:
            path += 'D'
            pass
        elif n_x > x:
            path += 'U'
            pass
        elif n_y < y:
            path += 'R'
            pass
        elif n_y > y:
            path += 'L'
            pass
        x = n_x
        y = n_y
    return ''.join(reversed(path))
# print(construct(["...", ".#.", "..."], 6))
