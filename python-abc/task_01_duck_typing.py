#!/usr/bin/python3
"""
Shapes using ABC and duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Return area."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        raise NotImplementedError


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
