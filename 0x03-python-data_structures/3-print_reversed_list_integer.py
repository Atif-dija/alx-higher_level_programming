#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for j in reversed(my_list):
            print("{:d}".format(j))
