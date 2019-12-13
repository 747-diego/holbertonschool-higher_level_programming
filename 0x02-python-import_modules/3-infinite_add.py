#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Sum = 0
    for index in range(1, len(sys.argv)):
        Numbers = int(sys.argv[index])
        Sum += Numbers
    print("{}".format(Sum))
