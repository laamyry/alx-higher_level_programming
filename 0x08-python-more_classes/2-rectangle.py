#!/usr/bin/python3

'''defines a rectangle by: (based on 1-rectangle.py)'''


class Rectangle:
    '''Rectangle class'''
    def __init__(self, width=0, height=0):
        '''init def'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''width def'''
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return (self.__width)

    @width.setter
    def width(self, width):
        '''width def'''
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''height def'''
        if (not isinstance(self.__height, int)) or isinstance(self.__height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return (self.__height)

    @height.setter
    def height(self, height):
        '''height def'''
        if not isinstance(self.__height, int) or isinstance(self.__height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        '''area def'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''perimeter def'''
        if self.__height == 0 or self.width == 0:
            return (0)
        return ((self.__height + self.width) * 2)
