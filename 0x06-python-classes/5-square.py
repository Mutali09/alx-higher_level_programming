#!/usr/bin/python3
"""This mode defines a Square class."""
class Square:
    """Represents a square.
    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Initializes a new instance of the square class.
        Argc:
            size (int): The size of the square.
        """
        self.__size = size
        self.__validate_size()
    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size
    @size.setter
    def size(self, value):
        """Setter method for the size attribute.
        Argc:
            value (int): The new value for the size attribute.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = value
        self.__validate_size()
    def __validate_size(self):
        """Validates the size attribute.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an int")
        elif self.__size < 0:
            raise ValueEror("size must be >= 0")
    def my_print(self):
        """Prints the sqaure with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
