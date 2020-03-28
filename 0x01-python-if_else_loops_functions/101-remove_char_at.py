#!/usr/bin/python3
def remove_char_at(str, n):
    NewString = ""
    for index in range(0, len(str)):
        if index != n:
            NewString = NewString + str[index]
    return NewString
