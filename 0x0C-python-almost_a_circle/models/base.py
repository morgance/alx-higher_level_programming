#!/usr/bin/python3
""" module that has class base """

import json
import csv
import os.path


class Base:
    """"base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instnce"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
