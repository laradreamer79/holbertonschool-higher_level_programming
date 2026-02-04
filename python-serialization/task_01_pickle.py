#!/usr/bin/env python3
"""Pickle serialization module for saving and loading Python objects."""

import pickle


def serialize_and_save_to_file(data, filename):
    """Serialize a Python object and save it to a pickle file."""
    with open(filename, mode="wb") as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """Load a pickle file and return the deserialized Python object."""
    with open(filename, mode="rb") as f:
        return pickle.load(f)
