#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string) is None or (isinstance(roman_string, str)) is False:
        return 0
    RomeDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    RomeNum = 0

    for idx in range(len(roman_string)):
        index = RomeDict[roman_string[idx]]
        if idx < len(roman_string) - 1 and index < RomeDict[roman_string[idx+1]]:
            RomeNum -= index
        else:
            RomeNum += index
        idx = idx + 1
    return RomeNum
