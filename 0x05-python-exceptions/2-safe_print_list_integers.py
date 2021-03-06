#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for iterator in range(0, x):
        try:
            # index += 1
            print("{:d}".format(my_list[iterator]), end='')
            index += 1
        except(ValueError, TypeError):
            pass
    print()
    return index
