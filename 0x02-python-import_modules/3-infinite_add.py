#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    lent = len(argv)
    numbers = 0
    for i in range(1, lent):
        numbers = numbers + int(argv[i])
    print("{:d}".format(numbers))
