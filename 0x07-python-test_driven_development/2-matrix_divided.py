#!/usr/bin/python3
''' divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(message)
    row_l = []
    counter = 0

    for row in matrix:
        if type(row) is not list:
            raise TypeError(message)
        row_l.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(message)
        counter += 1
    if len(set(row_l)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    n_matrix = list(map(lambda row: list(
        map(lambda x: round(x/div, 2), row)), matrix))
    return n_matrix
