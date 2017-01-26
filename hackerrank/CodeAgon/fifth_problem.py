from collections import deque

GRAY, BLACK = 0, 1

def topological(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order

query_count = 1
for _ in range(query_count):
    program_count, _ = [int(p) for p in input().split()]
    program_graph = {}
    for i in range(1, program_count+1):
        dependencies = [int(p) for p in input().split()]
        program_graph[i] = []
        if dependencies[0] == 0:
            pass
        else:
            program_graph[i] = list(reversed(sorted(dependencies[1:])))
    wanted_programs = [int(p) for p in input().split()]
graph = program_graph
print(program_graph)
print(topological(graph))