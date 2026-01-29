#!/usr/bin/python3
"""Defines an abstract Animal class."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass
