#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Creatiing the public atributes"""
    first_name = ""
    last_name = ""
    age = ""

    """attributes are initialized"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Returning a dictionary as and atribute"""
    def to_json(self, attrs=None):
        attList = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for values in attrs:
                if values in self.__dict__:
                    attList.update({values: self.__dict__[values]})

            return attList
        return self.__dict__
