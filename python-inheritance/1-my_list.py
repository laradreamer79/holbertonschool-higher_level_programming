#!/usr/bin/python3
"""Defines a custom list class"""

class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order without modifying original"""
        print(sorted(self))
