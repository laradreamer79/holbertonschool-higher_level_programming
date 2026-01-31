#!/usr/bin/env python3
"""
This module demonstrates the use of abstract base classes (ABCs)
and duck typing in Python.

It defines a generic Shape interface using the abc module, along with
concrete implementations for Circle and Rectangle. A standalone
function, shape_info, operates on shape-like objects without explicitly
checking their types, relying instead on the presence of expected
methods.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class that defines the interface for geometric shapes.

    Any class that inherits from Shape must implement the area and
    perimeter methods. This ensures a consistent API while allowing
    different shape implementations.
    """

    @abstractmethod
    def area(self):
        """
        Compute and return the area of the shape.

        Subclasses must override this method to provide a concrete
        implementation specific to the shape they represent.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute and return the perimeter of the shape.

        Subclasses must override this method to calculate the perimeter
        according to their geometric properties.
        """
        pass


class Circle(Shape):
    """
    Represents a circle shape.

    The circle is defined by its radius and provides implementations
    for calculating its area and perimeter.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculate and return the area of the circle.

        Uses the mathematical formula: π * r².
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate and return the perimeter of the circle.

        Uses the mathematical formula: 2 * π * r.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle shape.

    The rectangle is defined by its width and height and implements
    methods to calculate its area and perimeter.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float or int): The width of the rectangle.
            height (float or int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Uses the mathematical formula: width * height.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Uses the mathematical formula: 2 * (width + height).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Display information about a shape.

    This function relies on duck typing rather than explicit type
    checking. Any object passed to this function is expected to provide
    area() and perimeter() methods.

    Args:
        shape: An object that implements area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
