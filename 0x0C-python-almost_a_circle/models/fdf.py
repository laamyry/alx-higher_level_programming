#!/usr/bin/python3
'''module doc for square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

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
        return {"id": self.id, "size": self.width,
            "x": self.x, "y": self.y}

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.x} - {self.width}"
