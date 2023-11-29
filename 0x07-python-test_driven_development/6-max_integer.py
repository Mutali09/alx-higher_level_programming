#!/usr/bin/python3
"""Module to determine max integer in a list
"""

def max_integer(list=[]):
    """Function that determine and return the max integer in a list of integers
        the function returns None with an emplty list
    """
    if len(list) = 0:
        return None
    result = list[0]
    p = 1
    while p < len(list):
        if list[p] > result:
            result = list[p]
        p += 1
    return result
