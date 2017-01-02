"""
An ugly 9/60 score solution done in the last 20 minutes of the HourRank16 competition
"""
import itertools
deleted_g = set()
graph = {}
dp = {}
n = int(input())


def dfs(node, wanted_node):
    m = 0
    visited = set()
    def _dfs(node, cost):
        nonlocal m, visited
        visited.add(node)
        if node == wanted_node:
            m = cost
        if node not in graph:
            return None
        for child in graph[node].keys():
            if child not in visited and child not in deleted_g:
                _dfs(child, cost + graph[node][child])
    _dfs(node, 0)

    return m

# build graph
for _ in range(n-1):
    node_1, node_2, edge = [int(part) for part in input().split()]
    if node_1 not in graph:
        graph[node_1] = {}
    if node_2 not in graph:
        graph[node_2] = {}
    graph[node_1][node_2] = edge
    graph[node_2][node_1] = edge

possible_scenarios = list(itertools.permutations(graph.keys()))

m = 0
for scenario in possible_scenarios:
    global deleted_g
    deleted_g = set()
    deleted = set()
    for node in scenario:
        for node_2 in graph.keys():
            if node_2 != node and node_2 not in deleted:
                val = None
                if node_2 in graph[node]:
                    val = graph[node][node_2]
                else:
                    val = dfs(node, wanted_node=node_2)
                m += val
        deleted.add(node)
        deleted_g = deleted

from math import factorial
print(int(((m/len(possible_scenarios))*factorial(n) % (10**9 + 9))))
