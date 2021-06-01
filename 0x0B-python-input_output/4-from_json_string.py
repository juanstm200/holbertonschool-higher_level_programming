#!/usr/bin/python3
"""function that returns an object (data structure) represented JSON string"""
import json


def from_json_string(my_str):
    """decode a JSON we are going to make use of the function loads"""
    objectJson = json.loads(my_str)
    return objectJson
