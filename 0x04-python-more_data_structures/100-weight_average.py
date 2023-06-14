#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0
    num = sum(m * n for m, n in my_list)
    deno = sum(n for m, n in my_list)
    return (num / deno)
