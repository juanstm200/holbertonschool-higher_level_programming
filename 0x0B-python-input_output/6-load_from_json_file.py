#!/usr/bin/python3
"""Function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """object from a JSON format stored in a file"""
    with open(filename, encoding="utf-8") as textJson:
        objectText = json.loads(textJson.read())
        return objectText
