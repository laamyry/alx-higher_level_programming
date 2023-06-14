#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    ls_ord = list(a_dictionary.keys())
    ls_ord.sort()
    
    for m in ls_ord:
        print("{}: {}".format(m, a_dictionary.get(m)))
