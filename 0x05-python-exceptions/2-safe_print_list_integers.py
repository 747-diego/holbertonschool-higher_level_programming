#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for iterator in range(x):
        # index += 1
        try:
            index += 1
            print("{:d}".format(my_list[iterator]), end='')
        except(TypeError, ValueError):
            continue
    print()
    return index
