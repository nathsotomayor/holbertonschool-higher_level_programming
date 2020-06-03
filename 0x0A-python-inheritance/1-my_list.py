#!/usr/bin/python3
""" Creates class that inherits from 'list' """


class MyList(list):
    """ Defines a class inheritance """
    def print_sorted(self):
        """ Creates function that prints a sorted list """
        print("{}".format(sorted(self)))
