#!/usr/bin/env python3

def no_c(my_string):

    new = ""
    for m in range (len(my_string)):
        if my_string[m] != 'c' and my_string[m] != 'C':
            new += my_string[m]
    return new