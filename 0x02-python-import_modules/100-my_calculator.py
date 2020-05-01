#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    oper = argv[2]
    if oper != "+" and oper != "-" and oper != "*" and oper != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if oper == "+":
        print("{} {} {} = {}".format(a, oper, b, add(a, b))) 
    if oper == "-":
        print("{} {} {} = {}".format(a, oper, b, sub(a, b)))
    if oper == "*":
        print("{} {} {} = {}".format(a, oper, b, mul(a, b)))
    if oper == "/":
        print("{} {} {} = {}".format(a, oper, b, div(a, b)))
