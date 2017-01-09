class Zone:
    def __init__(self, typ, x, y, w, h, p):
        self.typ = typ
        self.x = x
        self.x2 = x + w
        self.y = y
        self.y2 = y + h
        self.price_per_min = p
        self.zones = []

    def add_zone(self, x, y):
        self.zones.append((x, y))

    def __str__(self):
        return 'Zone Type: {0}; X: {1}; Y: {2}; Price: {3:.2f}'.format(
            self.typ, self.x, self.y, self.price_per_min
        )

zone_count = int(input())
zones = []
for _ in range(zone_count):
    zone_args = [p.replace(',', '') for p in input().split()]
    zone_name = zone_args[0][:-1]
    # print(zone_name)
    x, y, w, h, p = [float(p) for p in zone_args[1:]]
    zones.append(Zone(zone_name, x, y, w, h, p))

coords = [c.split(', ') for c in input().split('; ')]
coords = [(int(x), int(y))for x, y in coords]
wanted_x, wanted_y = [int(p) for p in input().split(', ')]
seconds = int(input())
for x,y in coords:
    for zone in zones:
        if zone.x <= x <= zone.x2 and zone.y <= y <= zone.y2:
            zone.add_zone(x, y)
            break
from math import ceil

clos_price, clos_time = 101013510, 15014051041
clos_zone = None
for zone in zones:
    closest_distance = 1431414134
    closest_zone = None
    for x, y in zone.zones:
        distance = abs(x - wanted_x) + abs(y - wanted_y)
        if distance <= closest_distance:
            closest_zone = (x, y)
            closest_distance = distance
    # print(closest_zone)
    # print(closest_distance)
    blocks_to_walk = (closest_distance-1) * 2
    seconds_needed = blocks_to_walk*seconds
    minutes_needed = ceil(seconds_needed / 60)
    price = minutes_needed * zone.price_per_min
    if clos_price > price:
        clos_price = price
        clos_time = seconds_needed/60
        clos_zone = Zone(typ=zone.typ, x=closest_zone[0], y=closest_zone[1], w=0, h=0, p=price)
    elif clos_price == price:
        if seconds_needed/60 < clos_time:
            clos_price = price
            clos_time = seconds_needed / 60
            clos_zone = Zone(typ=zone.typ, x=closest_zone[0], y=closest_zone[1], w=0, h=0, p=price)

print(clos_zone)
