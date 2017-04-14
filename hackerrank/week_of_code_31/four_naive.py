"""
A PriorityQueue implemented with a binary heap with the additional ability to modify a given element
Complexities:
    add: O(log(n))
    extract_min: O(log(n))
    modify_element: O(n + log(n))
    re_order_element: O(log(n))
"""

top_nominator = 0
top_denominator = 0

class Edge:
    def __init__(self, node_a, node_b, a, b):
        self.node_a = node_a
        self.node_b = node_b
        self.a = a
        self.b = b
        self.diff = abs(a-b)
        self.sm = a+b
        self.weight = a/b

    def __gt__(self, other):
        global top_denominator, top_nominator
        new_nom, new_denom = top_nominator + self.a, top_denominator + self.b
        new_nom2, new_denom2 = top_nominator + other.a, top_denominator + other.b
        return new_nom/new_denom < new_nom2/new_denom2

    def __hash__(self):
        return hash(str(self.node_a) + str(self.node_b) + str(self.weight) + str(self.a) + str(self.b))

    def __eq__(self, other):
        return self.node_a == other.node_a and self.node_b == other.node_b and self.weight == other.weight and self.a == other.a and self.b == other.b


    def __repr__(self):
        return '{} {} - {}({}/{})'.format(self.node_a, self.node_b, self.weight, self.a, self.b)

def build_graph(nodes, edges):
    graph = {node: [] for node in range(nodes)}
    for edge in edges:
        graph[edge.node_a].append(edge)
        graph[edge.node_b].append(edge)
    return graph


nodes, edge_count = [int(p) for p in input().split()]
edges = []
for _ in range(edge_count):
    node_a, node_b, a, b = [int(p) for p in input().split()]
    edges.append(Edge(node_a, node_b, a, b))

edges = build_graph(nodes, edges)
# start from A
max_pair = None
for node_a in reversed(range(nodes)):
    top_denominator = 0
    top_nominator = 0
    connected_set = {node_a}
    used_edges = []
    edges_to_add = []
    for edge in edges[node_a]:
        edges_to_add.append(edge)
    # PriorityQueue.put()
    # edges_to_add = PriorityQueue(elements=[edge for edge in edges[node_a]])

    while len(edges_to_add) > 0:
        edges_to_add = sorted(edges_to_add)
        min_edge = edges_to_add[0]
        if min_edge.node_a not in connected_set:
            connected_set.add(min_edge.node_a)

            for edge in edges[min_edge.node_a]:
                if edge.node_a not in connected_set or edge.node_b not in connected_set:
                    edges_to_add.append(edge)
            used_edges.append(min_edge)
            top_nominator += min_edge.a
            top_denominator += min_edge.b
        elif min_edge.node_b not in connected_set:
            connected_set.add(min_edge.node_b)

            for edge in edges[min_edge.node_b]:
                if edge.node_a not in connected_set or edge.node_b not in connected_set:
                    edges_to_add.append(edge)
            # edges_to_add.add_elements([edge for edge in edges[min_edge.node_b]  # add edges which make sense
            #                           if edge.node_a not in connected_set or edge.node_b not in connected_set])
            used_edges.append(min_edge)
            top_nominator += min_edge.a
            top_denominator += min_edge.b
        edges_to_add = edges_to_add[1:]

    if max_pair is None or max_pair[0]/max_pair[1] < top_nominator/top_denominator:
        max_pair = (top_nominator, top_denominator)
top_nominator, top_denominator = max_pair
from math import gcd
gcd_of_both = gcd(top_nominator, top_denominator)
print('{}/{}'.format(top_nominator//gcd_of_both, top_denominator//gcd_of_both))