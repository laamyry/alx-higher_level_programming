#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    for m in range(list_length):
        try:
            div = my_list_1[m] / my_list_2[m]
        except (TypeError, ZeroDivisionError, IndexError):
            div = 0
        finally:
            new_list.append(div)
    return new_list
