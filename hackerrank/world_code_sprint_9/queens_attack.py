n, obstacle_count = [int(p) for p in input().split()]
rows, cols = n, n
queen_row, queen_col = [int(p) for p in input().split()]
obstacles = set()
for _ in range(obstacle_count):
    x, y = [int(p) for p in input().split()]
    obstacles.add((x, y))

# TODO: Smarter obstacle detection via mmath???

moves = 0
# LEFT
for col in reversed(range(1, queen_col)):
    if (queen_row, col) in obstacles:
        break
    moves += 1
# RIGHT
for col in range(queen_col+1, rows+1):
    if (queen_row, col) in obstacles:
        break
    moves += 1
# UP
for row in range(queen_row+1, rows+1):
    if (row, queen_col) in obstacles:
        break
    moves += 1
# DOWN
for row in reversed(range(1, queen_row)):
    if (row, queen_col) in obstacles:
        break
    moves += 1

# DOWN-LEFT
cur_col, cur_row = queen_col, queen_row
while True:
    cur_col -= 1
    cur_row -= 1
    if (cur_row, cur_col) in obstacles or cur_row < 1 or cur_col < 1:
        break
    moves += 1

# DOWN-RIGHT
cur_col, cur_row = queen_col, queen_row
while True:
    cur_col += 1
    cur_row -= 1
    if (cur_row, cur_col) in obstacles or cur_row < 1 or cur_col > cols:
        break
    moves += 1

# UP-LEFT
cur_col, cur_row = queen_col, queen_row
while True:
    cur_col -= 1
    cur_row += 1
    if (cur_row, cur_col) in obstacles or cur_row > rows or cur_col < 1:
        break
    moves += 1

# UP-RIGHT
cur_col, cur_row = queen_col, queen_row
while True:
    cur_col += 1
    cur_row += 1
    if (cur_row, cur_col) in obstacles or cur_row > rows or cur_col > cols:
        break
    moves += 1
print(moves)