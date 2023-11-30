#!/usr/bin/python3
'''module doc for square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''doc of square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''doc of square'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''doc of square'''
        return self.width

    @size.setter
    def size(self, vl):
        '''doc of square'''
        self.width = vl
        self.height = vl

    def update(self, *args, **kwargs):
        '''doc of square'''
        if len(args) == 0:
            id = kwargs["id"] if "id" in kwargs else self.id
            self.id = id
            size = kwargs["size"] if "size" in kwargs else self.width
            x = kwargs["x"] if "x" in kwargs else self.x
            y = kwargs["y"] if "y" in kwargs else self.y
        else:
            if len(args) >= 1:
                self.id = args[0]
            size = args[1] if len(args) >= 2 else self.width
            x = args[2] if len(args) >= 3 else self.x
            y = args[3] if len(args) >= 4 else self.y
        self.checks(size, size, x, y)
        self.width = size
        self.x = x
        self.y = y

    def to_dictionary(self):
        '''doc of square'''
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.x} - {self.width}"