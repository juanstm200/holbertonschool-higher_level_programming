#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    lent = len(argv)
    operador = ['+', '-', '*', '/']
    if lent != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
  
    a = int(argv[1])
    b = int(argv[3])
    for i in range(1,lent):
        if argv[2] == operador[0]:
            print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
            break
        elif argv[2] == operador[1]:
            print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
            break
        elif argv[2] == operador[2]:
            print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
            break
        elif argv[2] == operador[3]:
            print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))
            break
        else:
            print("Unknown operator. Available operators: +, -, * and /")      
            exit(1)
