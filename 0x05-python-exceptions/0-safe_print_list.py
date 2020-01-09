#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for iterator in range(x):
        # index += 1
        try:
            index += 1
            print("{}".format(my_list[iterator]), end="")
        except:
            index -= 1
            break
    print()
    return index
