#!/usr/bin/python3
""" function that returns True or False"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited"""
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
