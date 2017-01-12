q = int(input())
for _ in range(q):
    n, m = [int(p) for p in input().split()]
    graph = {
        # key: the node
        # value: list of  (using a list due to the references, where when I change one all the others change)
            #  1. A set oaf the nodes in the graph component
            #  2. The amount of edges.
    }
    for _ in range(m):
        node_a, node_b = [int(p) for p in input().split()]
        if node_a in graph:
            if node_b in graph:
                # both are in the graph
                if graph[node_a][0] == graph[node_b][0]:
                    graph[node_a][1] += 1
                else:
                    node_a_component, conns = graph[node_a]
                    node_b_component, conns_b = graph[node_b]
                    node_a_component.update(node_b_component)
                    graph[node_a][1] += conns_b + 1
                    for old_b in node_b_component:
                        graph[old_b] = graph[node_a]
            else:
                # add B to the graph
                node_a_component, conns = graph[node_a]
                node_a_component.add(node_b)
                graph[node_a][1] += 1
                graph[node_b] = graph[node_a]
        elif node_b in graph:
            # add A to the graph
            node_b_component, conns = graph[node_b]
            node_b_component.add(node_a)
            graph[node_b][1] += 1
            graph[node_a] = graph[node_b]
        else:
            # create a Component
            component = {node_a, node_b}
            ls = [component, 1]
            graph[node_a] = ls
            graph[node_b] = ls

    keys = set(graph.keys())
    overall_sum = 0
    component_sums = 0
    sorted_keys = [x for x,y in sorted(graph.items(), key=lambda x: x[1][1]-len(x[1][0]) - x[1][1])]
    # greedily add all the redundant edges at the end to get the maximum amount of each friend count
    redundant_edges_to_add = 0
    s_keys_idx = 0
    s_keys_len = len(sorted_keys)
    while len(keys) > 0:
        next_key = 0
        if s_keys_idx >= s_keys_len:
            break
        for idx in range(s_keys_idx, s_keys_len):
            key = sorted_keys[idx]
            if key in keys:
                next_key = key
                s_keys_idx = idx + (len(graph[key][0]) - 1)
                break

        current_sum = 0
        comp, conns = graph[next_key]
        component_length = len(comp)
        this_comp_sum = (component_length * (component_length-1))
        # update the keys
        keys = keys.difference(comp)

        # the count of edges that do not add new nodes to the graph
        redundant_edge_count = (conns - (component_length-1))
        if redundant_edge_count > 0:
            redundant_edges_to_add += redundant_edge_count
        # WARNING: MATH  -- ps: special thanks to wolframalpha
        current_sum = 1/3*(-1+component_length)*component_length*(1+component_length) + ((component_length-1)*component_sums)
        overall_sum += current_sum
        component_sums += this_comp_sum

    overall_sum += component_sums * redundant_edges_to_add
    print(int(overall_sum))
