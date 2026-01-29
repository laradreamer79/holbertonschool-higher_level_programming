#!/usr/bin/python3
"""
This module defines abstract and concrete shape classes.

It demonstrates the use of abstract base classes (ABCs),
interfaces, and duck typing to work with different shapes
in a uniform way.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class that defines the interface for shapes.

    Any class that inherits from Shape must implement
    the area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.

        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.

        This method must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Represents a circle shape.

    Inherits from Shape and implements area and perimeter
    calculations specific to a circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle shape.

    Inherits from Shape and implements area and perimeter
    calculations specific to a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int or float): The width of the rectangle.
            height (int or float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print information about a shape using duck typing.

    This function assumes that the given object has
    area() and perimeter() methods, without checking
    its concrete type.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
