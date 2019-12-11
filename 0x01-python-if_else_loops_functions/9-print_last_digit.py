#!/usr/bin/python3
def print_last_digit(number):
    Digit = abs(number) % 10
    print("{:d}".format(Digit), end="")
    return Digit
