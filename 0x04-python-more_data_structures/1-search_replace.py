#!/usr/bin/python3

def search_replace(my_list, search, replace):

    return (list(map(lambda m: replace if m is search else m, my_list)))
