from dateutil import parser


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes.add(value)
            self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
          weight = current_weight + graph.distances[(min_node, edge)]
          if edge not in visited or weight < visited[edge]:
            visited[edge] = weight
            path[edge] = min_node

    return visited, path


input()
ROADS = Graph()
user_input = input()
while user_input != 'Records:':
    start_node, end_node, distance, limit = user_input.split()
    distance, limit = float(distance), float(limit)
    ROADS.add_node(start_node)
    ROADS.add_node(end_node)
    ROADS.add_edge(start_node, end_node, distance/limit)
    user_input = input()

user_input = input()
speeding = set()
shortest_distances = {}
plate_locations = dict()

while user_input != 'End':
    city, plate, time = user_input.split()
    date = parser.parse(time)
    if plate not in plate_locations:
        plate_locations[plate] = []
    plate_locations[plate].append((city, time))
    user_input = input()


for plate, locations in plate_locations.items():
    for idx, location in enumerate(locations):
        city, time = location
        time = parser.parse(time)
        if plate in speeding:
            break
        for idx_2 in range(idx+1, len(locations)):
            if plate in speeding:
                break
            new_city, new_time = locations[idx_2]
            new_time = parser.parse(new_time)
            time_travelling = (max(time, new_time)-min(time, new_time)).seconds / 3600

            if new_city not in shortest_distances:
                shortest_distances[new_city] = dijsktra(ROADS, new_city)[0]
            shortest_path = shortest_distances[new_city]
            if city not in shortest_path:
                continue
            min_time = shortest_path[city]
            if min_time > time_travelling:
                speeding.add(plate)
print('\n'.join(sorted(speeding)))

