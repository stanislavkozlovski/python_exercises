from fractions import gcd
dp = {}
def build_matrix(n, m, a, b):
    mat = []
    for idx in range(n):
        mat.append([])
        for idx_2 in range(m):
            mat[idx].append(gcd(a[idx], b[idx_2]))
    return mat

def aa(mat, min_r, min_c, max_r, max_c):
    if (min_r, min_c, max_r, max_c) in dp:
        return dp[(min_r, min_c, max_r, max_c)]
    st = set()
    for i in range(min_r, max_r+1):
        for j in range(min_c, max_c+1):
            st.add(mat[i][j])
    dp[(min_r, min_c, max_r, max_c)] = len(st)
    return len(st)

n, m, q = [int(p) for p in input().split()]
a = [int(p) for p in input().split()]
b = [int(p) for p in input().split()]
mat = build_matrix(n, m, a, b)
for _ in range(q):
    args = [int(p) for p in input().split()]
    min_r, min_c = args[0], args[1]
    max_r, max_c = args[2], args[3]
    print(aa(mat, min_r, min_c, max_r, max_c))