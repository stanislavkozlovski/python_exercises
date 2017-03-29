#  https://www.hackerrank.com/challenges/torque-and-development
from collections import deque


def build_map(city_count, road_count):
    """ Builds a graph which denotes the connections between cities"""
    map = {}
    for city in range(1, city_count+1):
        map[city] = set()

    for _ in range(road_count):
        city_a, city_b = [int(p) for p in input().split()]
        map[city_a].add(city_b)
        map[city_b].add(city_a)

    return map


def find_component(map, city):
    cities_to_visit = deque()
    cities_to_visit.append(city)
    visited = set()

    while cities_to_visit:
        city = cities_to_visit.popleft()
        visited.add(city)
        for con_city in map[city]:
            if con_city not in visited:
                visited.add(con_city)
                cities_to_visit.append(con_city)

    return visited


"""
Within a network of a city, you have two options for minimal cost:
    1. Build a single library and connect all the cities
    2. Build a library at every city
So:
    Find the network of each city.
    Compare both prices:
        1 library + city_count-1 roads
        city_count libraries
    Add the minimal one
"""
query_count = int(input())

for query in range(query_count):
    overall_city_count, overall_road_count, library_cost, road_cost = [int(p) for p in input().split()]

    map: dict = build_map(overall_city_count, overall_road_count)
    visited = set()
    overall_cost = 0
    for city in range(1, overall_city_count+1):
        if city not in visited:
            component = find_component(map, city)
            visited.update(component)
            city_count = len(component)
            road_count = city_count - 1
            if road_count == 0:
                # There is a city that is not connected to anything, we must build a library there
                overall_cost += library_cost
            else:
                # Check if its cheaper to build a library at each city or one library and connect each city
                one_library_all_roads_cost = library_cost + (road_count * road_cost)
                library_in_every_city_cost = library_cost * city_count
                overall_cost += min(one_library_all_roads_cost, library_in_every_city_cost)

    print(overall_cost)
