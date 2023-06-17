#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    target_key = [key for key in a_dictionary if a_dictionary[key] == value]
    for key in target_key:
        del a_dictionary[key]
    return (a_dictionary)
