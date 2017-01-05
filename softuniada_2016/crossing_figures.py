
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.ax = x - radius
        self.bx = x + radius
        self.ay = y + radius
        self.by = y - radius


    def intersects(self, other):
        return (self.ax <= other.bx
                and other.ax <= self.bx
                and self.ay >= other.by
                and other.ay >= self.by)

    def overlaps(self, other):
        return (self.bx <= other.bx
                and self.ax >= other.ax
                and self.by >= other.by
                and self.ay <= other.ay)

class Rectangle:
    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by

    def intersects(self, other):
        return (self.ax <= other.bx
                and other.ax <= self.bx
                and self.ay >= other.by
                and other.ay >= self.by)

    def overlaps(self, other):
        return (self.bx <= other.bx
                and self.ax >= other.ax
                and self.by >= other.by
                and self.ay <= other.ay)

def get_figure_type(figure_one):
    if figure_one.startswith('circle'):
        coordinates = figure_one[7:].split(', ')
        coordinates[-1] = coordinates[-1][:-1]  # remove the )
        x, y, radius = [float(coord) for coord in coordinates]
        figure_one = Circle(x, y, radius)
    elif figure_one.startswith('rectangle'):
        coordinates = figure_one[10:].split(', ')
        coordinates[-1] = coordinates[-1][:-1]  # remove the )
        ax, ay, bx, by = [float(coord) for coord in coordinates]
        figure_one = Rectangle(ax, ay, bx, by)

    return figure_one


test_count = int(input())

for _ in range(test_count):
    figure_one, figure_two = input(), input()
    figure_one = get_figure_type(figure_one)
    figure_two = get_figure_type(figure_two)

    if figure_one.overlaps(figure_two):
        print("{} inside {}".format(type(figure_one).__name__, type(figure_two).__name__.lower()))
    elif figure_two.overlaps(figure_one):
        print("{} inside {}".format(type(figure_two).__name__, type(figure_one).__name__.lower()))
    elif figure_one.intersects(figure_two) or figure_two.intersects(figure_one):
        print('Rectangle and circle cross')
    else:
        print('Rectangle and circle do not cross')
