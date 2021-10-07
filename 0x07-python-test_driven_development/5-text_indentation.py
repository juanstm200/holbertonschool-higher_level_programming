#!/usr/bin/python3
""" function that prints a text with 2 new
    lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines"""
    if type(text) != str:
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    for i in characters:
        text = (i + "\n\n").join(line.strip(" ") for line in text.split(i))
    print("{}".format(text), end="")
