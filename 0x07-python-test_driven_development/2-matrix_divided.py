#!/usr/bin/python3
"""
This is the "2-matrix_divided" module

The ```2-matrix_divided``` module divides a matrix of integers or floats
and returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all of the elements in a matrix
    parameters:
        matrix (list): matrix of integers and floats
        div (int/float): Divisor
    Returns:
        result_matrix (list): Newly created matrix
    """
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    result_matrix = []
    e = "matrix must be a matrix (list of lists) of integers/floats"
    for lst in matrix:
        if len(lst) != length:
            error = "Each row of the matrix must have the same size"
            raise TypeError(error)
        new_list = []
        for num in lst:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(e)
            new_list.append(round(num / div, 2))
        result_matrix.append(new_list)
    return result_matrix
