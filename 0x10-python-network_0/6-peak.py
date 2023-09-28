#!/usr/bin/python3
'''finds a peak in a list of unsorted integers.'''

def find_peak(list_of_integers):
    size = len(list_of_integers)
    
    if size == 0:
        return None

    size_semi = size // 2
    size_semi2 = size // 2
    
    while True:
        if size_semi < size - 1 and list_of_integers[size_semi] < list_of_integers[size_semi + 1]:
            if size_semi2 == 0:
                size_semi2 = 2
            size_semi += size_semi2 // 2

        elif size_semi2 > 0 and list_of_integers[size_semi] < list_of_integers[size_semi - 1]:
            if size_semi2 == 0:
                size_semi2 = 2
            size_semi -= size_semi2 // 2
        else:
            return list_of_integers[size_semi]
