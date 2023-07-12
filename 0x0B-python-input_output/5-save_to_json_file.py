#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """def save_to_json_file"""
    with open(filename, "w") as m:
        json.dump(my_obj, m)
