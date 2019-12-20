#!/usr/bin/python3
""" MAX is a function used to find the biggest number. """
""" items() is a function used to specify where in the dictionary. """


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for Name, Number in a_dictionary.items():
        if Number is max(a_dictionary.values()):
            return Name
