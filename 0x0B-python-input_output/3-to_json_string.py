#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Variable save json array and return variable"""
    reFile = json.dumps(my_obj)
    return reFile
