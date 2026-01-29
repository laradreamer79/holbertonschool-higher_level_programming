#!/usr/bin/python3
"""
Defines an abstract Animal class and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    """

    @abstractmethod
    def sound(self):
        """
        Return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    """

    def sound(self):
        """
        Return the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    """

    def sound(self):
        """
        Return the sound of a cat.
        """
        return "Meow"
