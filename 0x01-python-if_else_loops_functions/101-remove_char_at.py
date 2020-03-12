#!/usr/bin/python3
def remove_char_at(str, n):
    """ Copy string and remove character """

    NewString = ""
    for index in range(0, len(str)):
        if index != n:
            NewString = NewString + NewString[index]
    return NewString
    