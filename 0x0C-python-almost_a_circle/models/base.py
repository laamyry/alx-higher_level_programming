#!/usr/bin/python3
'''the first class Base:'''


class Base:
    '''class Base:'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''__init__'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
