#!/usr/bin/python3
"""Function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, mode="a", encoding="utf-8") as appFile:
        numChar = appFile.write(text)
    return numChar
