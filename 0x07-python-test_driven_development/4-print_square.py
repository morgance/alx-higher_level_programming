#!/usr/bin/python3
"""
Prints a square with character "#"
"""


def print_square(size):
    """
    Returns a square with # character
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")

    else:
        print("\n".join(["#" * size for rows in range(size)]))
