#!/usr/bin/python3
""" function that appends to a text file"""


def append_write(filename="", text=""):
    """appends to a text file"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
