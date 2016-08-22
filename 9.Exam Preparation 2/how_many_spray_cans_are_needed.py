"""
How many spray cans are needed to paint a wall with W meters wide and H meters high, if one spray can covers
1.76 m^2
W and H are floats, given as input
"""
from math import ceil


wall_area = float(input()) * float(input())
spray_cans_needded = ceil(wall_area/1.76)

print(spray_cans_needded)

# 100/100 score