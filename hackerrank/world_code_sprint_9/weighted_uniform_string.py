from string import ascii_lowercase
string = input()
weight = [ascii_lowercase.index(a) + 1 for a in string]
last_weight = None
# print(weight)
mod = []
last_sum = 0
for w in weight:
    if last_weight is None or w == last_weight:
        mod.append(last_sum)
        last_weight = w
        last_sum += w
    else:
        mod.append(last_sum)
        last_sum = w
        last_weight = w
mod.append(last_sum)
# print(mod)
mod = set(mod)
q_c = int(input())
for _ in range(q_c):
    inpudt = int(input())
    print('Yes' if inpudt in mod else 'No')