#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    element = 0
    for i in my_list:
        if i == search:
            new_list[element] = replace
        element += 1
    return new_list
