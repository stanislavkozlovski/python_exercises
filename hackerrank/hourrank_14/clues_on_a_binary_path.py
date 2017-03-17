
house_count, bidir_road_count, distance = [int(p) for p in input().split()]

matrix = []
for _ in range(house_count+1):
    matrix.append([float('inf') for _ in range(house_count + 1)])
for _ in range(bidir_road_count):
    u, v, w = [int(p) for p in input().split()]
    matrix[u][v], matrix[v][u] = w, w

def get_valid_indices(matrix, node):
    indices = []
    for idx, el in enumerate(matrix[node]):
        if el != float('inf'):
            indices.append(idx)
    return indices

steps_set = set()
dp_set = set()
curr_steps = []
def trav(matrix, start_node, steps, steps_str):
    global distance
    global steps_set
    global dp_set

    if steps == distance:
        if start_node != 1:
            steps_set.add(steps_str)
        return
    if (steps_str, start_node) in dp_set:
        return
    for idx in get_valid_indices(matrix, start_node):
        trav(matrix, idx, steps+1, steps_str + str(matrix[start_node][idx]))
    dp_set.add((steps_str, start_node))

trav(matrix, 1, 0, '')
print(len(steps_set))
