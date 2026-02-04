#!/usr/bin/env python3
"""CSV serialization and deserialization helpers."""

import csv


def serialize_to_csv(data, filename):
    """
    Serialize data to a CSV file.

    data can be:
    - a list of dictionaries (recommended)
    - a single dictionary
    Returns True on success, None on failure.
    """
    try:
        rows = data if isinstance(data, list) else [data]
        if not rows:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                pass
            return True

        if not all(isinstance(r, dict) for r in rows):
            return None

        fieldnames = []
        seen = set()
        for row in rows:
            for key in row.keys():
                if key not in seen:
                    seen.add(key)
                    fieldnames.append(key)

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        return True
    except Exception:
        return None


def load_from_csv(filename):
    """
    Load data from a CSV file and return it.

    Returns:
    - list of dictionaries on success
    - None on failure
    """
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [dict(row) for row in reader]
    except Exception:
        return None
