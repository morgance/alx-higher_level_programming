#!/usr/bin/python3
""" function that writes to a atring to text file"""


def write_file(filename="", text=""):
    """ Function that writes to a file  """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
