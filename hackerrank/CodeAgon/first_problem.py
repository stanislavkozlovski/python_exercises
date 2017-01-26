t_x, t_y = [int(p) for p in input().split()]
dir_count = int(input())
for _ in range(dir_count):
    x, y = [int(p) for p in input().split()]
    t_x -= x
    t_y -= y

print('{} {}'.format(t_x, t_y))