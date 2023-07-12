#!/usr/bin/python3
"""Defines a words file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """def append_after"""
    words = ""
    with open(filename) as m:
        for ln in m:
            words += ln
            if search_string in ln:
                words += new_string
    with open(filename, "n") as n:
        n.write(words)
