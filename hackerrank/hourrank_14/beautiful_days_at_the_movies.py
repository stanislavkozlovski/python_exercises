i, j, k= [int(p) for p in input().split()]
print(sum([
              (day - int(''.join(reversed(str(day))))) % k == 0
    for day in
    range(i, j+1)
]))
