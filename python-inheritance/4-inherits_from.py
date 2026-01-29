#!/usr/bin/python3
"""
Defines a function that checks if an object is an instance
of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class
    (but not an instance of a_class itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
