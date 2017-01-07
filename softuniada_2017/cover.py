class Soldier:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        if other.x == self.x:
            return self.y > other.y
        return self.x > other.x

    def __lt__(self, other):
        if other.x == self.x:
            return self.y < other.y
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
class Shelter:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.soldiers = 0

    def __gt__(self, other):
        if other.x == self.x:
            return self.y > other.y
        return self.x > other.x

    def __lt__(self, other):
        if other.x == self.x:
            return self.y < other.y
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

s, m, c = [int(p) for p in input().split()]
soldies = []
shelters = []
for _ in range(s):
    x, y = [int(p) for p in input().split()]
    soldies.append(Soldier(x, y))
for _ in range(m):
    x, y = [int(p) for p in input().split()]
    shelters.append(Shelter(x, y))

sorted_solders = sorted(soldies)
sorted_shelters = sorted(shelters)


for s in sorted_solders:
    for sh in sorted_shelters:
        if sh.soldiers < c:
            sh.soldiers += 1
            break