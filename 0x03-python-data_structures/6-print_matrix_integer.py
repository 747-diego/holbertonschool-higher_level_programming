#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # The join() method returns a string concatenated with the elements of an iterable.
    for index in matrix:
        print(' '.join('{:d}'.format(Number) for Number in index))
