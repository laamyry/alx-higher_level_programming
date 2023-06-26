#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0
    for m in range(x):
        try:
            if isinstance(my_list[m], int):
                print(my_list[m], end="")
                count += 1
        except IndexError:
            break
    print()
    return count
