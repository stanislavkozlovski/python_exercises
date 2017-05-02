dest_rod = []
mid_rod = []
start_rod = [3, 2, 1]


def sol(disk_num, dest_rod, mid_rod, start_rod):
    if disk_num == 1:
        dest_rod.append(start_rod.pop())
        return
    sol(disk_num - 1, dest_rod=mid_rod,
                      mid_rod=dest_rod,
                      start_rod=start_rod)
    print(mid_rod)
    dest_rod.append(start_rod.pop())
    sol(disk_num - 1, dest_rod=dest_rod,
                      mid_rod=start_rod,
                      start_rod=mid_rod)
sol(3, dest_rod, mid_rod, start_rod)
