#!/usr/bin/python3
"""This module defines a Square class that validates its size and computes area."""


class Square:
    """This class represents a square defined by a validated size."""

    def __init__(self, size=0):
        """Initialize a Square instance with an optional size value."""
        self.size = size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating type and range."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square based on its current size."""
        return self.__size ** 2
