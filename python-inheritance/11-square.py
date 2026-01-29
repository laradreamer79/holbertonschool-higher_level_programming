#!/usr/bin/python3
"""
Defines a Square class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    Represents a square using size validated by BaseGeometry.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size ** 2
