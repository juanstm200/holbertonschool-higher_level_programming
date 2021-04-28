#!/usr/bin/python3
def uppercase(str):
    for i in range(str):
        letter = ord(i)
        if letter >= ord('a') and letter <= ord('z'):
            char = chr(letter - 32)
        else:
            char = i
        print("{:s}".format(char), end="")
    print()
