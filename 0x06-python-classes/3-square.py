#!/usr/bin/python3

"""defines a square by: (based on 2-square.py) """


class Square:
    """A class representing a square."""

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

    def area(self):
        """
        Calculate square's area.
        Returns: The square of the size.

        """

        return (self.__size ** self.__size)
