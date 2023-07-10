#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """ inherits from class int"""

    def __eq__(self, other):
        """ returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ returns == check """
        return int.__eq__(self, other)
