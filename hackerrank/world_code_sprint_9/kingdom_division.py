from copy import deepcopy

count = 0


def fork_graph(red_nodes, graph):
    red = deepcopy(red_nodes) + [True]
    blue = deepcopy(red_nodes) + [False]

    if len(red) == len(graph):
        validate(red, graph)
        validate(blue, graph)
    else:
        fork_graph(red, graph)
        fork_graph(blue, graph)


def validate(nodes, graph):
    global count
    # go through each node
    for i in range(1, len(nodes)+1):
        # if it does not have a neighbour node of the same color, break
        if not any(nodes[i-1] == nodes[j-1] for j in graph[i]):
            return
    count += 1


def build_tree(n):
    tree = {}

    for _ in range(n-1):
        a, b = [int(p) for p in input().split()]
        if a not in tree:
            tree[a] = []
        if b not in tree:
            tree[b] = []
        tree[a].append(b)
        tree[b].append(a)

    for i in range(1, n+1):
        if i not in tree:
            tree[i] = []
    return tree


def main():
    n = int(input())
    tree = build_tree(n)
    fork_graph([], tree)
    print(count)


if __name__ == '__main__':
    main()
