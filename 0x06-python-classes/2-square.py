#!/usr/bin/python3
"""Create Square methods private size"""


class Square:
    """TypeError exception with the message size must be an integer"""
    def __init__(self, size=0):
        interger = type(size)
        if interger is not int:
            raise TypeError('size must be an integer')
            """ValueError exception the message size must be >= 0"""
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
