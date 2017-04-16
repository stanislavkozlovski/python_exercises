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

class Edge:
    def __init__(self, node_a, node_b, a, b):
        self.node_a = node_a
        self.node_b = node_b
        self.a = a
        self.b = b
        self.weight = a/b

    def __lt__(self, other):
        # a1.a/x-a1.b>a2.a/x-a2.b
        # if self.weight == other.weight:
        #     return self.a < other.a
        # if (self.weight >= sort_point and other.weight < sort_point):
        #     return True
        # if self.weight < sort_point and other.weight >= sort_point:
        #     return False
        # if self.weight >= sort_point and other.weight >= sort_point:
        #     return self.weight > other.weight
        return self.a/sort_point-self.b > other.a/sort_point-other.b
        # return abs(self.a/sort_point-self.b) < abs(other.a/sort_point-other.b)
        # global sort_point
        # if self.weight > sort_point and other.weight < sort_point:
        #     return True
        # elif self.weight < sort_point and other.weight > sort_point:
        #     return False
        # return self.weight > other.weight

    def __hash__(self):
        return hash(str(self.node_a) + str(self.node_b) + str(self.weight) + str(self.a) + str(self.b))

    def __eq__(self, other):
        return self.node_a == other.node_a and self.node_b == other.node_b and self.weight == other.weight and self.a == other.a and self.b == other.b


    def __repr__(self):
        return '{} {} - {}({}/{})'.format(self.node_a, self.node_b, self.weight, self.a, self.b)



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
def prim(nodes, edges):
    global best_result
    node_a = 0
    connected_set = {node_a}
    used_edges = []
    edges_to_add = PriorityQueue()
    for edge in edges[node_a]:
        if (datetime.now() - start > timedelta(seconds=8)):
            if best_result is None:
                best_result = top_nominator/top_denominator, top_nominator, top_denominator
            print_results(best_result)
        edges_to_add.put(edge)


    top_nominator = 0
    top_denominator = 0
    while edges_to_add.qsize() > 0:
        if (datetime.now() - start > timedelta(seconds=8)):
            if best_result is None:
                best_result = top_nominator/top_denominator, top_nominator, top_denominator
            print_results(best_result)
        min_edge = edges_to_add.get()
        if min_edge.node_a not in connected_set:
            connected_set.add(min_edge.node_a)

            for edge in edges[min_edge.node_a]:
                if edge.node_a not in connected_set or edge.node_b not in connected_set:
                    edges_to_add.put(edge)
            used_edges.append(min_edge)
            top_nominator += min_edge.a
            top_denominator += min_edge.b
        elif min_edge.node_b not in connected_set:
            connected_set.add(min_edge.node_b)

            for edge in edges[min_edge.node_b]:
                if edge.node_a not in connected_set or edge.node_b not in connected_set:
                    edges_to_add.put(edge)
            used_edges.append(min_edge)
            top_nominator += min_edge.a
            top_denominator += min_edge.b

    return top_nominator/top_denominator, top_nominator, top_denominator
from queue import PriorityQueue

def kruskal(edges):
    global best_result
    top_nominator, top_denominator = 0, 0
    connected_nodes = set()
    used_edges = []
    parents = {}
    edge_idx = 0
    edges = sorted(edges)
    while edge_idx < len(edges):
        if (datetime.now() - start > timedelta(seconds=8)):
            if best_result is None:
                best_result = top_nominator/top_denominator, top_nominator, top_denominator
            print_results(best_result)
        edge = edges[edge_idx]
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

        edge_idx += 1
    # print(used_edges)
    return top_nominator/top_denominator, top_nominator, top_denominator

def build_graph(nodes, edges):
    graph = {node: [] for node in range(nodes)}
    for edge in edges:
        if edge.node_a == edge.node_b:
            continue
        graph[edge.node_a].append(edge)
        graph[edge.node_b].append(edge)
    return graph
from datetime import datetime, timedelta
start = datetime.now()

n, m = [int(p) for p in input().split()]
# nodes = {node: Node(node) for node in range(n)}
# edges = []
# for _ in range(m):
#     a, b, c, d = [int(p) for p in input().split()]
def print_results(best_result):
    _, nominator, denominator = best_result
    # print results
    from math import gcd

    gcd_of_both = gcd(nominator, denominator)
    print("{}/{}".format(
        nominator // gcd_of_both, denominator // gcd_of_both
    ))
    exit()
edges = []
for _ in range(m):
    node_a, node_b, a, b = [int(p) for p in input().split()]
    if node_a == node_b:
        continue
    edges.append(Edge(node_a, node_b, a, b))
edges = build_graph(n, edges)
    # from math import gcd
    # both= gcd(c, d)

    # edges.append(Edge(nodes[a], nodes[b], c, d))
best_result = None
lo = (n - 1) * (1 / (100 * (n - 1)))
hi = ((n - 1) * 100 / (n - 1)) + 1
while True:
    start_point = lo + (hi - lo) / 4
    mid_point = lo + (hi - lo) / 2
    end_point = hi - (hi - lo) / 4

    sort_point = start_point
    start_result = prim(n, edges)
    if best_result is None or best_result[0] < start_result[0]:
        best_result = start_result
    sort_point = mid_point
    mid_result = prim(n, edges)
    if best_result is None or best_result[0] < mid_result[0]:
        best_result = mid_result
    sort_point = end_point
    end_result = prim(n, edges)
    max_res = sorted([start_result, mid_result, end_result], key=lambda x: x[0])[-1]
    max_result = max_res[0]
    if best_result is None or best_result[0] < max_res[0]:
        best_result = max_res
    # print(f'Start: {start_point} Mid: {mid_point} End: {end_point}')
    # print(max_res)
    if hi-lo < 0.0001 or datetime.now()-start > timedelta(seconds=8):
        _, nominator, denominator = max_res if max_res[0] > best_result[0] else best_result
        # print results
        from math import gcd
        gcd_of_both = gcd(nominator, denominator)
        print("{}/{}".format(
            nominator//gcd_of_both, denominator//gcd_of_both
        ))
        break

    if start_result[0] == mid_result[0] and mid_result[0] == end_result[0]:
        sample_result = start_result[0]
        if sample_result >= 1/4 and sample_result <= 3/4:
            lo = 1/4
            hi = 3/4
        elif sample_result < 1/4:
            hi = 1/2
        else:
            lo = 1/2

        continue
    if start_result[0] >= mid_result[0] and start_result[0] >= end_result[0]:  # start result is biggest
        hi = mid_point
    elif end_result[0] >= mid_result[0] and end_result[0] >= start_result[0]:  # end result is biggest
        lo = mid_point
    elif mid_result[0] >= start_result[0] and mid_result[0] >= end_result[0]:  # mid result is biggest
        lo = start_point
        hi = end_point



    # print(max_res)
    # print(start_point, mid_point, end_point)