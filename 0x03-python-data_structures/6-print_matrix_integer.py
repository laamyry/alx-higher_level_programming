#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if n not in 0:
                print(" ", end='')
            print("{:d}".format(matrix[m][n]), end='')
        print()
