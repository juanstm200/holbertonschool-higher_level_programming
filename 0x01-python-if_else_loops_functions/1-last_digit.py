#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

var = "Last digit of {:d}".format(number)
num = abs(number) % 10;
if number < 0:
  num = -num

if num == 0:
    print("{} is {} and is 0".format(var, num))
elif num > 5:
    print("{} is {} and is greater than 5".format(var, num))
elif num < 6 and not 0:
    print("{} is {} and is less than 6 and not 0".format(var, num))
