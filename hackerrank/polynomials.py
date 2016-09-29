"""
You are given the coefficients of a polynomial.
Your task is to find the value of  at point.
"""
import numpy

# read the input
# coefficients
user_input = [float(i) for i in input().split(' ')]

# x
x = float(input())

print(numpy.polyval(user_input, x))