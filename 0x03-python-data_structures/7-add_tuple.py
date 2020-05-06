#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        first_tup = tuple_a + (0, 0)
    if len(tuple_b) < 2:
        second_tup = tuple_b + (0, 0)
    res_tuple = (first_tup[0] + second_tup[0], first_tup[1] + second_tup[1])
    return res_tuple
