#!/usr/bin/python3

def uniq_add(my_list=[]):

    total = 0
    for m in set(my_list):
        total += m
    return total
