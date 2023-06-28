#!/usr/bin/python3
"""defines a square by: (based on 1-square.py)"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square object with the given size.

        Args:
            size (int): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
