import sys


class StarCluster:
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
        self.stars = 1
        self.x_sum = x
        self.y_sum = y

    def add_star(self, x, y):
        self.stars += 1
        self.x_sum += x
        self.y_sum += y
        self.x = self.x_sum / self.stars
        self.y = self.y_sum / self.stars


cluster_count = int(input())
clusters = []
for _ in range(cluster_count):
    cluster_name, coords = input().split(' (')
    x, y = [int(cord) for cord in coords.replace(' ', '').replace(')', '').split(',')]
    cluster = StarCluster(x, y, cluster_name)
    clusters.append(cluster)

star = input()
clusters = sorted(clusters, key=lambda x: x.name.lower())

while star != 'end':
    coords = [[int(x) for x in st.replace('(', '').replace(')', '').split(', ')] for st in star.split(') (')]

    for x,y in coords:
        min_distance = sys.maxsize
        cluster = None
        for cluser in clusters:
            distance = abs(cluser.x-x) + abs(cluser.y-y)
            if distance <= min_distance:
                min_distance = distance
                cluster = cluser
        cluster.add_star(x, y)

    star = input()

clusters = sorted(clusters, key=lambda x: x.name.lower())

for cluster in clusters:
    print("{name} ({x}, {y}) -> {st_count} stars".format(
        name=cluster.name,
        x=round(cluster.x),
        y=round(cluster.y),
        st_count=cluster.stars
    ))
