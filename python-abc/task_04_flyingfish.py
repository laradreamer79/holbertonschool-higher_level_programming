#!/usr/bin/env python3
"""
Demonstrates multiple inheritance using Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """
    Fish class.
    """

    def swim(self):
        """
        Print swimming behavior of a fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Bird class.
    """

    def fly(self):
        """
        Print flying behavior of a bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird.
    """

    def swim(self):
        """
        Print swimming behavior of a flying fish.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Print flying behavior of a flying fish.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Print habitat of a flying fish.
        """
        print("The flying fish lives both in water and the sky!")
