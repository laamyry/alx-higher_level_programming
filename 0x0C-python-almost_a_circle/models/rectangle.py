#!/usr/bin/python3
'''Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    '''First Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_width(self):
        '''get_width'''
        return self.width

    def set_width(self, value):
        '''set_width'''
        self.width = value

    def get_height(self):
        '''get_height'''
        return self.height

    def set_height(self, value):
        '''set_height'''
        self.height = value

    def get_x(self):
        '''get_x'''
        return self.x

    def set_x(self, value):
        '''set_x'''''
        self.x = value

    def get_y(self):
        '''get_y'''
        return self.y

    def set_y(self, value):
        '''set_y'''
        self.y = value
