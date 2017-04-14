"""
A PriorityQueue implemented with a binary heap with the additional ability to modify a given element
Complexities:
    add: O(log(n))
    extract_min: O(log(n))
    modify_element: O(n + log(n))
    re_order_element: O(log(n))
"""


class PriorityQueue:
    def __init__(self, elements=None):
        self._elements = []
        self.count = 0
        if elements is not None and isinstance(elements, list):
            for el in elements:
                self.add(el)

    def __len__(self):
        return self.count

    def __contains__(self, item):
        # O(N)
        return item in self._elements

    def __repr__(self):
        return '{type} with {el_count} elements.'.format(type=type(self).__name__, el_count=self.count)

    def add(self, value):
        """ Add the value at the end and heapify up from there """
        self._elements.append(value)
        new_value_idx = len(self._elements) - 1
        self._heapify_up(new_value_idx)
        self.count += 1

    def add_elements(self, elements: list):
        for el in elements:
            self.add(el)

    def extract_min(self):
        """ Remove the min element by placing the last element on it's place and heapifying down"""
        min_el = self._elements[0]
        last_idx = len(self._elements) - 1

        self._elements[0] = self._elements[last_idx]

        self._elements.pop()
        self._heapify_down(0)

        self.count -= 1

        return min_el

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx < 0 or parent_idx < 0:
            return
        if self._elements[parent_idx] > self._elements[idx]:
            # swap
            self._elements[parent_idx], self._elements[idx] = self._elements[idx], self._elements[parent_idx]
            # update indices
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx):
        """
        Heapify the value down by getting it's smaller child and swapping values. Then continue heapifying down
        until we find children that are not smaller than the value.
        """
        l_child_idx, r_child_idx = (idx*2) + 1, (idx*2) + 2

        if l_child_idx < len(self._elements):
            # get the index of the bigger child
            if r_child_idx < len(self._elements) and self._elements[r_child_idx] < self._elements[l_child_idx]:
                min_idx = r_child_idx
            else:
                min_idx = l_child_idx
            # check if the child is bigger than the value and stop
            if self._elements[min_idx] >= self._elements[idx]:
                return

            # swap
            self._elements[idx], self._elements[min_idx] = self._elements[min_idx], self._elements[idx]
            self._heapify_down(min_idx)

    def modify_element(self, old_value, new_value):
        """
        Modify an old value and re-order it in the heap
        O(N+log(N))
        """
        idx = self._elements.index(old_value)
        self._elements[idx] = new_value
        if new_value > old_value:
            self._heapify_down(idx)
        else:
            self._heapify_up(idx)

    def re_order_decreased_element(self, value):
        """
        Heapifies the given element up.
        This is typically done when the element has been changed, which, if you're calling this method,
        should be a reference type and should have been changed outside the PriorityQueue
        """
        idx = self._elements.index(value)
        self._heapify_up(idx)

    def re_order_increased_element(self, value):
        """
        Heapifies the given element down.
        This is typically done when the element has been changed, which, if you're calling this method,
        should be a reference type and should have been changed outside the PriorityQueue
        """
        idx = self._elements.index(value)
        self._heapify_down(idx)


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
        if self.weight == other.weight:
            # TODO: Look at global var and try to equal it
            # if self.a == other.b:
            #     return self.b > other.b
            if self.weight >= 1:
            # if self.weight == int(self.weight):
                return self.sm < other.sm
            return self.sm > other.sm
            # return self.sm > other.sm
        return self.weight < other.weight

    def __ge__(self, other):
        if self.weight == other.weight:
#            TODO: Look at global var and try to equal it
#             if self.a == other.b:
#                 return self.b >= other.b
            if self.weight >= 1:
            # if self.weight == int(self.weight):
                return self.sm < other.sm
            return self.sm > other.sm
        return self.weight < other.weight


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

node_a = 0
connected_set = {node_a}
used_edges = []
from queue import PriorityQueue
edges_to_add = PriorityQueue()
for edge in edges[node_a]:
    edges_to_add.put(edge)
# PriorityQueue.put()
# edges_to_add = PriorityQueue(elements=[edge for edge in edges[node_a]])
top_nominator = 0
top_denominator = 0
while edges_to_add.qsize() > 0:
    min_edge = edges_to_add.get()
    if min_edge.node_a not in connected_set:
        connected_set.add(min_edge.node_a)

        for edge in edges[min_edge.node_a]:
            if edge.node_a not in connected_set or edge.node_b not in connected_set:
                edges_to_add.put(edge)
        # edges_to_add.add_elements([edge for edge in edges[min_edge.node_a]  # add edges which make sense
        #                           if edge.node_a not in connected_set or edge.node_b not in connected_set])
        used_edges.append(min_edge)
        top_nominator += min_edge.a
        top_denominator += min_edge.b
    elif min_edge.node_b not in connected_set:
        connected_set.add(min_edge.node_b)

        for edge in edges[min_edge.node_b]:
            if edge.node_a not in connected_set or edge.node_b not in connected_set:
                edges_to_add.put(edge)
        # edges_to_add.add_elements([edge for edge in edges[min_edge.node_b]  # add edges which make sense
        #                           if edge.node_a not in connected_set or edge.node_b not in connected_set])
        used_edges.append(min_edge)
        top_nominator += min_edge.a
        top_denominator += min_edge.b


from math import gcd
gcd_of_both = gcd(top_nominator, top_denominator)
print('{}/{}'.format(top_nominator//gcd_of_both, top_denominator//gcd_of_both))