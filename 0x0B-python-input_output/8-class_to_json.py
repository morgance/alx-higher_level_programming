#!/usr/bin/python3
""" function that returns the dictionary description with a simple
data structure for a JSON serialization of an object"""


def class_to_json(obj):
    """ retuns the dictionary description of an obj """

    boo = {}
    if hasattr(obj, "__dict__"):
        boo = obj.__dict__.copy()
    return boo
