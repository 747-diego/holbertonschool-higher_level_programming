#!/usr/bin/python3

"""

Write a function that prints.

My name is <first name> <last name>

You are not allowed to import any module

"""


def say_my_name(first_name, last_name=""):
    """

    First_name and Last_name must be strings otherwise.

    raise a TypeError

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
