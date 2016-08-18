from math import sqrt

try:
    a = float(input())
    b = float(input())
    c = float(input())

    perimeter = (a + b + c) / 2

    area = sqrt(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c))

    print("{:.2f}".format(area))
except Exception:
    print("INVALID INPUT")
