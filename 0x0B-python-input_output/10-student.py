#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """def __init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """def to_json"""
        if (type(attrs) == list and all(type(ele)
                                        == str for ele in attrs)):
            return ({k: getattr(self, k) for k in attrs if hasattr(self, k)})
        return self.__dict__
