#!/usr/bin/python3
'''Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    '''First Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''__init__'''
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''get_width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set_width'''
        self.validate("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''get_height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set_height'''
        self.validate("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''get_x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set_x'''''
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        '''get_y'''

        return self.__y

    @y.setter
    def y(self, value):
        '''set_y'''
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value, fl=True):
        '''Validate attributes'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if fl and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not fl and value <= 0:
            raise ValueError("{} must be > 0".format(name))
