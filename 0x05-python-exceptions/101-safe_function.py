#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        SafeFCT = fct(*args)
        return SafeFCT
    except Exception as errMsg:
        print("Exception: {}".format(errMsg), file=stderr)
        return None
