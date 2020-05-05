#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        idx = my_list.index(i)
        if idx < 0:
            return None
        if idx > len(my_list):
            return None
    return idx
