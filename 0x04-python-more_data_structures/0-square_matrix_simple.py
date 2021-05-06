#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix[:]
    for i in range(len(new_list)):
        new_list[i] = list(map(lambda x: x * x, matrix[i]))
    return (new_list)
