#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {value: a_dictionary[value] * 2  for value in a_dictionary} 
    return new_dictionary
