#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """def __init__"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """def area"""
        return (self.__width * self.__height)

    def __str__(self):
        """def __str__"""
        stri = "[" + str(self.__class__.__name__) + "] "
        stri += str(self.__width) + "/" + str(self.__height)
        return (stri)
