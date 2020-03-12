#!/usr/bin/python3
from magic_calculation_102 import add, sub

    if Num1 < Num2:
        outcome = add(Num1, Num2)
        for index in range(4, 6):
            outcome = add(outcome, index)
        return outcome
    return sub(Num1, Num2)
