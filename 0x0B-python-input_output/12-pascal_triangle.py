#!/usr/bin/python3
"""function that returns pascal triangle"""


def pascal_triangle(n):
    """ Function that returns the pascal triangle"""

    pro = []
    pyst = []

    for i in range(n):
        list_ls = []
        p1 = -1
        p2 = 0
        for j in range(len(pyst) + 1):
            if p1 == -1 or p2 == len(prev):
                list_ls += [1]
            else:
                list_ls += [pyst[p1] + pyst[p2]]
            p1 += 1
            p2 += 1
        pro.append(list_ls)
        pyst = list_ls[:]

    return pro
