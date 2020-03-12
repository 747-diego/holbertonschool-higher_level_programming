#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda lin: list(map(lambda TwoD: TwoD**2, lin)), matrix))
