#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (int): The new value for the size attribute.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__validate_size(value)

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute.

        Args:
            value (tuple): The new value for the position attribute.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.__validate_position(value)

    def __validate_size(self, size):
        """Validates the size attribute.

        Args:
            size (int): The size to validate.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __validate_position(self, position):
        """Validates the position attribute.

        Args:
            position (tuple): The position to validate.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = position
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
