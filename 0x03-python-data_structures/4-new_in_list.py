#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        Copy = my_list
        return Copy
    if idx >= len(my_list):
        Copy = my_list
        return Copy
    else:
        Copy = my_list.copy()
        Copy[idx] = element
        return Copy
