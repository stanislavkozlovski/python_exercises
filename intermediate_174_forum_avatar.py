"""
Your forum's usernames follow the same rules as reddit's usernames (e.g. no spaces, etc.). Your program will receive a single reddit-style username as input.

Your program outputs an avatar, preferably in color, with a unique pattern for that username. The output must always be the same for that username.
 You could just generate a totally random block of data, but you should try to make it interesting while still being reasonably unique.
"""
import hashlib
from PIL import Image, ImageDraw

# color list of tuples containing 16 colors(RGB) to choose from
COLORS = [
    (255, 0, 179),  #pink
    (189, 0, 0),  #dark red
    (255, 0, 0),  #red
    (122, 220, 225),  #sky blue
    (61, 89, 171),  #cobalt
    (75, 0, 130),  #indigo
    (187, 255, 255),  #paleturquoise 1
    (32, 178, 170),  #lightseagreen
    (0, 255, 0),  #green (lime)
    (250, 250, 210),  #light goldenrod yellow
    (255, 215, 0),  #gold
    (205, 102, 0),  #darkorange 3
    (255, 114, 86),  #coral 1
    (255, 153, 18),  #cadium yellow
    (31, 232, 233),  #exotic sea blue
    (53, 31, 101)  # pantone coated 2112 C
]
VERTICAL_SYMMETRY, HORIZONTAL_SYMMETRY, V_AND_H_SYMMETRY = 1,2,3
SYMMETRY_INDEX, COLOR_INDEX, PATTERN_INDEX, SECOND_COLOR_INDEX = 0,1,2,3

username = input("Please enter your username: ")
# convert the string to a sha1 hash
hashed_username = hashlib.sha1(username.encode()).hexdigest()
choose_symmetry = hashed_username[SYMMETRY_INDEX]
choose_color = hashed_username[COLOR_INDEX]
choose_second_color = hashed_username[SECOND_COLOR_INDEX]
choose_pattern = hashed_username[PATTERN_INDEX:]

# convert from hex to decimal and use floor (integer) division to get a number
# 0:no symmetry, 1:vertical symmetry, 2:horizontal symmetry, 3:both
symmetry = int(choose_symmetry, 16) // 4
# choose the color
color, second_color = COLORS[int(choose_color, 16)], COLORS[int(choose_second_color, 16)]

#create the image pattern
pattern = []
row = choose_pattern[:2]
hash_pattern = choose_pattern[2:]

for i in range(0,8):
    # use the first 2 numbers and shorten the hash by 2 each time
    rowlist = list(bin(int(row,16))[2:])  # create a list with the first 2 numbers as binary strings
    rowlist = list(map(lambda num: bool(int(num)), rowlist)) # convert each number (1 or 0) to a boolean
    # Booleans will determine if the pixel is colored or not :)

    while len(rowlist) < 8:
        rowlist.insert(0, False)

    pattern.append(rowlist)
    row = hash_pattern[:2]
    hash_pattern = hash_pattern[2:]

# handle symmetry
if symmetry in [VERTICAL_SYMMETRY, V_AND_H_SYMMETRY]: # vertical symmetry
    pattern = pattern[:4] + list(reversed(pattern[:4]))

if symmetry in [HORIZONTAL_SYMMETRY, V_AND_H_SYMMETRY]: # horizontal symmetry
    pattern = list(map(lambda x: x[:4] + list(reversed(x[:4])), pattern))

image = Image.new("RGB", (256, 256), "white")  #firstly a white canvas to be drawed on
draw = ImageDraw.Draw(image)
draw_color = color

# draw the 256x256 avatar :)
for i in range(8):
    for j in range(8):
      if pattern[i][j]:
        x_1, x_2 = i*32, (i+1)*32
        y_1, y_2 = j*32, (j+1)*32

        if j % 2 == 0: draw_color = second_color
        else: draw_color = color

        draw.rectangle(xy=[x_1, y_1, x_2, y_2], fill=draw_color)

image.show()
image.save("./" + username + "_avatar.jpg")
