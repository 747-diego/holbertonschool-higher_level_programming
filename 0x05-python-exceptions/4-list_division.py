#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ElementList = []

    index = 0
    while index < list_length:
        try:
            divs = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
            divs = 0
        except TypeError:
            print("wrong type")
            divs = 0
        except IndexError:
            print("out of range")
            divs = 0
        finally:
            ElementList.append(divs)
            divs = 0
        index += 1
    return ElementList
