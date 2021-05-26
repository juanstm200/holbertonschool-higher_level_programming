#!/usr/bin/python3
"""Function that print character #"""


def print_square(size):
    if type(size) not in (int, float):
        raise TypeError("size must be an integer")
    if size <= -1:
        raise ValueError("size must be >= 0")
    for i in range(round(size)):
        for j in range(round(size - 1)):
            print("#", end='')
        print("#")
