#!/usr/bin/env python3
"""
Defines CountedIterator, an iterator that keeps track of
how many items have been iterated over.
"""


class CountedIterator:
    """
    CountedIterator wraps an iterable and counts how many
    elements have been returned during iteration.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable: Any iterable object.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.
        """
        item = next(self.iterator)  # may raise StopIteration
        self.count += 1
        return item

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def get_count(self):
        """
        Return the number of items iterated over so far.
        """
        return self.count
