#!/usr/bin/python3
"""Funtion by print massage of a file in display"""


def read_file(filename=""):
    """Open file, read file and print cont file"""
    with open(filename, encoding="utf-8") as f:
        readText = f.read()
        print(readText, end="")
