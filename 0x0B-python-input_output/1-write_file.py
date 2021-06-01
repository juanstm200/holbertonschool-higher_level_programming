#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w') as textWrite:
        numChar = textWrite.write(text)
        return numChar
