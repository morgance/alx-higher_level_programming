#!/usr/bin/python3
"""function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found"""

    line_py = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            line_py += [line]
            if line.find(search_string) != -1:
                line_py += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(line_py))
