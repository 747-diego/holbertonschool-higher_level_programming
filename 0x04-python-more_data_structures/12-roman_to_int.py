#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string) is None or (isinstance(roman_string, str)) is False:
        return 0
    RomanDictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    RomeNum = 0
    for idx in range(len(roman_string)):
        if idx < len(roman_string) - 1 and RomanDictionary[roman_string[idx]] < RomanDictionary[roman_string[idx+1]]:
            RomeNum -= RomanDictionary[roman_string[idx]]
        else:
            RomeNum += RomanDictionary[roman_string[idx]]
        idx = idx + 1
    return RomeNum
