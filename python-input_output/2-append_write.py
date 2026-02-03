#!/usr/bin/python3
"""append a string to a text file, return the number of charechters added"""


def append_write(filename="",text=""):
    """function that append a string to a file,return the number of addotions"""
    with open(filename, mode="a", encoding="utf-8") as f:
         return f.write(text)
