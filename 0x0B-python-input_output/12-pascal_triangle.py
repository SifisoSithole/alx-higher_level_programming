#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        row = pascal[-1]
        new_row = [1]
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])
        new_row.append(1)
        pascal.append(new_row)
    return pascal
