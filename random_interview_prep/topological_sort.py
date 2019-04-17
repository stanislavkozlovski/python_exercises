from collections import deque
graph = {
    4: [0, 1],
    2: [3],
    5: [2, 0],
    1: [],  # add 4 here to create a cycle
    3: [1],
    0: []
}

other_graph = {
    4: [3, 2],
    3: [2, 1],
    2: [1],  # add 3 here to create a cycle
    1: []
}

tp_sorted_nodes = []
visited = set()
visited_this_iter = set()


def traverse_nodes(curr_node: int, graph: dict):
    """ Use DFS to traverse through the nodes """
    global tp_sorted_nodes, visited, visited_this_iter
    if curr_node in visited:
        return
    visited.add(curr_node)
    visited_this_iter.add(curr_node)
    for child in graph[curr_node]:
        if child in visited_this_iter and child not in tp_sorted_nodes:
            raise Exception('cycle!')
        traverse_nodes(child, graph)
    tp_sorted_nodes.append(curr_node)


def traverse_nodes_iterative(curr_node: int, graph: dict):
    """ DFS using a stack just for the sake of it """
    global tp_sorted_nodes, visited
    nodes_to_visit = deque()
    topologically_visited_nodes = deque()  # second stack to use as if backtracing
    nodes_to_visit.append(curr_node)
    tp_visited = []
    while len(nodes_to_visit) != 0:
        curr_node = nodes_to_visit.pop()
        if curr_node in visited:
            continue
        topologically_visited_nodes.append(curr_node)
        visited.add(curr_node)
        tp_visited.append(curr_node)
        for child in graph[curr_node]:
            nodes_to_visit.append(child)

    while len(topologically_visited_nodes) != 0:
        tp_sorted_nodes.append(topologically_visited_nodes.pop())


def topological_sort(graph: dict):
    global visited_this_iter, tp_sorted_nodes
    for node in graph.keys():
        traverse_nodes(node, graph)
        visited_this_iter = set()
    print(f'Topological sorting is {tp_sorted_nodes}')

topological_sort(other_graph)
