#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    DifferenceOne = set_1.difference(set_2)
    DifferenceTwo = set_2.difference(set_1)
    CombinedDifference = DifferenceOne.union(DifferenceTwo)
    return CombinedDifference
