#!/usr/bin/python3
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0:
            print("Fizz", end=" ")
        if index % 5 == 0:
            print("Buzz", end=" ")
        if index % 3 != 0 and index % 5 != 0:
            print("{:d}".format(index), end=" ")
