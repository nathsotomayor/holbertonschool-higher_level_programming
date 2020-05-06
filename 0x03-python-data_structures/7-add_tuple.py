#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_one = tuple_a + (0, 0)
    tup_two = tuple_b + (0, 0)
    res_tuple = (tup_one[0] + tup_two[0], tup_one[1] + tup_two[1])
    return res_tuple
