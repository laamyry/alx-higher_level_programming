#!/usr/bin/python3
""" returns a list of lists of integers representing the Pascal’s triangle of n:"""


def pascal_triangle(n):
    """def pascal_triangle"""
    if n <= 0:
        return ([])

    triangle = [[1]]
    while len(triangle) != n:
        trian = triangle[-1]
        temp = [1]
        for m in range(len(trian) - 1):
            temp.append(trian[m] + trian[m + 1])
        temp.append(1)
        triangle.append(temp)
    return (triangle)
