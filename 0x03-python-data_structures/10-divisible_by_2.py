#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    NewList = []
    for index in my_list:
        if index % 2 == 0:
            NewList.append(True)
        else:
            NewList.append(False)
    return NewList
