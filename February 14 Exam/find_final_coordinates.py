"""
Given a coordinate system, find the final coordinates of a point, given a file that has the steps that the
point should take.
The valid steps are - (right, left, up or down) accompanied by the distance the point should take in the direction.

sample input:
./steps.txt

sample content of steps.txt:
right 12
up 2
left 17.8
right 3.772
up 32.9
left 20.6
down 17.8

expected output:
X -22.628
Y 17.100
"""

try:
    INDEX_DIRECTION = 0
    INDEX_DISTANCE = 1

    file_path = input()
    x,y = 0, 0

    with open(file_path, encoding='utf-8') as steps_reader:
        lines = steps_reader.read().splitlines()
        for line in lines:
            if line:  # if it's not an empty line
                line_info = line.split()
                step_direction = line_info[INDEX_DIRECTION]
                step_distance = float(line_info[INDEX_DISTANCE])

                if step_direction == "right":
                    x += step_distance
                elif step_direction == "left":
                    x -= step_distance
                elif step_direction == "up":
                    y += step_distance
                elif step_direction == "down":
                    y -= step_distance

    print("X {x:.3f}\nY {y:.3f}".format(x=x, y=y), end='')

except Exception as e:
    print("INVALID INPUT")

# 100/100