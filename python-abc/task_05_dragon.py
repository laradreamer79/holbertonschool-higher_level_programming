#!/usr/bin/env python3
"""
Demonstrates the use of mixins by creating a Dragon
that can both swim and fly.
"""


class SwimMixin:
    """
    Mixin that provides swimming capability.
    """

    def swim(self):
        """
        Print swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying capability.
    """

    def fly(self):
        """
        Print flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that combines swimming and flying abilities.
    """

    def roar(self):
        """
        Print roaring behavior of the dragon.
        """
        print("The dragon roars!")
