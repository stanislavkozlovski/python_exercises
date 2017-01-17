n, k = [int(p) for p in input().split()]

if n < k:
    print(-1)
    exit()
left_n = n-2
left_k = k-2
if left_k == 0:
    print(-1)
    exit()
aa = [0] * left_k
idx = 0
while left_n > 0:
    aa[idx] += 1
    left_n -= 1
    idx += 1
    if idx >= len(aa):
        aa[0] += left_n
        break
# print(aa)
final = [1] + aa + [1]
# print(final)
edge_count = 0
# if 0 in final:
#     print(-1)
#     exit()
if len(final) == 2:
    print(final[0] * final[1])
    exit()
for idx in range(1, len(final)):
    edge_count += final[idx] * final[idx-1]

# if n ==
print(edge_count)