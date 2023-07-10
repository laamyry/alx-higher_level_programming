#!/usr/bin/python3
"""class MyInt that inherits from int:"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    def __new__(cls, *args, **kwargs):
        """def __new__"""
        return (super(MyInt, cls).__new__(cls, *args, **kwargs))

    def __eq__(self, other):
        """def __ex__"""
        return (int(self) != other)

    def __ne__(self, other):
        """def __na__"""
        return (int(self) == other)
