#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for ch in text:
        line += ch
        if ch in ".?:":
            print(line.strip())
            print()
            line = ""

    if line.strip() != "":
        print(line.strip(), end="")
