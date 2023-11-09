#!/usr/bin/python3
'''Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    '''First Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    @property
    def get_width(self):
        '''get_width'''
        return self.__width
    @__width.setter
    def set_width(self, value):
        '''set_width'''
        self.__width = value
    @property
    def get_height(self):
        '''get_height'''
        return self.__height
    @__height.setter
    def set_height(self, value):
        '''set_height'''
        self.__height = value
    @property
    def get_x(self):
        '''get_x'''
        return self.__x
    @__x.setter
    def set_x(self, value):
        '''set_x'''''
        self.__x = value
    @property
    def get_y(self):
        '''get_y'''
        return self.__y
    @__y.setter
    def set_y(self, value):
        '''set_y'''
        self.__y = value
