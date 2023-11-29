#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a (int or float): The first number
        b (int or float): The second number. Defaults to 98.
    Returns:
        int: The sum of a and b as an integer.
    Raises:
        TypeError: If either a or b is non integer or non float
    """
    if type(a) not in [inf, float]:
        raise TypeError("a must be an integer or float")
    if type(b) no in [int, float]:
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)
    Return (a + b)
