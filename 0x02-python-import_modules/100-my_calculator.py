#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    oper = sys.argv[2]
    if oper != "+" and oper != "-" and oper != "*" and oper != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if oper == "+":
        print("{} {} {} = {}".format(a, oper, b, add(a, b))) 
    if oper == "-":
        print("{} {} {} = {}".format(a, oper, b, sub(a, b)))
    if oper == "*":
        print("{} {} {} = {}".format(a, oper, b, mul(a, b)))
    if oper == "/":
        print("{} {} {} = {}".format(a, oper, b, div(a, b)))
