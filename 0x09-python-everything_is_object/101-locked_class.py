#!/usr/bin/python3
"""containts a clas that avoids
dynmaically created attributes
"""


class LockedClass():
    """
    instance attribute is called first_name
    """

    __slots__ = ('first_name', )
