#!/usr/bin/python3
def uniq_add(my_list=[]):
    UniqueList = my_list
    return sum(index for index in set(UniqueList))
