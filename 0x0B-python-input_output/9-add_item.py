#!/usr/bin/python3
"""TASK 9 Load, add, save."""


from sys import argv
from os.path import isfile

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

"""Write a script that adds all arguments to a Python list."""
"""Then save them to a file."""
file = "add_item.json"
ItemsToBeAdded = []
if isfile(file):
    ItemsToBeAdded = load_from_json_file(file)


for index in range(1, len(argv)):
    ItemsToBeAdded.append(argv[index])

save_to_json_file(ItemsToBeAdded, file)
