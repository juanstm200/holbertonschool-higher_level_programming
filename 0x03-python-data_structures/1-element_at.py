#!/usr/bin/python3
def element_at(my_list, idx):
    lent = len(my_list)
    if (idx < 0 or idx != lent):
        return None
    return(my_list[idx])
