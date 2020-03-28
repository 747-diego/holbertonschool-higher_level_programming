#!/usr/bin/python3
def magic_calculation(a, b):
    calculation = 0
    for index in range(1, 3):
        try:
            if (index > a):
                raise Exception("Too far")
            calculation += (a ** b)/index
        except:
            calculation = a+b
            break
    return calculation
