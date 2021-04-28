#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number) % 10
    if number < 0:
         number = -number
    print(number, end='')
    return(number)
