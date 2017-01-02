from collections import deque


def bfs(graph, node):
    """
    Standard BFS to go through the whole graph component
    Returns the number of nodes in the component and a set of the visited nodes
    """
    visited_nodes = set()
    component_nodes_count = 0
    node_stack = deque()
    node_stack.append(node)

    while len(node_stack) > 0:
        node = node_stack.pop()
        if node in visited_nodes:
            continue
        component_nodes_count += 1
        if node in graph:
            node_stack.extend(graph[node])

        visited_nodes.add(node)

    return component_nodes_count, visited_nodes


def build_graph(line_count):
    graph = {}

    for _ in range(line_count):
        node_a, node_b = [int(part) for part in input().split()]
        if node_a not in graph:
            graph[node_a] = set()
        if node_b not in graph:
            graph[node_b] = set()
        graph[node_a].add(node_b)
        graph[node_b].add(node_a)

    return graph


def get_graph_components(graph, node_count):
    """ Get all the components from the graph, returning a list denoting the number of nodes in each component """
    components = []  # each index represents the number of nodes in a separate graph component
    visited_nodes = set()  # contains nodes we've visited so we don't traverse a traversed component twice
    for node in graph.keys():
        if node not in visited_nodes:
            nodes_count, visited = bfs(graph, node)
            components.append(nodes_count)
            for visited_node in visited:
                visited_nodes.add(visited_node)

    # add missing graph nodes as single components
    # these are nodes that are not connected to anybody and as such were not in the input
    for _ in range(node_count - len(graph.keys())):
        components.append(1)

    return components


def calculate_possible_pairs_between_components(components):
    """ Given the number of nodes in each graph component, calculate the number of
        possible combinations between each two components"""
    possible_pair_count = 0
    components_sum = components[0]  # dynamic optimization to store the sum of the components up to the i-th index
    for i in range(1, len(components)):
        possible_pair_count += components_sum * components[i]
        components_sum += components[i]

    return possible_pair_count


def main():
    astronauts_count, input_lines_count = [int(part) for part in input().split()]
    graph = build_graph(input_lines_count)
    components = get_graph_components(graph, astronauts_count)
    result = calculate_possible_pairs_between_components(components)
    print(result)
