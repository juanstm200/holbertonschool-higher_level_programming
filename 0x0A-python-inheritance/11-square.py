#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Function that validates the data height and width are of type integer"""
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    """returns the previously multiplied data on the screen"""
    def area(self):
        return super().area()

    """prints the area multiplication value on the screen"""
    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
