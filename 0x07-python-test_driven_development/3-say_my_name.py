#!/usr/bin/python3
""" Function that prints the first and last name of the data entered by
    Fist_name
    Last_name
"""


def say_my_name(first_name, last_name=""):
    """ if fist_name or last_name not is str
    print TypeError"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
