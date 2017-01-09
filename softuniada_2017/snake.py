directions = {
    'right': (0, 1),
    'left': (0, -1),
    'forward': (-1, 0),
    'backward': (1, 0),
    'up': -1,
    'down': 1
}


def get_snake_coord(matrices):
    for m_idx, matrix in enumerate(matrices):
        for r_idx, row in enumerate(matrix):
            for c_idx, col in enumerate(row):
                if col == 's':
                    return m_idx, r_idx, c_idx

n = int(input())
matrices = []
for i in range(n):
    matrices.append([])
for idx in range(n):
    line = input().split(' | ')
    for i in range(n):
        matrices[i].append(list(line[i]))

snake_has_died = False


def traverse():
    m_idx, r_idx, c_idx = get_snake_coord(matrices)
    direction = input()
    points = 0
    global directions
    while True:
        if direction != 'end':
            c_args = input().split()
        steps = int(c_args[-2])
        if direction in ['down', 'up']:
            for i in range(steps):
                m_idx += directions[direction]
                if m_idx < 0 or m_idx >= len(matrices):
                    return True, points
                if matrices[m_idx][r_idx][c_idx] == 'a':
                    matrices[m_idx][r_idx][c_idx] = 'o'
                    points += 1
        else:
            if direction == 'end':
                return False, points
            for i in range(steps):
                r_to_add, c_to_add = directions[direction]
                r_idx, c_idx = r_idx + r_to_add, c_idx + c_to_add
                if r_idx < 0 or c_idx < 0 or r_idx >= len(matrices[m_idx]) or c_idx >= len(matrices[m_idx][r_idx]):
                    return True, points
                if matrices[m_idx][r_idx][c_idx] == 'a':
                    matrices[m_idx][r_idx][c_idx] = 'o'
                    points += 1

        direction = c_args[0]
    #  first do the steps

has_died, pointz = traverse()
print("Points collected: {}".format(pointz))
if has_died:
    print('The snake dies.')