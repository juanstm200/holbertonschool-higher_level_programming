#!/usr/bin/python3
"""Funtion by print massage of a file in display"""


def read_file(filename=""):
    with open("my_file_0.txt") as f:
        for line in f:
            print(line, end="")
