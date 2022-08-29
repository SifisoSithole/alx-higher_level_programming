#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        len_list = len(list)
        for i in range(len_list):
            if i != len_list - 1:
                print("{:d}".format(list[i]), end=" ")
            else:
                print("{:d}".format(list[i]))
    if len(matrix[0]) == 0:
        print("")
