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

    def get_width(self):
        '''get_width'''
        return self.__width
        
    def set_width(self, value):
        '''set_width'''
        self.__width = value

    def get_height(self):
        '''get_height'''
        return self.__height
        
    def set_height(self, value):
        '''set_height'''
        self.__height = value

    def get_x(self):
        '''get_x'''
        return self.__x
        
    def set_x(self, value):
        '''set_x'''''
        self.__x = value

    def get_y(self):
        '''get_y'''
        return self.__y
        
    def set_y(self, value):
        '''set_y'''
        self.__y = value
