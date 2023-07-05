#!/usr/bin/python3
""" defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """create a rectangle."""
    def __init__(self, width=0, height=0):
        """create new rectangle.
        Args:
            width (int):  new rectangle width.
            height (int): new rectangle height.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0")
        self._height = value
