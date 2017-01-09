def substr(a, S):
    i = 0  # on a
    j = 0  # on S
    while i < len(a) and j < len(S):
        if a[i] == S[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(a):
        return True
    return False


q = int(input())

for _q in range(q):
    a = input().split()
    b = input().split()
    a_cap = []
    for color in a:
        if color.startswith('('):
            a_cap.append(color[1:-1])
        else:
            a_cap.append(color)
    # print(a_cap)
    a_onlycap = [c for c in a if not c.startswith('(')]

    if substr(b, a_cap) and substr(a_onlycap, b):
        print("true")
    else:
        print("false")
#
# for _ in range(int(input())):
#     a, b = input().split(), input().split()
#     print('true' if is_abbreviatable(a, b) else 'false')

