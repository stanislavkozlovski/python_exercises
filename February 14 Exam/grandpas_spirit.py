"""
We have some alcoholic spirits left off by grandpa and some cannisters
Given the liter of spirits, assuming that 1 liter = 1dm^3 and given
the path to a text file that holds the radius and height of all the cannisters, find the smallest cannister
that can hold all our alcohol.

sample input:
2
./containers.txt

sample content of containers.txt:
Бидонче 1,4.5,20
Бидонче 2,6,25
Бидонче 8,30,120

sample output:
Бидонче 2
"""
import math
from sys import maxsize

try:
    INDEX_CONTAINER_NAME = 0
    INDEX_CONTAINER_RADIUS = 1
    INDEX_CONTAINER_HEIGHT = 2

    litres_spirit = float(input())
    if litres_spirit <= 0:
        raise ValueError("The spirit's litres cannot be a negative value!")

    spirits_volume = litres_spirit * 1000  # we convert the litres to 1dm^3 which then convert to cm^3
    file_path = input()
    
    found_container = False  # type: bool
    smallest_container = ''  # type: str
    smallest_container_volume = maxsize # type: float

    with open(file_path, encoding='utf-8') as containers_reader:
        containers = containers_reader.read().splitlines()

        for container in containers:
            if container:  # if the line is not empty
                container_info = container.split(',')
                container_name = container_info[INDEX_CONTAINER_NAME]
                container_radius = float(container_info[INDEX_CONTAINER_RADIUS])
                container_height = float(container_info[INDEX_CONTAINER_HEIGHT])

                container_volume = math.pi * container_radius ** 2 * container_height

                # check if it's smaller than the smallest container and bigger than the spirit's volume
                if smallest_container_volume >= container_volume >= spirits_volume:
                    # update container
                    found_container = True
                    smallest_container = container_name
                    smallest_container_volume = container_volume

    if found_container:
        print(smallest_container)
    else:
        print("NO SUITABLE CONTAINER")

except Exception as e:
    print("INVALID INPUT")

# 100/100
