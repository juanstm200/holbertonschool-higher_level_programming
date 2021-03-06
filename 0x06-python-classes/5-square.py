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
    """that returns the current square area"""
    def area(self):
        area = (self.__size * self.__size)
        return area

    @property
    def size(self):
        """public size"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter"""
        inter = type(value)
        if inter is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """print # in the square"""
        if self.__size is not 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
