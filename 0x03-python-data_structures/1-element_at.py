#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        idx = my_list.index(idx)
    if idx < 0:
        return None
    if idx > len(my_list)-1:
        return None
    return idx
