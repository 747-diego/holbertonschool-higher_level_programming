#!/usr/python3
# using the sorted function to sort a dictionary
def print_sorted_dictionary(a_dictionary):
    for keys in sorted(a_dictionary):
        print("{}: {}".format(keys, a_dictionary[keys]))
