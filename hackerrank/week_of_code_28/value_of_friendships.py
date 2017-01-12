q = int(input())
for _ in range(q):
    n, m = [int(p) for p in input().split()]
    graph = {}
    for _ in range(m):
        node_a, node_b = [int(p) for p in input().split()]
        if node_a in graph and node_b in graph:
            if graph[node_a][0] == graph[node_b][0]:
                graph[node_a][1][0] += 1
            else:
                node_a_component, conns = graph[node_a]
                node_b_component, conns_b = graph[node_b]
                node_a_component.update(node_b_component)
                conns[0] += conns_b[0]
                node_b_component = node_a_component
                conns_b = conns
        elif node_a not in graph and node_b not in graph:
            # create a Component
            component = {node_a, node_b}
            conns = [1]
            graph[node_a] = component, conns
            graph[node_b] = component, conns
        elif node_a not in graph and node_b in graph:
            node_b_component, conns = graph[node_b]
            node_b_component.add(node_a)
            conns[0] += 1
            graph[node_a] = node_b_component, conns
        elif node_a in graph and node_b not in graph:
            node_a_component, conns = graph[node_a]
            node_a_component.add(node_b)
            conns[0] += 1
            graph[node_b] = node_a_component, conns


    keys = set(graph.keys())
    overall_sum = 0
    while len(keys) > 0:
        comp, conns = graph[keys.pop()]
        component_length = len(comp)
        orig_len = component_length
        different = (conns[0] - len(comp)) + 1
        if different > 0:
            overall_sum += different * (component_length * (component_length-1))
        while component_length > 1:
            overall_sum += component_length * (component_length-1)
            component_length-=1
        keys = keys.difference(comp)
    print(overall_sum)
