'''
We are living in 2D world and we are running out of water! We are migrating to KEPLER-186F, the new planet that NASA discovered, but it is a slow migration because that planet is far far away.

Luckily we still have some big lakes full of clean water. We need to know exactly how much water is in every lake.

Write a program that takes the lake structure and calculates the amount of water there.

Few important things:

Our lakes live in a 2D grid of 1x1 squares.
We are always going to start from depth 0 and finish at depth 0.
Each square can be filled with 1000 liters of water.
Input

On the standard input, we read a line - string that represents the structure of the lake.

d - stands for down. We are always taking the horizontal line that splits the 1x1 square in half.
h - stands for horizontal
u - stands for up
Output should be the total liters of water.
'''
# https://github.com/HackBulgaria/ApplicationFall2016/tree/master/2-Lakes

depth = 0
squares_in = 0
square_liters = 1000
total_liters = 0
user_input = input()

for command in user_input:
    if command == 'd':  # down
        # whenever we go down, we take half the liters and a square for every one we're down
        if depth >= 0:
            total_liters += (depth * square_liters) + (square_liters/2)
        depth += 1
    elif command == 'h':  # horizontal
        if depth >= 0:
            total_liters += (depth * square_liters)
    else:  # up
        # whenever w go up, we take half the liters of a square
        # and (after we go up one) a square for every one we're down
        depth -= 1
        if depth >= 0:
            total_liters += ((depth) * square_liters) + (square_liters/2)


print(total_liters)