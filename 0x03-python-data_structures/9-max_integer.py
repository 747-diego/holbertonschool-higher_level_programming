#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    MaxInt = my_list[0]
    for index in my_list:
        if MaxInt < index:
            MaxInt = index
    return MaxInt
