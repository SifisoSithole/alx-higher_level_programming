#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[matrix[y][x] ** 2 for x in range(len(matrix[0]))] for y in range(len(matrix))]
