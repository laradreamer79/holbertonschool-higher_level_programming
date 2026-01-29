#!/usr/bin/python3
"""
Defines a MyInt class that inverts the behavior of equality operators.
"""


class MyInt(int):
    """
    MyInt is a subclass of int that inverts the behavior of
    the == and != operators.
    """

    def __eq__(self, other):
        """
        Invert equality operator (== behaves like !=).
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert inequality operator (!= behaves like ==).
        """
        return super().__eq__(other)
