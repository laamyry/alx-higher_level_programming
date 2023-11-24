#!/usr/bin/python3
'''Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        '''__init__'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value, fl=True):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if fl and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not fl and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        ar = self.width * self.height
        return ar

    def display(self):
        dis = '\n' * self.y + (' ' * self.x + '#' *
                               self.width + '\n') * self.height
        print(dis, end='')

    def __str__(self):
        return (
            f'[{type(self).__name__}] ({self.id}) '
            f'{self.x}/{self.y} - {self.width}/{self.height}'
        )

    def up_display(self, id=None, width=None, height=None, x=None, y=None):
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        if args:
            self.up_display(*args)
        elif kwargs:
            self.up_display(**kwargs)
