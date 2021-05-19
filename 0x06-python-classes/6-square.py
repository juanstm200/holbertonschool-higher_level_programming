#!/usr/bin/python3
"""Create Square methods private size"""


class Square:
    """TypeError exception with the message size must be an integer"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        if self.__size != 0:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
        else:
            print()

    @property
    def position(self):
        """public psotion"""
        return self.__position

    @position.setter
    def position(self, value):
        """ position"""
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                value[0] < 0 or
                type(value[1]) is not int or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
