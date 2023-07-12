#!/usr/bin/python3
"""creates an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    """def load_from_json_file."""
    with open(filename) as m:
        return json.load(m)
