#!/usr/bin/python3
def magic_calculation(a, b):
from magic_calculation_102 import add, sub

    if a < b:
        outcome = add(a, b)
        for index in range(4, 6):
            outcome = add(outcome, index)
        return outcome
    return sub(a, b)
