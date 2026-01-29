#!/usr/bin/python3
"""Defines a MyInt class that inverts equality operators."""


class MyInt(int):
    """MyInt class that inverts == and != operators."""

    def __eq__(self, other):
        """Invert equality: == behaves like !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert inequality: != behaves like =="""
        return super().__eq__(other)
