#!/usr/bin/python3
"""Create class for rectangle."""


class Rectangle:
    """Create constructor for with and height."""

    def __init__(self, width=0, height=0):
        """class defenicion"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Proprty to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set it"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property height to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter height to retrieve it"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
