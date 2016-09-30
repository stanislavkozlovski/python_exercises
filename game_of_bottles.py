"""
In one of the neighborhoods in Sofia, there's a very popular drinking game, called Game of Bottles.

The game is unusual, because it combines math & drinking:

In a standard 2D plain (usually a football field), different bottles are arranged. Each bottle has position, described by (x, y) coordinates.
In order to walk between bottles, you can use only horizontal and vertical lines - no diagonals.
You can visit a bottle only once.
Your task is to find the best way(s) to walk between bottles that will give you the smallest walking distance.

Example

Lets have the following bottles:

A = (1, 1)
B = (1, 2)
C = (3, 3)

The distance between A and B is 1 (you need to go one step up)

The distance between A and C is 4 (you need to go 2 steps to the left and 2 steps up)
The distance between B and C is 3 (you need to go 2 steps to the left and 1 step up)
The obvious solution is taking A -> B -> C for total distance of 4. There is another solution C -> B -> A with distance 4.

https://github.com/HackBulgaria/ApplicationFall2016/tree/master/4-Game-of-Bottles
"""
"""
Solution:
1.Pick a node and connect it with the closest node to it.
2.Move to that node and connect to the shortest again.
3.Go on until you connect all of them.
4.Save the distance it took you
5.Repeat 1-4 until you iterate through all the nodes
"""
import sys


def main():
    point_count = int(input())
    coordinates = []
    shortest_path = sys.maxsize

    for i in range(0, point_count):
        coordinates.append(tuple([int(n) for n in input().split()]))

    for coords in coordinates:
        current_shortest_path = get_shortest_path(coords, coordinates)
        if current_shortest_path < shortest_path:
            shortest_path = current_shortest_path

    print(shortest_path)


def get_shortest_path(coords: tuple, coordinates: list):
    """
    This function gets the shortest possible path to traverse all the coordinates
     in the list from our starting coordinates

    :param coords: the coords we start from
    :param coordinates: the list with all the available coordinates
    :return: the shortest possible path from our coordinates
    """
    temp_coordinates = coordinates[:]  # copy the list by value, not by reference
    temp_coordinates.remove(coords)  # remove the starting temp_coordinates from the list
    path_distance = 0

    while len(temp_coordinates) is not 0:
        # loop through the temp_coordinates
        closest_coords = get_closest_coordinates(coords, temp_coordinates)

        path_distance += get_distance_between_coordinates(coords, closest_coords)  # update path distance

        coords = closest_coords
        temp_coordinates.remove(closest_coords)

    return path_distance


def get_closest_coordinates(coords: tuple, coordinates: list):
    """
    This function iterates through the coordinates list and find the coordinates closest to our current coords
    :return: tuple
    """
    current_closest_coords = tuple()
    current_closest_distance = sys.maxsize

    for coords_two in coordinates:
        distance = get_distance_between_coordinates(coords, coords_two)
        if distance < current_closest_distance:
            current_closest_distance = distance
            current_closest_coords = coords_two

    return current_closest_coords


def get_distance_between_coordinates(coords_one: tuple, coords_two: tuple):
    """
    This function returns the distance between two coordinates
    """
    x1, y1 = coords_one
    x2, y2 = coords_two

    x_distance = abs(x1 - x2)
    y_distance = abs(y1 - y2)

    return x_distance + y_distance


if __name__ == "__main__":
    main()