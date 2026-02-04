#!/usr/bin/env python3
"""Serialize and deserialize data using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")

    # Create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Write XML to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
