#!/usr/bin/python3
"""write doc"""

import math


class MagicClass:
    """start magic"""

    def __init__(self, radius=0):
        """write another doc"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """another one with the doc"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """such doc"""
        return (2 * math.pi * self.__radius)
