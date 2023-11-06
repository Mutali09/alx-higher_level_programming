#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for q in range(len(matrix)):
        for p in range(len(matrix[q])):
            print("{:d}".format(matrix[q][p]), end="")
            if p != (len(matrix[q]) - 1):
                print(" ", end="")
                print("")
