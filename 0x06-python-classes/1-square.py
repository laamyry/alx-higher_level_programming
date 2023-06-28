#!/usr/bin/python3
"""defines a square by: (based on 0-square.py)"""


class Square:
    """Represents a square with a given size."""

    def __init__(self, size):
        """Initializes a new Square object.

        Args:
            size (int):  size of the new square.
        """
        self._size = size
