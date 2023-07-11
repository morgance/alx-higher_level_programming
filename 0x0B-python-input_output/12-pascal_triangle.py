#!/usr/bin/python3
"""function that returns pascal triangle"""


def pascal_triangle(n):
    """Returns pascal's trangle """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        pro = triangles[-1]
        tsr = [1]
        for i in range(len(pro) - 1):
            tsr.append(pro[i] + pro[i + 1])
        tsr.append(1)
        triangles.append(tsr)
    return triangles
