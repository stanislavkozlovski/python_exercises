class Component:
    def __init__(self, node_a, node_b):
        self.nodes = {node_a, node_b}

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        yield from self.nodes.__iter__()

    def get_sum(self):
        node_count = len(self.nodes)
        return node_count * (node_count-1)

    def add_node(self, node):
        self.nodes.add(node)

    def has_node(self, node):
        """ Returns a boolean value indicating if the given node is present in the component """
        return node in self.nodes

    def consume_component(self, component: 'Component'):
        self.nodes = self.nodes.union(component.nodes)

q = int(input())
n, m = [int(p) for p in input().split()]
for _ in range(q):
    graph = {}
    overall_sum = 0
    # steps = []  # TEMP
    current_sum = 2
    for _ in range(m):
        node_a, node_b = [int(p) for p in input().split()]
        if node_a in graph and node_b in graph:
            if graph[node_a] == graph[node_b]:
                # Equal components, nothing to do
                current_sum -= graph[node_a].get_sum()
            else:
                # different components, need to union
                # don't merge the components, because we'd need to iterate over every element and change his reference
                # rather, just have both components hold the same values
                # let's hope it doesn't get too memory intensive EH
                node_a_component = graph[node_a]
                node_b_component = graph[node_b]
                current_sum -= graph[node_a].get_sum() + graph[node_b].get_sum()
                node_a_component.consume_component(node_b_component)
                for b_node in node_b_component:
                    graph[b_node] = node_a_component
                del node_b_component
                # node_b_component.nodes = node_a_component.nodes
        elif node_a not in graph and node_b not in graph:
            # create a Component
            component = Component(node_a, node_b)
            graph[node_a] = component
            graph[node_b] = component
        elif node_a not in graph and node_b in graph:
            current_sum -= graph[node_b].get_sum()

            graph[node_b].add_node(node_a)
            graph[node_a] = graph[node_b]
        elif node_a in graph and node_b not in graph:
            current_sum -= graph[node_a].get_sum()
            graph[node_a].add_node(node_b)
            graph[node_b] = graph[node_a]
        new_sum = graph[node_a].get_sum()
        # steps.append(new_sum)
        overall_sum += new_sum

    # print(steps)
    print(overall_sum)