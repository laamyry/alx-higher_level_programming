#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return 0
    total = 0
    digi = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        m = digi[roman]
        if total < m * 5:
            total += m
        else:
            total -= m
    return total
