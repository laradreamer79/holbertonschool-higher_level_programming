#!/usr/bin/env python3
"""pickle serialization module for saving and loading python objects."""

import pickle


def serialize__and_save_to_file(data, filename):
    """serialize a Python object and save it to a pickle file."""
    with open(filename, mode"wb") as f:
        pickle.dump(data, f)


def load_and_deserilize(filename):
    """ load a pickle file and return the deserialized Python object."""
    with open(filename, mode="rb") as f:
        return pickle.load(f)
