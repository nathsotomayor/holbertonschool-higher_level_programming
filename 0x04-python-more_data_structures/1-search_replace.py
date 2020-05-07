#!/user/bin/python3
def search_replace(my_list, search, replace):
    my_list = my_list.copy()
    element = 0
    for i in my_list:
        if i == search:
            my_list[element] = replace
        element += 1
    return my_list
