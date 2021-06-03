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
