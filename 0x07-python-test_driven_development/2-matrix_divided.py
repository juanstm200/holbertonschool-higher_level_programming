#!/usr/bin/python3
"""Divided two Matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix and return new matrix"""
    new_matrix = []
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    size = len(matrix[0])

    for div_row in matrix:
        new_row = []
        if size == len(div_row):
            for elment in div_row:
                if type(elment) not in (int, float):
                    raise TypeError(msg)
                new_row.append(round(elment / div, 2))
            new_matrix.append(new_row)
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
