#!/usr/bin/python3
"""
This module defines a Square class that represents a square
using a validated size attribute and provides a method
to compute the area of the square.
"""


class Square:
    """
    This class represents a square and controls access
    to its size attribute using getter and setter methods.
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
