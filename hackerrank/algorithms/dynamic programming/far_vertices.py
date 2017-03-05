from collections import Counter

marked_nodes = set()


def build_graph(n) -> [[]]:
    """ Build a matrix representation of the graph """
    graph = []

    for i in range(n + 1):
        graph.append([float('inf') for _ in range(n + 1)])  # no initial path
        graph[i][i] = 0
    for _ in range(n - 1):
        a, b = [int(p) for p in input().split()]
        graph[a][b] = 1
        graph[b][a] = 1
    return graph


def floyd_warshall(graph):
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                new_dist = graph[i][k] + graph[k][j]
                if graph[i][j] > new_dist:
                    graph[i][j] = new_dist


def get_longest_path_len(graph):
    """ Return the longest path between two non-marked nodes in the graph """
    global marked_nodes
    longest_len = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i not in marked_nodes and j not in marked_nodes:
                dist = graph[i][j]
                if dist == float('inf'):
                    continue
                if dist > longest_len:
                    longest_len = dist
    return longest_len


def get_nodes_k_or_less(graph, k) -> Counter:
    """
    Returns a Counter object which holds the amount of K edges a given node has.
    """
    global marked_nodes
    nodes = []
    visited = set()

    for i in range(len(graph)):
        for j in range(len(graph)):
            if i not in marked_nodes and j not in marked_nodes and (i,j) not in visited:
                dist = graph[i][j]
                if dist == float('inf'):
                    continue
                if dist <= k:
                    nodes.extend([i, j])
                    visited.add((i, j))
                    visited.add((j, i))
    return Counter(nodes)


def get_nodes_with_given_len_edge(graph, lon_len) -> Counter:
    """
    Returns a Counter object which holds a node and the amount of edges that are of the given length for the given node
    """
    global marked_nodes
    edges = []
    visited = set()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i not in marked_nodes and j not in marked_nodes and graph[i][j] == lon_len and (i, j) not in visited:
                edges.extend([i, j])
                visited.add((i, j))
                visited.add((j, i))

    return Counter(edges)


def get_node_with_least_k_edges(nodes_k_edge_count: Counter, nodes: []):
    """ Given the K edge count for each node and a list of nodes, return the node from the nodes list which
    has the least K edges """
    min_edges = nodes_k_edge_count[nodes[0]]
    min_node = nodes[0]
    for edge in nodes:
        if nodes_k_edge_count[edge] < min_edges:
            min_edges = nodes_k_edge_count[edge]
            min_node = edge
    return min_node


def main():
    global marked_nodes
    n, k = [int(p) for p in input().split()]
    graph = build_graph(n)
    # Calculate the path from each node to each node
    floyd_warshall(graph)

    longest_len = get_longest_path_len(graph)
    while longest_len > k:
        # Get the number of K edges for each node
        nodes_k_edge_count = get_nodes_k_or_less(graph, k)
        # Get the nodes which have edges with the longest length and sort them
        most_common_edges = get_nodes_with_given_len_edge(graph, longest_len).most_common()
        _, most_common_count = most_common_edges[0]
        # Get the nodes which have the most edges with the longest length
        # ie {5: 3, 4:3, 2:3, 1:2} => Edges should be [5, 4, 2], since they all have the longest length 3
        edges_to_choose_from = [node for node, edge_count in most_common_edges if edge_count == most_common_count]

        # From those edges, pick the one which has the least valid K edges
        node_to_mark = get_node_with_least_k_edges(nodes_k_edge_count, edges_to_choose_from)
        marked_nodes.add(node_to_mark)
        longest_len = get_longest_path_len(graph)

    print(len(marked_nodes))

if __name__ == '__main__':
    main()
