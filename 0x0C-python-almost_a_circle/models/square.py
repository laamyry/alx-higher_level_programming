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
        if args and len(args) != 0:
            i = 0
            for ar in args:
                if i == 0:
                    if ar is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = ar
                elif i == 1:
                    self.size = ar
                elif i == 2:
                    self.x = ar
                elif i == 3:
                    self.y = ar
                i += 1

        elif kwargs and len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "id":
                    if n is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = n
                elif m == "size":
                    self.size = n
                elif m == "x":
                    self.x = n
                elif m == "y":
                    self.y = n

    def to_dictionary(self):
        '''doc of square'''
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.x} - {self.width}"
