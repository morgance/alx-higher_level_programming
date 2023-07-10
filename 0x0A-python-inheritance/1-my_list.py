#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
