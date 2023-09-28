#!/usr/bin/python3
'''finds a peak in a list of unsorted integers.'''

def find_peak(list_of_integers):
    size = len(list_of_integers)
    
    if size == 0:
        return None
    
    semi = size // 2
    
    while True:

        if semi < size - 1 and list_of_integers[semi] < list_of_integers[semi + 1]:
            if semi == 0:
                semi = 2
            semi += semi // 2

        elif semi > 0 and list_of_integers[semi] < list_of_integers[semi - 1]:
            if semi == 0:
                semi = 2
            semi -= semi // 2
        else:
            return list_of_integers[semi]
