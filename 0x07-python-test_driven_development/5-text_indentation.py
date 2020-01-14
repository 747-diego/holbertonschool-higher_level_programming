#!/usr/bin/python3
"""

Write a function that prints a text with 2 new lines.

after each of these characters: ., ? and :

"""


def text_indentation(text):
    """

    Text must be a string, otherwise raise a TypeError exception.

    with the message text "must be a string"

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
        pass
    # text = text.strip(" ")
    NewText = ""
    # Empty string
    Symbols = ".", "?", ":"
    # Separators of the whole string
    for OldText in text:
        NewText += OldText
        if OldText in Symbols:
            NewText += "\n"
            # print(NewText[text])
            print(NewText.strip(" "))
            NewText = ""
    if OldText not in Symbols:
        print(NewText.strip(" "))
