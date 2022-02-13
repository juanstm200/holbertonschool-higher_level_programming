#!/usr/bin/python3
""" Module: For defining the Square class. """


class Square:
    """ Class: For defining a Square object. """
    def __init__(self, size=0):
        """__init__: with validation of size as int and positive.
        Args:
            size (int): Size of the square.
        """
        if isinstance(size, (int)) is True:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size  #: init attribute.
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ area: Returns the area of the Square instance. """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ size: Gets the size of the Square instance. """
        return self.__size

    @size.setter
    def size(self, value):
        """ size: Sets the size of the square instance with value. """
        if isinstance(value, (int)) is True:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value  #: Set size value.
        else:
            raise TypeError("size must be an integer")

    def __eq__(self, other):
        """ Method: For enabling Square1 == Square2 """
        return (self.area() == other.area())

    def __ne__(self, other):
        """ Method: For enabling Square1 != Square2 """
        return (self.area() != other.area())

    def __lt__(self, other):
        """ Method: For enabling Square1 < Square2 """
        return (self.area() < other.area())

    def __le__(self, other):
        """ Method: For enabling Square1 <= Square2 """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """ Method: For enabling Square1 > Square2 """
        return (self.area() > other.area())

    def __ge__(self, other):
        """ Method: For enabling Square1 >= Square2 """
        return (self.area() >= other.area())
