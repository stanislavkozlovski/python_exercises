
def add(votes, count, idx):
    if len(count) <= idx:
        return
    count[votes[idx]] += 1

def remove(votes, count, idx):
    if len(count) <= idx:
        return


    count[votes[idx]] -= 1

from math import sqrt
block = None
class Query:
    def __init__(self, l, r, x, idx):
        self.l = l
        self.r = r
        self.x = x
        self.idx = idx
    def __lt__(self, other):
        if self.l//block != other.l//block:
            return self.l//block < other.l//block
        return self.r < other.r

    def __hash__(self):
        return hash(str(self.l) + str(self.r) + str(self.x) + str(self.idx))

    def __eq__(self, other):
        return self.l == other.l and self.r == other.r and self.x == other.x and self.idx == other.idx


def solution(queries, votes, query_order):
    """
    Use Mo's algorithm
    """
    global block
    curr_l, curr_r = 0, 0
    count = [0 for _ in range(len(votes))]
    from math import sqrt
    block = int(sqrt(len(votes)))
    queries = sorted(queries)
    query_results = [None for _ in range(len(queries))]

    for query in queries:
        l, r, x = query.l, query.r, query.x

        while curr_l < l:
            remove(votes, count, curr_l)
            curr_l += 1
        while curr_l > l:
            add(votes, count, curr_l-1)
            curr_l -= 1
        while curr_r <= r:
            add(votes,count,curr_r)
            curr_r += 1
        while curr_r > r+1:
            remove(votes,count,curr_r-1)
            curr_r -= 1
        query_results[query_order[query]] = get_ans(count, wanted=x)
    for res in query_results:
        print(res)
def get_ans(count, wanted):
    for idx, c in enumerate(count):
        if c == wanted:
            return idx
    return -1
t = int(input())

for _ in range(t):
    n = int(input())
    student_votes = [int(vote) for vote in input().split()]
    # votes = {idx: 0 for idx in range(n)}
    group_count = int(input())
    queries = []
    orig_query_order = {}
    for idx in range(group_count):
        query_obj = Query(*[int(p) for p in input().split()], idx)
        orig_query_order[query_obj] = idx
        queries.append(query_obj)
    solution(queries, student_votes, orig_query_order)
