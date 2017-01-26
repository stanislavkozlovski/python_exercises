thief_max, crate_count = [int(p) for p in input().split()]
crates = []
for _ in range(crate_count):
    matchboxes, matches_in_box = [int(p) for p in input().split()]
    matches = matchboxes * matches_in_box
    crates.append((matchboxes, matches_in_box))

summ = 0
for matchboxes, matches in reversed(sorted(crates, key=lambda x: x[1])):
    if matchboxes < thief_max:
        summ += matchboxes * matches
        thief_max -= matchboxes
    elif matchboxes == thief_max:
        summ += matchboxes * matches
        break
    else:
        matchboxes -= thief_max
        summ += thief_max * matches
        break
print(summ)