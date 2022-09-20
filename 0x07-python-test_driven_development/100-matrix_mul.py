#!/usr/bin/python3
"""
This is the 100-matrix_mul module.

Returns the product of two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns a new matrix
    Parameters:
        m_a (list): First matrix
        m_b (list): Second matrix
    Return:
        new_matrix (list): Product of m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a an m_b can't be multiplied")

    length = len(m_b[0])
    new_m_b = []
    for c in range(len(m_b[0])):
        temp_list = []
        for r in range(len(m_b)):
            if len(m_b[r]) != length:
                raise TypeError("each row of m_b must be the same size")
            temp_list.append(m_b[r][c])
        new_m_b.append(temp_list)

    new_matrix = []

    length = len(m_a[0])
    for row in m_a:
        if len(row) != length:
            raise TypeError("each row of m_a must be the same size")
        new_row = []
        for col in new_m_b:
            prod = 0
            for i in range(len(new_m_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
