#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix[0])
    size2 = len(matrix)
    return [[matrix[y][x]**2 for x in range(size)] for y in range(size2)]
