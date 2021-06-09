#!/usr/bin/python3
""" Module for storing the Square class. """
from models.rectangle import Rectangle
from collections import OrderedDict


class Square(Rectangle):
    """Update the class Square by adding the public method """
    def __init__(self, size, x=0, y=0, id=None):
        """ __init__"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the string for the Rectangle object """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ Updates all attributes of the Rectangle object. """
        if bool(args) is True and args is not None:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception as e:
                pass
        else:
            for i in kwargs.keys():
                if i in dir(self):
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """ Returns the dictionary"""
        ret_dict = OrderedDict()
        ret_dict["id"] = self.id
        ret_dict["size"] = self.width
        ret_dict["x"] = self.x
        ret_dict["y"] = self.y
        return dict(ret_dict)

    @property
    def size(self):
        """ Getter"""
        return self.width

    @size.setter
    def size(self, number):
        """ Setter"""
        self.width = number
        self.height = number
