#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise ValueError('Invalid value for a')
            res += (a ** b) / m
        except ValueError:
            res = b + a
            break
    return res
