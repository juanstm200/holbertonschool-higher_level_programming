#!/usr/bin/python3
import sys
if __name__ == '__main__':
  lent = len(sys.argv)
  if lent > 1:
    print("{:d} arguments:".format((lent - 1)))
  elif lent == 2:
    print("{:d} argument:".format((lent - 1)))
  elif lent == 1:
    print("{:d} arguments.".format((lent - 1)))
  for i in range (1, lent):
    print("{:d}: {}".format(i, sys.argv[i]))
