#!/usr/bin/python3
"""File writing function definition."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename (str): name of the file to write
        text (str): the text to write to the file
    Return:
        The number of characters written.
    """
    with open(fiename, "w", encoding="utf-8") as f:
        return f.write(text)
