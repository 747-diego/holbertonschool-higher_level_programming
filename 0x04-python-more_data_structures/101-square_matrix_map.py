#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda line: list(map(lambda TwoD: TwoD**2, line)), matrix))
