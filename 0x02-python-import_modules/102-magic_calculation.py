#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        magic = add(a, b)
        for i in range(4, 6):
            magic = add(c, i)
        return magic
    return sub(a, b)
