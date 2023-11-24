#!/usr/bin/python3
'''Rectangle module'''


class Rectangle:
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for m, arg in enumerate(args):
                setattr(self, attrs[m], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return f"[Rectangle]
        ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
