#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file data to JSON format and save it to data.json.
    Returns True on success, False on failure.
    """
    try:
        data = []

        # Read CSV file
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        # Write JSON file
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
