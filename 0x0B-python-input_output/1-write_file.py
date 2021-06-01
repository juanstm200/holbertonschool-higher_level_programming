#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Create file and wirte in the file"""
    with open(filename, mode='w+', encoding="utf-8") as textWrite:
        numChar = textWrite.write(text)
    return numChar
