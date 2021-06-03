#!/usr/bin/python3
"""unction that returns the list of available attributes"""


def lookup(obj):
    """takes maximum of one object."""
    return dir(obj)
