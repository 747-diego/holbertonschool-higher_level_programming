#!/usr/bin/python3
# """ .items() is a function used to specify the number being multiplied. """


def multiply_by_2(a_dictionary):
    NewDictionary = {}
    for Name, Number in a_dictionary.items():
        NewDictionary[Name] = 2 * Number
    return NewDictionary
