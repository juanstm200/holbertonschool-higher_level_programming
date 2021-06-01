#!/usr/bin/python3
"""Function that returns the dictionary description"""


def class_to_json(obj):
    """Returns the dictionary description"""
    return dict(obj.__dict__)
