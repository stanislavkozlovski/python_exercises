def floyd_warshall(graph, a, b):
    """
    Find the closest path from each node to each other node
    """
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                # if (i == a and b == j) or (j == a and b == i):
                #     continue
                if i == j:
                    graph[i][j] = 0
                    continue
                new_distance = graph[i][k] + graph[k][j]
                if new_distance < graph[i][j]:
                    graph[i][j] = new_distance


def read_input(n, m, k):
    """
    Read the input and build the graph, represented as a dictionary
    Also, return the wanted road, on which the point should be on
    """
    graph = []
    for i in range(n+1):
        graph.append([float('Inf') for _ in range(n+1)])

    saved_road = None
    for i in range(1, m+1):
        a, b, w = [int(p) for p in input().split()]
        graph[a][b] = w
        graph[b][a] = w
        if i == k:
            saved_road = (a, b)

    return graph, saved_road


def get_closest_nodes(a, b, graph, offset_a=0, offset_b=0):
    """
    Given two points in a graph,
        separate all nodes into two lists, where one is closer to A and the other to B
    """
    nodes_closer_to_a, nodes_closer_to_b = {a}, {b}
    max_a_dist, max_b_dist = offset_a, offset_b
    for node in range(1, len(graph)):
        if node != a and node != b:
            if graph[node][a]+offset_a < graph[node][b]+offset_b:
                dist = graph[node][a] + offset_a
                if max_a_dist < dist:
                    max_a_dist = dist
                nodes_closer_to_a.add(node)
            else:
                dist = graph[node][b] + offset_b
                if max_b_dist < dist:
                    max_b_dist = dist
                nodes_closer_to_b.add(node)

    return nodes_closer_to_a, nodes_closer_to_b, max_a_dist, max_b_dist


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = [int(p) for p in input().split()]
        graph, saved_road = read_input(n,m,k)

        # TODO: Floyd sometimes updates the saved_road by finding a new shorter path, IDK what to do
        floyd_warshall(graph, saved_road[0], saved_road[1])

        """
        For each possible integer P, find the one where the dist is minimized
        Then, putting an lower/upper bound p-1 and p+1, find each possible P with 1 decimal point, i.e 0.1, 0.2 where dist is minimized
        repeat until we get to 5 decimal points ie 0.00001, 0.00002, constantly updating when finding a min dist
        """
        nds_a, nds_b, max_a, max_b = get_closest_nodes(saved_road[0], saved_road[1], graph)
        max_dist_to_a, max_dist_to_b = max_a, max_b
        saved_road_dist = graph[saved_road[0]][saved_road[1]]
        ov_max_a, ov_max_b = max_dist_to_a, max_dist_to_b + saved_road_dist
        ov_max = max(max_a, max_b + saved_road_dist)
        chosen_point = 0
        for i in range(0, saved_road_dist+1):
            a_nds, b_nds, max_dist_to_a, max_dist_to_b = get_closest_nodes(saved_road[0], saved_road[1], graph, offset_a=i, offset_b=saved_road_dist - i)

            max_a = max_dist_to_a
            max_b = max_dist_to_b

            if max(max_a, max_b) < ov_max:
                # Found a new minimal max
                ov_max = max(max_a, max_b)
                ov_max_a, ov_max_b = max_a, max_b
                chosen_point = i

        for idx, dec_point in enumerate([0.1, 0.01, 0.001, 0.0001, 0.00001]):
            prev_dec_point = dec_point * 10
            min_point, max_point = max(chosen_point - prev_dec_point, 0), min(chosen_point + prev_dec_point, saved_road_dist)
            i = min_point
            while i <= max_point:
                *_, max_dist_to_a, max_dist_to_b = get_closest_nodes(saved_road[0], saved_road[1], graph,
                                                                     offset_a=i,
                                                                     offset_b=saved_road_dist - i)

                max_a = max_dist_to_a
                max_b = max_dist_to_b
                if max(max_a, max_b) < ov_max or (max(max_a, max_b) == ov_max) and (i < chosen_point):
                    # Found a new minimal max
                    ov_max = max(max_a, max_b)
                    ov_max_a, ov_max_b = max_a, max_b
                    chosen_point = i
                i += dec_point
                i = round(i, 5)

        print("{:.5f} {:.5f}".format(round(chosen_point, 5), round(max(ov_max_a, ov_max_b), 5)))

if __name__ == '__main__':
    main()

