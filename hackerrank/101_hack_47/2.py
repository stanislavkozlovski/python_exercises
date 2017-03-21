n, p, q = [int(p) for p in input().split()]
p_nums = [int(p) for p in input().split()]
q_nums = [int(p) for p in input().split()]


max_num = 0
dicts = {}
for p in p_nums:
    for q in q_nums:
        # print((p+q) % n)
        sm = p+q
        if sm not in dicts:
            dicts[sm] = 0
        dicts[sm] += 1
        # if (p+q) < n:
        #     max_num = max(max_num, n %(p + q))
        # else:
        #     max_num = max(max_num, (p+q) % n)
sr = sorted(dicts.items(), key=lambda x:-x[1])
best_occur = sr[0][1]


def find_ct_till_mod(num, n):
    count = 0
    while num % n != 0:
        count += 1
        num += 1
    return count
max_num = 0
# print(sr)

max_nums = []
from collections import Counter
for num, occur in sr:

    # if occur != best_occur:
    #     break
    max_nums.extend([find_ct_till_mod(num, n) + 1] * occur)
    # if (num) < n:
    #     max_num = max(max_num, n -(num))
    # else:
    #     max_num = max(max_num, (num) % n)
most_cmn = Counter(max_nums).most_common()
bst_occ = most_cmn[0][1]
max_num = most_cmn[0][0]
sm = 0
for num, occ in most_cmn:
    if occ != bst_occ:
        break
    if num > max_num:
        if sm != 0:
            if sm % n != 0:
                sm += num
                max_num = num
        else:
            sm += num
            max_num = num
# print(most_cmn)
# print(most_cmn)
m_cmn_occ = most_cmn[0][1]
print(max_num)

if max_num == 0:
    raise Exception()