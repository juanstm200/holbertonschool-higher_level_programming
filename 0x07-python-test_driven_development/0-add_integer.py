#!/usr/bin/python3
"""Function what sum two integers
    a convert to integer
    b convert to integer
"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
        if a or b not is int or float raise,
        TypeError
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
