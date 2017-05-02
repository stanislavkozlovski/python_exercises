def df(node, graph):
    visited = set()
    longest_path = 0
    def d(node, graph):
        nonlocal  visited, longest_path
        pass
def get_with_one_child(graph):
    ks = []
    for key, values in graph.items():
        if len(values) == 1:
            ks.append(key)
    return ks

def get_with_three_child_or_more(graph):
    ks = []
    for key, values in graph.items():
        if len(values) >= 3:
            ks.append(key)
    return ks



going_to_win = True

n = int(input())
graph = {}
for i in range(n+1):
    graph[i] = []

for _ in range(n-1):
    a, b = [int(p) for p in input().split()]
    graph[a].append(b)
    graph[b].append(a)

one = get_with_one_child(graph)
three = get_with_three_child_or_more(graph)
import random
while three:
    first_child = graph[three[0]][random.randint(0, len(graph[three[0]]))]
    idx = 0
    while first_child == one[0]:
        idx += 1
        first_child = graph[three[0]][idx]
    graph[three[0]].remove(first_child)
    graph[first_child].remove(three[0])

    graph[one[0]].append(three[0])
    graph[three[0]].append(one[0])
    # three[0]
    # one[0]
    three = get_with_three_child_or_more(graph)
    one = get_with_one_child(graph)
print(graph)
