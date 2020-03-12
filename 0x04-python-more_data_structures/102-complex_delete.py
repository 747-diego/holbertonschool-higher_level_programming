#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    KeysList = []
    for keys, existing in a_dictionary.items():
        if value is existing:
            KeysList.append(keys)
    if len(KeysList) > 0:
        for SpecifiedValue in KeysList:
            del a_dictionary[SpecifiedValue]
    return a_dictionary
