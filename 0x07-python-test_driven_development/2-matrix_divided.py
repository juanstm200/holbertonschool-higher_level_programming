#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = matrix
    for i in range(len(new_matrix[0])):
        for j in range(len(new_matrix)):
            if type(new_matrix[j][i])  not in (int, float):
                print(TypeError("hola"))
            else:
                new_matrix[j][i] = round((new_matrix[j][i] / div), 2) 
    return new_matrix