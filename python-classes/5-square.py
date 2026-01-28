#!/usr/bin/python3
"""
This module defines a Square class that validates its size and can print
a square using the character '#'.
"""


class Square:
    """
    This class represents a square and controls access to its size attribute
    using getter and setter methods, and can compute and print the square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with an optional size value.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square after validating its type and value.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square to stdout using the character '#'.

        If size is 0, this prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
