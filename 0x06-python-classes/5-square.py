#!/usr/bin/python3
"""defines a square by: (based on 4-square.py)"""


class Square:
    """class represents square"""

    def __init__(self, size=0):
        """ square class Initializing.
        Args:
            size: represnets the size.
        Raises:
            TypeError: if size not integer.
            ValueError: if size less than 0.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """size square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate square's area.
        Returns: The square of the size.

        """
        return (self.__size ** 2)

    def my_print(self):
        """print square in # """

        if self.__size == 0:
            print()

        for m in range(self.__size):
            print("#" * self.__size)
