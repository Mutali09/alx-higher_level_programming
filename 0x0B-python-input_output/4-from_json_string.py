#!/usr/bin/python3
# 6-from_jason_string.py
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the python object strucuture represented by JSON string."""
    return json.loads(my_str)
