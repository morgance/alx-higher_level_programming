#!/usr/bin/python3
"""function returns an object by a JSON representation
"""
import json


def from_json_string(my_str):
    """returns an object by a JSON representatio"""
    return json.loads(my_str)
