"""
Consider an undirected graph consisting of N nodes where each node is labeled from 1 to N and the edge between
any two nodes is always of length 6. We define node S to be the starting position for a BFS.

Given  queries in the form of a graph and some starting node, S, perform each query by calculating the shortest distance
 from starting node S to all the other nodes in the graph. Then print a single line of N-1 space-separated integers
 listing node S's shortest distance to each of the N-1 other nodes (ordered sequentially by node number);
  if S is disconnected from a node, print -1 as the distance to that node.

Input Format

The first line contains an integer, Q, denoting the number of queries.
The subsequent lines describe each query in the following format:

    The first line contains two space-separated integers describing the respective values of N
    (the number of nodes) and M(the number of edges) in the graph.
    Each line I of the M subsequent lines contains two space-separated integers, U and V,
    describing an edge connecting node U to node V.
    The last line contains a single integer, S, denoting the index of the starting node.

Output Format:
For each of the Q queries, print a single line of N-1 space-separated integers denothing the shortest distances to
each of the N-1 other nodes from starting position S. These distances should bel istedn sequentially by
node number (i.e., 1, 2, ...., n), but should not include node S.
 If some node is unreachable from S, print -1 as the distance to that node
"""


def initialize_dictionary(node_count: int):
    graph = {}  # type: dict holding as key the node and as a value a hashset of all the nodes it's connected to
    shortest_paths = {}  # type: dict holding as key the node and as value the shortest distance to it
    # initialize nodes in the dictionaries
    for new_node in range(1, node_count+1):
        graph[new_node] = set()
        shortest_paths[new_node] = 0

    return graph, shortest_paths


def add_edges(graph, edge_count):
    ''' read the edges from the user input and add them to the graph'''
    # read edges
    for _ in range(edge_count):
        node_a, node_b = tuple(map(lambda x: int(x), input().split()))
        # add the connections
        graph[node_a].add(node_b)
        graph[node_b].add(node_a)

    # no need to return graph as it's passed by reference


def bfs(graph: dict, shortest_paths: dict, starting_index: int):
    ''' traverse the graph using breadth first searching and return a dictionary containing the
    shortest path for each node '''
    traversed_nodes = {starting_index}  # type: set holding each node we've traversed
    queue = list(graph[starting_index])

    while queue:
        node = queue.pop(0)
        # get the shortest path to the node by taking the parent with the shortest path
        for par in [par for par in traversed_nodes if par in graph[node]]:  # iterate through list of parents
            if shortest_paths[node] == 0 or shortest_paths[par] + 6 < shortest_paths[node]:
                shortest_paths[node] = shortest_paths[par] + 6

        traversed_nodes.add(node)
        # add the childs of the node that we have not traversed yet
        queue.extend([node_to_traverse for node_to_traverse in graph[node]
                      if node_to_traverse not in queue and node_to_traverse not in traversed_nodes])

    # again no need to return, what we change in shortest_paths here will be changed in the main function


def main():
    query_count = int(input())

    for _ in range(query_count):
        node_count, edge_count = tuple(map(lambda x: int(x), input().split()))
        graph, shortest_paths = initialize_dictionary(node_count)
        add_edges(graph, edge_count)

        starting_index = int(input())
        bfs(graph, shortest_paths, starting_index)

        # print results
        del shortest_paths[starting_index] # remove the starting node from our shortest paths for easy printing
        print(' '.join([str(shortest_paths[key]) if shortest_paths[key] != 0 else '-1'
                        for key in sorted(shortest_paths.keys())]))


if __name__ == '__main__':
    main()