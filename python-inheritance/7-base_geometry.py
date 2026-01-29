#!/usr/bin/python3
"""
Defines a BaseGeometry class with integer validation.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): the name of the parameter
            value (int): the value to validate
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
