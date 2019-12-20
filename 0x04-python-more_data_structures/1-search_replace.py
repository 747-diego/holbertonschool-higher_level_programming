#!/usr/bin/python3
def search_replace(my_list, search, replace):
    NewList = my_list
    return [replace if index == search else index for index in NewList]
