#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for val_dict in list(a_dictionary.keys()):
        if value == a_dictionary[val_dict]:
            del a_dictionary[val_dict]
    return a_dictionary
