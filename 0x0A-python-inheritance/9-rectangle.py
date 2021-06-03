#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometr"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Function that validates the data height and width are of type integer"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    """returns the multiplication the height by the width that is the area"""
    def area(self):
        return (self.__width * self.__height)

    """returns the previously multiplied data on the screen"""
    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
