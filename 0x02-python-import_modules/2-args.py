#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    lent = len(argv)
    if lent > 1:
        print("{:d} arguments:".format((lent - 1)))
    elif lent == 2:
        print("{:d} argument:".format((lent - 1)))
    elif lent == 1:
        print("{:d} arguments.".format((lent - 1)))
    for i in range (1, lent):
        print("{:d}: {:s}".format(i, argv[i]))
