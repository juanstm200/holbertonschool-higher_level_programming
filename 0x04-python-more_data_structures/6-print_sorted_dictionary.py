#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary.items())
    for i, j in new_list:
        print("{}: {}".format(i, j))
