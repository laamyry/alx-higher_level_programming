#!/usr/bin/python3
"""class Student that defines a student by: (based on 10-student.py)"""


class Student:
    """class Student3"""

    def __init__(self, first_name, last_name, age):
        """def __init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """def to_json"""
        if (type(attrs) == list and all(type(ele)
                                        == str for ele in attrs)):
            return ({m: getattr(self, m) for m in attrs if hasattr(self, m)})
        return self.__dict__

    def reload_from_json(self, json):
        """def reload_from_json"""
        for m, n in json.items():
            setattr(self, m, n)
