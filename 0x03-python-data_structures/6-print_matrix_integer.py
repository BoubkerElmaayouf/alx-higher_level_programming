#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for y in range(len(row)):
            if y == len(row) - 1:
                print("{:d}".format(row[y]), end="")
            else:
                print("{:d} ".format(row[y]), end="")
        print()
