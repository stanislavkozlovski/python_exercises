"""
You are given three integers X, Y and Z representing the dimensions of a cuboid.
 You have to print a list of all possible coordinates on a 3D grid where the sum of X + Y + Z is not equal to N.
  If X=2, the possible values of X can be 0, 1 and 2. The same applies to Y and Z.

Input Format
Four integers X, Y, Z and N each on four separate lines, respectively.

Output Format
Print the list in lexicographic increasing order.
"""
x, y, z, n = (int(input()) for _ in range(4))

coordinates_list = [[x_i, y_i, z_i] for x_i in range(0, x+1) for y_i in range(0, y+1) for z_i in range(0, z+1)
                    if x_i + y_i + z_i is not n]

print(coordinates_list)