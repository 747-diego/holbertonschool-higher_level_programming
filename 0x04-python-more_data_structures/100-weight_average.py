#!/usr/bin/python3
def weight_average(my_list=[]):

    if len(my_list) is 0:
        return 0

    average = 0
    numbersTuple = []
    for index in my_list:
        average += index[1]
        numbersTuple.append(index[0] * index[1])
    return sum(numbersTuple) / average
