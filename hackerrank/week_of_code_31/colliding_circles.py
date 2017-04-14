from copy import deepcopy
from math import pi


def rich_mans_deepcopy(arr, ignore_idx: int=-1, indices: set()=set()):
    return [num for idx, num in enumerate(arr) if idx != ignore_idx and idx not in indices]


def calc_radius(day: int, saved_radii):
    global days, saved
    if days == day:
        # print(saved_radii)
        area = sum([pi * rad**2 for rad in saved_radii])
        if area in saved:
            print(saved_radii)
        saved.append(area)
        return area

    for idx in range(len(saved_radii)):
        number = saved_radii[idx]

        for idx_2 in range(idx+1, len(saved_radii)):
            new_radii = rich_mans_deepcopy(saved_radii, indices={idx, idx_2})
            new_radii.append(number+saved_radii[idx_2])
            calc_radius(day + 1, new_radii)


_, days = [int(p) for p in input().split()]
radii = [int(p) for p in input().split()]
saved = []
calc_radius(0, radii)

try:
    print(sum(saved)/len(saved))
except ZeroDivisionError:
    print(0)
