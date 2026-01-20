#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in range(len(row)):
            end_char = " " if j != len(row) - 1 else ""
            print("{:d}".format(row[j]), end=end_char)
        print()
