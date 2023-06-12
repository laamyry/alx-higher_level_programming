#!/usr/bin/python3

def no_c(my_string):

    new = ""
    for m in range (len(my_string)):
        if my_string[m] not in ('c', 'C'):
            new += my_string[m]
    return new
