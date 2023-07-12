#!/usr/bin/python3
"""class Student that defines a student by:"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """ def __init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """def to_json"""
        return self.__dict__
