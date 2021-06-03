#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """function that prints an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    """verifies if the value variable as an integer or greater than 0"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
