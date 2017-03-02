class City:
    def __init__(self, height, lat, lon, points):
        self.height = height
        self.lat = lat
        self.lon = lon
        self.points = points

    def __lt__(self, other):
        return self.height < other.height

    def __repr__(self):
        return str(self.height)

    def is_in_range(self, other, max_lat, max_lon):
        return abs(self.lat - other.lat) <= max_lat and abs(self.lon - other.lon) <= max_lon

n, x, y = [int(p) for p in input().split()]
cities = []
for _ in range(n):
    cities.append(City(*[int(p) for p in input().split()]))
# print(list(sorted(cities)))

def trav_cities(start_idx, cities: [City]):
    idx = start_idx
    result = 0
    # if cities[start_idx].points <= 0:
    #     return 0
    while idx < len(cities):
        curr_city = cities[idx]
        result += curr_city.points
        # print(result)
        # get closest best city in range
        last_idx_2 = 0
        for idx_2 in range(idx+1, len(cities)):
            other_city = cities[idx_2]
            if other_city.points >= 0 and curr_city.is_in_range(other_city, x, y):
                # print(curr_city.points)
                # result += other_city.points
                last_idx_2 = idx_2
                break
        if last_idx_2:
            idx = last_idx_2
        else:
            idx += 1
    return result


sorted_cities = list(sorted(cities))

print(max([trav_cities(idx, sorted_cities) for idx in range(len(cities))]))
# print(trav_cities(0, ))