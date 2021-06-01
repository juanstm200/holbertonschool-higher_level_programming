#!/usr/bin/python3
"""function that writes an Object to a  JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write or create new file with json representation"""
    with open(filename, mode="w+", encoding="utf-8") as objectWrite:
        writeObjectNum = objectWrite.write(json.dumps(my_obj))
        return writeObjectNum
