#!/usr/bin/python3
def no_c(my_string):
    list = ''
    for i in my_string:
        if (i != 'C' and i != 'c'):
            list = list + i
    return (list)
