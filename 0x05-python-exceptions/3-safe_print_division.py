#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        divis = a / b
    except ZeroDivisionError:
        divis = None
    else:
        print("Inside result: {}".format(divis))
    finally:
        return divis
