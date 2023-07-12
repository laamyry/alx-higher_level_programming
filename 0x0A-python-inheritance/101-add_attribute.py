#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible:"""


def add_attribute(obj, att, value):
    """Raise a TypeError exception, with the message
    can't add new attribute if the object can’t have new attribute
    You are not allowed to use try/except
    You are not allowed to import any module
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
