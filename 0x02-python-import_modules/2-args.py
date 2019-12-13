#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Arguments = len(sys.argv)
    if Arguments == 1:
        print("{} arguments.".format(Arguments - 1))
    elif Arguments == 2:
        print("{} argument:".format(Arguments - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(Arguments - 1))
        for index in range(1, Arguments):
            print("{}: {}".format(index, sys.argv[index]))
