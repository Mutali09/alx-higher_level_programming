#!/usr/bin/python3
"""This module defines a Square class."""
class Square:
    """Represents a square.
    Attributes:
       __size (int): Thesize of the square.
    """
    def __init__(self, size=0):
        """Initialize a new instance of the Square class.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.__validate_size()
    def __validate_size(self):
        """Validate the size attribute.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Calculated the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
