#!/usr/bin/env python3
"""
Defines VerboseList, a subclass of list that prints notifications
when items are added or removed.
"""


class VerboseList(list):
    """
    VerboseList extends the built-in list class and prints messages
    whenever the list is modified.
    """

    def append(self, item):
        """
        Add an item to the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from iterable and print a notification.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop an item from the list and print a notification.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
