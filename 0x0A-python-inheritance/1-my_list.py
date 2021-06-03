#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """prints the numerical data entered in an orderly manner"""
    def print_sorted(self):
        """This method print the values sorted"""
        print(sorted(self))
