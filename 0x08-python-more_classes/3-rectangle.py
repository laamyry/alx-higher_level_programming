#!/usr/bin/python3

"""defines a rectangle by: (based on 2-rectangle.py)"""


class Rectangle:
    """present rectangle."""

    def __init__(self, width=0, height=0):
        """create new Rectangle.
        Args:
            width (int): new rectangle width.
            height (int): new rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width def'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''width def'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height def'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height def'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''area def'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''perimeter def'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''str def'''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for m in range(self.__height):
            [rectangle.append('#') for n in range(self.__width)]
            if m != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
