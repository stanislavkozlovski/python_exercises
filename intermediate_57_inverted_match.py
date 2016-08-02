"""
Given a 3x3 table where 1 represents on and 0 represents off:
ABC
A010
B111
C011
Where "inverted match" is defined as a case where the values at
the coordinates in the format of (X, Y) and (Y, X) are the same, the inverted matches are as follows:
[[(A, B), (B, A)], [(A, C), (C, A)], [(B, C), (C, B)]]
Of these, the matches that have a value of 1 are:
[[(A, B), (B, A)], [(B, C), (C, B)]]
Therefore, there are 2 sets of inverted matches that have a value of 1.
Find the amount of inverted matches in the table in table(below) with a value of 1.
"""

"""
Game plan is:
1.Iterate through the whole matrix
2.Switch every coordinate to see if the inverted matches
matrix[x,y] == matrix[y,x]
3.Store inverted matches and store every switch so we don't repeat them
i.e not have the algorithm check twice for matrix[0,5] and matrix[5,0] because they've been compared already

"""

import numpy


def check_if_match(matrix, row, col, VALUE):
    if matrix[row,col] == VALUE and matrix[row,col] == matrix[col,row]:
        return True
    else:
        return False


def convert_input_to_matrix(user_input: str) -> numpy.matrix:
    temp_list = [] # 2D list that's going to be converted to a numpy.matrix

    for line in user_input.splitlines()[1:]:
        row_list = [int(i) for i in line[1:]]  # creates an integer list of the row
        temp_list.append(row_list)  # appends the row to the 2D list

    matrix = numpy.matrix(temp_list)

    return matrix


user_input = """ABCDEFGHIJKLMNOPQRST
A11110101111011100010
B10010010000010001100
C01101110010001000000
D10110011001011101100
E10100100011110110100
F01111011000111010010
G00011110001011001110
H01111000010001001000
I01101110010110010011
J00101000100010011110
K10101001100001100000
L01011010011101100110
M10110110010101000100
N10001111101111110010
O11011010010111100110
P01000110111101101000
Q10011001100010100000
R11101011100110110110
S00001100000110010101
T01000110011100101011"""


# matrix = numpy.matrix([[0, 1, 0],
#           [1, 1, 1],
#           [0, 1, 1]
#           ])
matrix = convert_input_to_matrix(user_input)
rows = matrix.shape[0]
cols = matrix.shape[1]

VALUE = 1  # the value we're searching for
ASCII_A_INDEX = 65
iterated_matches = set()
inverted_matches = []

for row in range(0,rows):
    for col in range(0,cols):
        if row == col:  # we don't want the same coordinates
            continue
        if (row, col) in iterated_matches:  # no need to check again
            continue

        if check_if_match(matrix,row,col,VALUE):
            # convert them to character like in the challenge's description
            row_character = chr(row + ASCII_A_INDEX)
            col_character = chr(col + ASCII_A_INDEX)
            inverted_matches.append([(row_character, col_character), (col_character,row_character)])

        iterated_matches.add((col,row))
        iterated_matches.add((row,col))

print(inverted_matches)
print(len(inverted_matches))

"""
Funny one liner that gets the job done but only if the value we're comparing is 1:
sum(m[i][j]*m[j][i] for i in range(len(m)) for j in range(i))

m = [map(int, a[1:]) for a in s.splitlines()[1:]]
convenient way to parse the string input, gonna use this
learned what map does: it goes through every index (or 1: in this case) and applies whatever
function you put, in this case - int

UPDATE: the map thing doesn't seem to work in the same way in python 3
"""