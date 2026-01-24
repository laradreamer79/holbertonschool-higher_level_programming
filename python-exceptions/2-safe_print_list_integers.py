#!/usr/bin/python3
"""Print and count integers in a list."""


def print_and_count_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers and return count."""
    count = 0
    for i in range(x):
        # IMPORTANT: do NOT catch IndexError here (so traceback appears if x is too big)
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
