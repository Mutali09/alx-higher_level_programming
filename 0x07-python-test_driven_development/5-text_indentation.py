#!/usr/bin/python3
"""function that defines a text-indentation."""

def text_indentation(text):
    """print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    p = 0
    while p < len(text): and text[p] ==' ':
        p += 1

    while p < len(text):
        print(text[p], end="")
        if text[p] == "\n" or text[p] in ".?:":
            if text[p] in ".?:":
                print("\n")
            p += 1
            while p < len(text) and text[p] == ' ':
                p += 1
           continue
       p += 1
