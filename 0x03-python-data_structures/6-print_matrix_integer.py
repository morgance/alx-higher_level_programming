#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for num in range(len(matrix[i])):
            if num != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][num]), end='')
        print()
