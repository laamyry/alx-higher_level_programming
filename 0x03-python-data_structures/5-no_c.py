#!/usr/bin/env python3

def no_c(my_string):

    new = ""
    for m in my_string:
        if m not in ('c', 'C'):
            new += m
    return new