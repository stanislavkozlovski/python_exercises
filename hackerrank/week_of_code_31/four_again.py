class Node:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return self.__str__()
top_nominator, top_denominator = 0, 0
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
        if new_nom/new_denom == new_nom2/new_denom2:
            return new_denom > new_denom2
        return new_nom/new_denom < new_nom2/new_denom2

    def __hash__(self):
        return hash(str(self.node_a) + str(self.node_b) + str(self.weight) + str(self.a) + str(self.b))

    def __eq__(self, other):
        return self.node_a == other.node_a and self.node_b == other.node_b and self.weight == other.weight and self.a == other.a and self.b == other.b


    def __repr__(self):
        return '{} {} - {}({}/{})'.format(self.node_a, self.node_b, self.weight, self.a, self.b)

# build the hardcoded graph
n, m = [int(p) for p in input().split()]
nodes = {node: Node(node) for node in range(n)}
edges = []
for _ in range(m):
    a, b, c, d = [int(p) for p in input().split()]
    from math import gcd
    both= gcd(c, d)

    edges.append(Edge(nodes[a], nodes[b], c//both, d//both))


def find_root(node, parents):
    while node in parents and parents[node] != node:
        node = parents[node]

    return node

def have_equal_parents(parents: dict, node_a, node_b):
    return find_root(node_a, parents) == find_root(node_b, parents)

def inverse_tree(parents: dict, node):
    if parents[node] == node:
        return
    parent = parents[node]

    inverse_tree(parents, parent)

    parents[parent] = node


def kruskal(edges):
    global top_nominator, top_denominator
    connected_nodes = set()
    used_edges = []
    parents = {}
    while len(edges) > 0:
        edges = sorted(edges)
        edge = edges[0]
        if ((edge.node_a not in connected_nodes or edge.node_b not in connected_nodes)
                or not have_equal_parents(parents, edge.node_a, edge.node_b)):

            connected_nodes.add(edge.node_a)
            connected_nodes.add(edge.node_b)
            if edge.node_b not in parents:
                # node_b is not connected to anything
                parents[edge.node_b] = edge.node_a
                if edge.node_a not in parents:
                    parents[edge.node_a] = edge.node_a
            elif edge.node_a not in parents:
                # node a is not connected to anything
                parents[edge.node_a] = edge.node_b
                if edge.node_b not in parents:
                    parents[edge.node_b] = edge.node_b
            else:
                # change node_a's parent to node_b.
                # to do that, we first need to make node_a the root of its subtree, so we inverse its path
                # up until the root

                inverse_tree(parents, edge.node_a)
                parents[edge.node_a] = edge.node_b
            # print(edge.node_a, edge.node_b)

            used_edges.append(edge)
            top_nominator += edge.a
            top_denominator += edge.b

        edges = edges[1:]

    return used_edges


# def build_output_string(used_edges) -> str:
#     """ Build the given output string"""
#     edge_strings = []
#     overall_weight = 0
#     for edge in used_edges:
#         overall_weight += edge.weight
#         edge_strings.append(str(edge))
#
#     return f'Minimum spanning forest weight: {overall_weight}\n' + '\n'.join(edge_strings)

used_edges = kruskal(edges)
# print(build_output_string(used_edges))
# print(top_nominator, top_denominator)
from math import gcd
gcd_of_both = gcd(top_nominator, top_denominator)
print('{}/{}'.format(top_nominator//gcd_of_both, top_denominator//gcd_of_both))