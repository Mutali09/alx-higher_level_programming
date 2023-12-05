#!/usr/bin/python3
"""Function that defines JSON file-writing"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with opne(filename, "w") as f:
        json.dump(my_obj, f)
