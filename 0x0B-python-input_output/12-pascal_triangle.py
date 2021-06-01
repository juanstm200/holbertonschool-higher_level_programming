#!/usr/bin/python3
"""that returns a list integers representing the Pascal triangle"""


def pascal_triangle(n):
    """pascal triangle"""
    list = []
    if n <= 0:
        return list
    if n == 1:
        return [[1]]
    list = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(list[i - 1][j - 1] + list[i - 1][j])
        row.append(1)
        list.append(row)
    return list
