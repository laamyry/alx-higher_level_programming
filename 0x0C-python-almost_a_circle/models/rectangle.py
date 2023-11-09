#!/usr/bin/python3
'''Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    '''First Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''__init__'''
        super().__init__(id)
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
        self.__width = value

    @property
    def height(self):
        '''get_height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set_height'''
        self.__height = value

    @property
    def x(self):
        '''get_x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set_x'''''
        self.__x = value

    @property
    def y(self):
        '''get_y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set_y'''
        self.__y = value
