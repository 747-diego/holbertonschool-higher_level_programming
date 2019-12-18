#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    Ta = tuple_a
    Tb = tuple_b

    if len(Ta) == 0:
        Ta = (0, 0)
    elif len(Ta) == 1:
        Ta = (Ta[0], 0)
    if len(Tb) == 0:
        Tb = (0, 0)
    elif len(Tb) == 1:
        Tb = (Tb[0], 0)
    SumOfTP = (Ta[0] + Tb[0], Ta[1] + Tb[1])
    return SumOfTP
