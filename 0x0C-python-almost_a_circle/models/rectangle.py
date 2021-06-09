#!/usr/bin/bash
"""storing Rectangle class. """
from models.base import Base
from collections import OrderedDict


class Rectangle(Base):
    """ Rectangle model class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ Returns the string """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def validate_int(self, name, number):
        """ Validates if the given"""
        if type(number) is not int:
            raise TypeError("{} must be an integer".format(name))

    def area(self):
        """ Returns the area of the Rectangle object. """
        return self.width * self.height

    def display(self):
        """ Prints the Rectangle object using width and height. """
        print("\n" * self.y, end='')
        for i in range(self.height):
            for j in range(self.width + self.x):
                if j < self.x:
                    print(' ', end='')
                else:
                    print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        """ Updates all attributes of the Rectangle object. """

        if bool(args) is True and args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for i in kwargs.keys():
                if i in dir(self):
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """ Returns the dictionary representation"""
        ret = OrderedDict()
        ret["id"] = self.id
        ret["width"] = self.width
        ret["height"] = self.height
        ret["x"] = self.x
        ret["y"] = self.y
        return dict(ret)

    @property
    def width(self):
        """ Getter of the Rectangle """
        return self.__width

    @width.setter
    def width(self, number):
        """ Setter of the Rectangle """
        self.validate_int("width", number)
        if number <= 0:
            raise ValueError("width must be > 0")
        self.__width = number

    @property
    def height(self):
        """ Getter of the Rectangle """
        return self.__height

    @height.setter
    def height(self, number):
        """ Setter of the Rectangle"""
        self.validate_int("height", number)
        if number <= 0:
            raise ValueError("height must be > 0")
        self.__height = number

    @property
    def x(self):
        """ Getter of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, number):
        """ Setter of the Rectangle """
        self.validate_int("x", number)
        if number < 0:
            raise ValueError("x must be >= 0")
        self.__x = number

    @property
    def y(self):
        """ Getter of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, number):
        """ Setter of the Rectangle"""
        self.validate_int("y", number)
        if number < 0:
            raise ValueError("y must be >= 0")
        self.__y = number
