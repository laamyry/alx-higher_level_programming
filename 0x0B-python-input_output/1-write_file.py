#!/usr/bin/python3
""" writes a string to a text file (UTF8)
and returns the number of characters written:"""


def write_file(filename="", text=""):
    """def write_file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
