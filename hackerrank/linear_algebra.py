"""
You are given a square matrix A with dimensions NxN. Your task is to find the determinant.

Input Format:
The first line contains the integer N.
The next N lines contains the N space separated elements of array A.

Output Format:
Print the determinant of A.
"""
import numpy

n = int(input())
a = []  # type: list

# build the matrix
for i in range(0, n):
    a.append([float(num) for num in input().split(' ')])

# get the determinant
determinant = numpy.linalg.det(a)

print(determinant)